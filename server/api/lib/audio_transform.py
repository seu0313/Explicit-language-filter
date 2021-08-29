import os
from moviepy.video.io.VideoFileClip import VideoFileClip
import numpy as np
from typing import Union
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from pydub import AudioSegment

from api.lib.gcp_transcibe import *
from api.lib.hangul_transform import *
from api.models import get_file_path, get_dir_path


AUDIO_FORMAT = ['.mp3']
VIDEO_FORMAT = ['.mp4']
SUPPORT_FORMAT = AUDIO_FORMAT + VIDEO_FORMAT

def get_filtered_file(file: Union[InMemoryUploadedFile, TemporaryUploadedFile], filename, format):
    """ 오디오 파일을 받아 비속어 처리

    @status `Active Review` \\
    @params `file: Union[InMemoryUploadedFile, TemporaryUploadedFile]` \\
    @params `format` \\
    @returns `AudioSegment File` """
    

    if format in VIDEO_FORMAT:
        video = VideoFileClip(file.temporary_file_path())
        audio = video.audio

        FILE_DIR = os.path.join(settings.MEDIA_ROOT, get_file_path(None, f'{filename}.mp3'))
        audio.write_audiofile(FILE_DIR)
        file_path = FILE_DIR

    else:
        path = get_file_path(None, file.name)
        file_path = default_storage.save(
            os.path.join(settings.MEDIA_ROOT, path), 
            ContentFile(file.read())
        )

    sound = AudioSegment.from_file_using_temporary_files(file_path)

    try:
        response = transcribe_local(file_path)
        timeline, swear_timeline, words = google_response(response)

        print(f'timeline : {timeline}\n')
        print(f'swear_timeline : {swear_timeline}\n')
        print(f'words : {words}\n')

        # deep

        # ============================================================================
        deep_swear_timeline = detect_swear(timeline=timeline, words=words)
        swear_timeline = deep_swear_timeline
        # swear_timeline = list(set(gcp_swear_timeline) & set(deep_swear_timeline))  # 테스트
        # swear_timeline = list(set(gcp_swear_timeline) | set(deep_swear_timeline))  # 실사용

        print(f'deep swear_timeline : {deep_swear_timeline}')
        print(f'swear_timeline : {swear_timeline}')
        # ============================================================================


        # ============================================================================
        # i = 0
        # beep = create_beep(duration=1000)
        # mixed = sound.overlay(beep, position=swear_timeline[i][0], gain_during_overlay=-50)
        mixed_final = sound

        for i in range(len(swear_timeline)):
            beep = create_beep(duration=swear_timeline[i][1] - swear_timeline[i][0])
            mixed_final = mixed_final.overlay(beep, position=swear_timeline[i][0], gain_during_overlay=-50)
        # ============================================================================

        '''
        mixed_final.export(os.path.join(MEDIA_DIR, 'temp.mp3'), format='mp3')

        video_clip = VideoFileClip(video_file.temporary_file_path(), audio=False)
        print(video_clip)
        video_clip: VideoFileClip = video_clip.set_audio(sound)
        print(video_clip)

        mixed_clip = video_clip.
        
        video_clip.write_videofile(video_file.temporary_file_path(), \
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='temp-audio.m4a', 
            remove_temp=True
        )
        '''
    except Exception as err:
        print(err)

    return mixed_final


def get_audio_with_meta(file: AudioSegment, filename: str, metadata: dict, format='mp3'):
    """오디오에 메타 데이터를 포함하여 파일을 생성하는 함수입니다.
    @status `Accepted` \\
    @params `file: AudioSegment` \\
    @params `filename: str` \\  
    @params `metadata: dict` \\
    @params `format: str` \\
    @Returns `새로운 오디오 파일` """

    FILE_DIR = os.path.join(settings.MEDIA_ROOT, get_dir_path())
    file.export(os.path.join(FILE_DIR, f'{filename}.{format}'), format=format, tags=metadata)
    return get_file_path(None, f'{filename}.{format}')


def get_metadata(validated_data: dict):
    """파일 메타 데이터 생성을 수행하는 함수입니다.
    @status `Accepted` \\
    @params `validated_data: dict` \\
    @returns `메타 데이터 JSON 파일` """
    
    metadata = {
        "title": validated_data['title'],
        'album': validated_data['album'],
        "composer": validated_data['composer'],
        "copyright": validated_data['copyright'],
    }
    return metadata


def create_beep(duration: int, sps: int=16000):
    """비프음 생성 함수입니다. sps은 `16khz`을 기본값으로 되어있으며 `durantion(ms)` 길이의 삐- 오디오를 생성합니다.

    @status `Accepted` \\
    @params `duration(ms): int` \\
    @params `sps(hz): int=16000` \\
    @returns `beep audio 파일` """

    freq_hz = 1000.0
    vol = 1

    esm = np.arange(duration / 1000 * sps)
    wf = np.sin(2 * np.pi * esm * freq_hz / sps)
    wf_quiet = wf * vol
    wf_int = np.int16(wf_quiet * 32767)

    beep = AudioSegment(
        wf_int.tobytes(),
        frame_rate=sps,
        sample_width=wf_int.dtype.itemsize, 
        channels=1
    )
    return beep