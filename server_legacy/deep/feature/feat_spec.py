## src
import io
import os
import shutil
import numpy as np

from typing import Tuple, List, NoReturn, Union

# django
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.core.files.uploadhandler import TemporaryFileUploadHandler, InMemoryUploadedFile

# video, audio processing
from pydub import AudioSegment
from pydub.utils import make_chunks
from moviepy.editor import VideoClip, VideoFileClip, AudioClip, AudioFileClip

# tools
from deep.feature.spec_tools import create_beep, mp3_to_wav_base, wav_to_mp3_base, load_model,preprocess_audio, detect_triggerword, chime_on_activate

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

## code
def processing_with_detection(video_file: Union[TemporaryUploadedFile, InMemoryUploadedFile]) -> Tuple[Union[TemporaryUploadedFile, InMemoryUploadedFile], int]:
    video_clip = VideoFileClip(video_file.temporary_file_path())
    video_clip.write_videofile(os.path.join(MEDIA_DIR, 'temp.mp4'))
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(os.path.join(MEDIA_DIR, 'temp.mp3'))

    # preprocessing
    filename = os.path.join(MEDIA_DIR, 'temp.mp3')
    mp3_to_wav_base(file_name=filename)

    wav_sound = AudioSegment.from_wav(file=os.path.join(MEDIA_DIR, 'temp.wav'))
    durations = len(wav_sound)

    chunk_length_ms = 10000
    chunks = make_chunks(wav_sound, chunk_length_ms)

    # model
    model = load_model(os.path.join(BASE_DIR, 'deep/feature/models/spec.h5'))

    combined_sounds = AudioSegment.empty()

    CHUNK_DIR = os.path.join(MEDIA_DIR, 'chunk')
    for i, chunk in enumerate(chunks):
        out_file = "chunk{0}.wav".format(i)
        if not os.path.exists(CHUNK_DIR):
            os.mkdir(CHUNK_DIR)

        filename = os.path.join(CHUNK_DIR, out_file)
        
        chunk.export(filename, format="wav")

        preprocess_audio(filename)

        prediction = detect_triggerword(filename, model)
        chime_on_activate(filename, prediction, 0.5, 0.5)
        
        processed_wav = AudioSegment.from_wav(file=filename)
        combined_sounds += processed_wav

    combined_sounds.export(os.path.join(MEDIA_DIR, 'temp.wav'), format="wav")
    shutil.rmtree(CHUNK_DIR)

    filename = os.path.join(MEDIA_DIR, 'temp.wav')
    wav_to_mp3_base(file_name=filename)

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

    return (video_file, durations)