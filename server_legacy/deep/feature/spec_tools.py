## src
import os
import random
import tensorflow
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from pprint import pprint
from tqdm import tqdm
from typing import List, Tuple, NoReturn

from scipy.io import wavfile
from pydub import AudioSegment

from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.models import Model, load_model, Sequential
from keras.layers import Dense, Activation, Dropout, Input, Masking, TimeDistributed, LSTM, Conv1D
from keras.layers import GRU, Bidirectional, BatchNormalization, Reshape
from keras.optimizers import Adam, SGD, RMSprop

# dir
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

## code
def graph_spectrogram(wav_file: str) -> List[List]:
    rate, data = get_wav_info(wav_file)
    nfft = 200  # window 부분 길이
    fs = 8000  # 샘플링 주파수
    noverlap = 120  # window간의 overlap 정도
    nchannels = data.ndim
    if nchannels == 1:
        pxx, freqs, bins, im = plt.specgram(data, nfft, fs, noverlap=noverlap)
    elif nchannels == 2:
        pxx, freqs, bins, im = plt.specgram(data[:, 0], nfft, fs, noverlap=noverlap)

    return pxx


# Function to compute a spectrogram. (No Plot)
def get_spectrogram(wav_file: str) -> List[List]:
    rate, data = get_wav_info(wav_file)
    nfft = 200
    fs = 8000
    noverlap = 120
    nchannels = data.ndim
    if nchannels == 1:
        pxx, _, _ = mlab.specgram(data, nfft, fs, noverlap=noverlap)
    elif nchannels == 2:
        pxx, _, _ = mlab.specgram(data[:, 0], nfft, fs, noverlap=noverlap)

    return pxx


def get_wav_info(wav_file: str) -> Tuple[int, List[List]]:
    rate, data = wavfile.read(wav_file)

    return rate, data

def detect_triggerword(filename: str, model: Model) -> List:
    x = get_spectrogram(filename)

    x = x.swapaxes(0, 1)
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x)
    return predictions


def chime_on_activate(filename: str, predictions: List, threshold_on: float, threshold_off: float) -> NoReturn:
    chime_file = os.path.join(MEDIA_DIR, "chime.wav")
    beep_file = os.path.join(MEDIA_DIR, "beep.wav")

    audio_clip = AudioSegment.from_wav(filename)
    # chime = AudioSegment.from_wav(chime_file)  # sib
    # beep = AudioSegment.from_wav(beep_file)  # gae
    beep = create_beep(duration=1000)
    Ty = predictions.shape[1]

    consecutive_timesteps = 0

    for i in range(Ty):
        consecutive_timesteps += 1
        if predictions[0, i, 1] > threshold_on and predictions[0, i, 1] > predictions[0, i, 2] and consecutive_timesteps > 75:
            audio_clip = audio_clip.overlay(beep, position=((i / Ty) * audio_clip.duration_seconds)*1000,  gain_during_overlay=-20)
            consecutive_timesteps = 0

        if predictions[0, i, 2] > threshold_off and predictions[0, i, 2] > predictions[0, i, 1] and consecutive_timesteps > 75:
            audio_clip = audio_clip.overlay(beep, position=((i / Ty) * audio_clip.duration_seconds)*1000,  gain_during_overlay=-20)
            consecutive_timesteps = 0

    audio_clip.export(filename , format='wav')

def mp3_to_wav_base(file_name: str) -> NoReturn:
    sound = AudioSegment.from_mp3(file_name)
    # print(file_name)
    sound.export(file_name.replace('mp3', 'wav'), format='wav')

def wav_to_mp3_base(file_name: str) -> NoReturn:
    sound = AudioSegment.from_wav(file_name)
    # print(file_name)
    sound.export(file_name.replace('wav', 'mp3'), format='mp3')

def preprocess_audio(filename):
    # Trim or pad audio segment to 10000ms
    padding = AudioSegment.silent(duration=10000)
    segment = AudioSegment.from_wav(filename)[:10000]
    segment = padding.overlay(segment)
    # Set frame rate to 44100
    segment = segment.set_frame_rate(44100)
    # Export as wav
    segment.export(filename, format='wav')

def create_beep(duration):
    sps = 441000
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