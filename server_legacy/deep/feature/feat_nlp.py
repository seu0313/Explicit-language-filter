## src
import os
import io

from pydub import AudioSegment
from moviepy.editor import VideoClip, VideoFileClip, AudioClip, AudioFileClip
from typing import Tuple, List, NoReturn, Any, Union

# django
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.core.files.uploadhandler import TemporaryFileUploadHandler, InMemoryUploadedFile

# google
from google.cloud import speech_v1
from google.auth.exceptions import DefaultCredentialsError

# tools
from deep.feature.nlp_tools import create_beep, get_profanity, detect_swear

# dir
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
SECRET_DIR = os.path.join(BASE_DIR, 'secrets')

## code

# google speech-to-text api
def sample_recognize(local_file_path: str) -> Tuple[List, List, List]:
    try:
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(SECRET_DIR, 'google.json')
    except DefaultCredentialsError as err:
        print(err)

    client = speech_v1.SpeechClient()

    language_code = "ko-KR"
    sample_rate_hertz = 44100

    encoding = speech_v1.enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
        "enable_word_time_offsets": True,
        "use_enhanced": True,
    }

    with io.open(local_file_path, "rb") as f:
        content = f.read()

    audio = {"content": content}
    response = client.recognize(config=config, audio=audio)

    timeline, swear_timeline, words = [], [], []

    profanities = get_profanity() # 1차 비속어 필터

    try:
        for result in response.results:
            alternative = result.alternatives[0]
            # print(u"\nTranscript: {}".format(alternative.transcript))
            
            for word in alternative.words:
                timeline.append([
                    int(word.start_time.seconds * 1000 + word.start_time.nanos * (10**-6)),
                    int(word.end_time.seconds * 1000 + word.end_time.nanos * (10**-6))
                ])
                
                words.append(word.word)

                # 비속어 처리
                for profanity in profanities :
                    if profanity in word.word:
                        swear_timeline.append((
                            int(word.start_time.seconds * 1000 + word.start_time.nanos * (10**-6)),
                            int(word.end_time.seconds * 1000 + word.end_time.nanos * (10**-6))
                        ))
    except Exception as err:
        print(err)
        print('google api error')

    return timeline, swear_timeline, words

# nlp 처리
def processing_with_gcp(video_file: Union[TemporaryUploadedFile, InMemoryUploadedFile]) -> Tuple[Union[TemporaryUploadedFile, InMemoryUploadedFile], int]:
    
    video_clip = VideoFileClip(video_file.temporary_file_path())
    video_clip.write_videofile(os.path.join(MEDIA_DIR, 'temp.mp4'))
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(os.path.join(MEDIA_DIR, 'temp.mp3'))

    try:
        sound = AudioSegment.from_file(file=(os.path.join(MEDIA_DIR, 'temp.mp3')), format='mp3')
        
    except Exception as err:
        print(f'오디오 load에서 문제 발생 {err}')

    durations = len(sound)

    # preprocessing
    timeline, gcp_swear_timeline, words = sample_recognize(os.path.join(MEDIA_DIR, 'temp.mp3'))

    # print(f'timeline : {timeline}\n')
    print(f'gcp_swear_timeline : {gcp_swear_timeline}\n')
    # print(f'words : {words}\n')

    # deep
    deep_swear_timeline = detect_swear(timeline=timeline, words=words)

    print(f'deep swear_timeline : {deep_swear_timeline}')

    # swear_timeline = list(set(gcp_swear_timeline) & set(deep_swear_timeline))  # 테스트
    # swear_timeline = list(set(gcp_swear_timeline) | set(deep_swear_timeline))  # 실사용
    swear_timeline = deep_swear_timeline

    print(f'swear_timeline : {swear_timeline}')

    beep = create_beep(duration=1000)
    
    i = 0
    mixed = sound.overlay(beep, position=swear_timeline[i][0], gain_during_overlay=-50)
    mixed_final = sound

    for i in range(len(swear_timeline)):
        beep = create_beep(duration=swear_timeline[i][1] - swear_timeline[i][0])
        mixed_final = mixed_final.overlay(beep, position=swear_timeline[i][0], gain_during_overlay=-50)

    mixed_final.export(os.path.join(MEDIA_DIR, 'temp.mp3'), format='mp3')

    video_clip = VideoFileClip(os.path.join(MEDIA_DIR, 'temp.mp4'))
    audio_clip = AudioFileClip(os.path.join(MEDIA_DIR, 'temp.mp3'))
    video_clip = video_clip.set_audio(audio_clip)

    video_clip.write_videofile(video_file.temporary_file_path(), \
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a', 
        remove_temp=True
    )
    video_clip.close()
    audio_clip.close()

    # os.remove(os.path.join(MEDIA_DIR, 'temp.mp3'))
    # os.remove(os.path.join(MEDIA_DIR, 'temp.mp4'))

    return (video_file, durations)


## exec