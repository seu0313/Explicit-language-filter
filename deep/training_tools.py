# import
import os
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from pydub import AudioSegment
from typing import NoReturn, Tuple, List
from load_data import load_raw_audio, graph_spectrogram
from preprocessing import create_training_example

# code
class Datalize():
    def __init__(self, dtype: str, Ty: int) -> NoReturn:
        background_preprocessing(dtype=dtype)
        self.__Ty = Ty
        self.__dtype = dtype
        self.__positives, self.__negatives, self.__backgrounds = load_raw_audio(dtype=dtype)

    # Create npy datasets
    def create_data(self, data_nums: int, filename: str) -> NoReturn:
        background_len = len(self.__backgrounds)
        X_data, Y_data = [], []

        for i in tqdm(range(data_nums)):
            x, y = create_training_example(
                self.__backgrounds[i % background_len],
                self.__positives,
                self.__negatives,
                self.__Ty
            )

            X_data.append(np.array(x).T)
            Y_data.append(np.array(y).T)

        X_data = np.array(X_data)
        Y_data = np.array(Y_data)
        
        np.save(f'./datasets/npy_file/{self.__dtype}/X_{filename}', X_data)
        np.save(f'./datasets/npy_file/{self.__dtype}/Y_{filename}', Y_data)

        del(X_data)
        del(Y_data)


    def combine_npy_file(self, path: str ,file_1: str, file_2: str, filename: str) -> NoReturn:
        X1 = np.load(path + file_1)
        X2 = np.load(path + file_2)
        print("Complete. Load Files")

        X = np.vstack([X1, X2])
        print("Complete. Combine Files")

        del(X1)
        del(X2)
        print("Delete. Files in memory")
        
        np.save(path + filename, X)


# 입력 전처리 함수 (duration = 10sec, sampling_rate=44.1kHz)
def preprocess_audio(filename: str) -> NoReturn:
    # Trim or pad audio segment to 10000ms
    padding = AudioSegment.silent(duration=10000)
    segment = AudioSegment.from_wav(filename)[:10000]
    segment = padding.overlay(segment)
    # Set frame rate to 44100
    segment = segment.set_frame_rate(44100)
    # Export as wav
    segment.export(filename, format='wav')


def background_preprocessing(dtype: str):
    for filename in os.listdir(f"./datasets/{dtype}/backgrounds"):
        if filename.endswith("wav"):
            preprocess_audio(f"./datasets/{dtype}/backgrounds/" + filename)


def detect_triggerword(filename, model):
    plt.subplot(2, 1, 1)

    x = graph_spectrogram(filename)

    x = x.swapaxes(0, 1)
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x)
    plt.subplot(2, 1, 2)
    plt.plot(predictions[0, :, 1], label='시발')
    plt.plot(predictions[0, :, 2], label='개새끼')
    plt.ylabel('probability')
    plt.legend()
    plt.show()
    return predictions

def create_beep(duration):
    sps = 44100
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

def chime_on_activate(filename, predictions, threshold_on, threshold_off):
    beep_file = create_beep(duration=1000)
    audio_clip = AudioSegment.from_wav(filename)
    beep = AudioSegment.from_wav(beep_file)
    Ty = predictions.shape[1]

    consecutive_timesteps = 0

    for i in range(Ty):
        consecutive_timesteps += 1
        if predictions[0, i, 1] > threshold_on and predictions[0, i, 1] > predictions[0, i, 2] and consecutive_timesteps > 75:
            audio_clip = audio_clip.overlay(beep, position=((i / Ty) * audio_clip.duration_seconds)*1000)
            consecutive_timesteps = 0

        if predictions[0, i, 2] > threshold_off and predictions[0, i, 2] > predictions[0, i, 1] and consecutive_timesteps > 75:
            audio_clip = audio_clip.overlay(beep, position=((i / Ty) * audio_clip.duration_seconds)*1000)
            consecutive_timesteps = 0

    audio_clip.export("./datasets/created_file/beep_output.wav", format='wav')

# test
if __name__ == "__main__":
    eieo = Datalize('train', 1375)
    # eieo.create_data(data_nums=10, filename='2')

    PATH = './datasets/npy_file/train/'
    file_1 = 'X_1.npy'
    file_2 = 'X_2.npy'
    eieo.combine_npy_file(PATH, file_1, file_2, filename='X_20')

    X = np.load('./datasets/npy_file/train/X_20.npy')
    print(X.shape)