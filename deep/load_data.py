# import
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

from typing import List, Tuple
from scipy.io import wavfile
from pydub import AudioSegment

# code
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


def match_target_amplitude(sound: AudioSegment, target_dBFS: float) -> AudioSegment:
    change_in_dBFS = target_dBFS - sound.dBFS
    
    return sound.apply_gain(change_in_dBFS)


# 데이터 로드 (train/test)
def load_raw_audio(dtype: str) -> Tuple[List[List], List, List]:
    '''
        dtype: data type (train/test)
    '''

    # 욕설 목록
    positive_word = ['sib','gae']  # 추가

    positives = [] # 욕설 트리거 데이터를 담을 리스트
    negatives = []
    backgrounds = []
    
    # 욕설 분류
    for word in positive_word:
        temp = []
        for filename in os.listdir("./datasets/"+dtype.lower()+"/positives/"+word):
            if filename.endswith("wav"):
                positive = AudioSegment.from_wav("./datasets/"+dtype.lower()+"/positives/"+word+"/"+filename)
                temp.append(positive)
        positives.append(temp)

    # 비욕설 분류
    for filename in os.listdir("./datasets/"+dtype.lower()+"/negatives"):
        if filename.endswith("wav"):
            negative = AudioSegment.from_wav("./datasets/"+dtype.lower()+"/negatives/"+filename)
            negatives.append(negative)

    # 배경 (노이즈)
    for filename in os.listdir("./datasets/"+dtype.lower()+"/backgrounds"):
        if filename.endswith("wav"):
            background = AudioSegment.from_wav("./datasets/"+dtype.lower()+"/backgrounds/"+filename)
            backgrounds.append(background)

    return positives, negatives, backgrounds

# test
if __name__ == "__main__":
    print(get_spectrogram('./test_wav.wav'))