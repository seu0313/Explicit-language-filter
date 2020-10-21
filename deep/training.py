import os
from typing import Tuple, List
import matplotlib.pyplot as plt
from pydub import AudioSegment
from tqdm import tqdm
import numpy as np

# 수정이 필요함
'''
+-----------------------------------------------+
    Create new train-datasets with labeling
+-----------------------------------------------+
'''

class Datalize():
    def __init__(self):
        background_preprocessing()
        self.__Ty = 1375
        self.__ons, self.__offs, self.__negatives, self.__backgrounds = load_raw_audio()
        self.__ons_split, self.__offs_split, self.__negatives_split = load_raw_audio_split()

    def Create_train(self, data_nums, name):
        X_data, Y_data = self.__Create_Data(data_nums, 'train')

        np.save(f"./XY_file/train/X_{name}", X_data)
        np.save(f"./XY_file/train/Y_{name}", Y_data)

    def Create_valid(self, data_nums, name):
        X_data, Y_data = self.__Create_Data(data_nums, 'valid')
        np.save(f"./XY_file/valid/X_val_{name}", X_data)
        np.save(f"./XY_file/valid/Y_val_{name}", Y_data)

    def Create_test(self, data_nums, name):
        X_data, Y_data = self.__Create_Data(data_nums, 'test')

        np.save(f"./XY_file/test/X_dev_{name}", X_data)
        np.save(f"./XY_file/test/Y_dev_{name}", Y_data)

    def Combine(self, file_path, file_1, file_2, file_name):
        X1 = np.load(file_path + file_1)
        X2 = np.load(file_path + file_2)
        print("Load")

        X = np.vstack([X1, X2])
        print("Combine")

        del(X1)
        del(X2)
        print("Delete")
        np.save(file_path + file_name, X)

    # Create data
    def __Create_Data(self, data_nums, sort):
        X_data = []
        Y_data = []
        for i in tqdm(range(data_nums)):
            b_len = len(self.__backgrounds)
            if sort.upper() == 'TRAIN':
                x, y = create_training_example(self.__backgrounds[i % b_len], self.__ons, self.__offs, self.__negatives, self.__Ty)
            else:
                x, y = create_training_example(self.__backgrounds[i % b_len], self.__ons_split, self.__offs_split, self.__negatives_split, self.__Ty)
            X_data.append(np.array(x).T)
            Y_data.append(np.array(y).T)

        X_data = np.array(X_data)
        Y_data = np.array(Y_data)

        return X_data, Y_data


# 입력 전처리 함수 (duration = 10sec, sampling_rate=44.1kHz)
def preprocess_audio(filename):
    # Trim or pad audio segment to 10000ms
    padding = AudioSegment.silent(duration=10000)
    segment = AudioSegment.from_wav(filename)[:10000]
    segment = padding.overlay(segment)
    # Set frame rate to 44100
    segment = segment.set_frame_rate(44100)
    # Export as wav
    segment.export(filename, format='wav')


def background_preprocessing():
    for filename in os.listdir("./raw_data/backgrounds"):
        if filename.endswith("wav"):
            preprocess_audio("./raw_data/backgrounds/" + filename)


def detect_triggerword(filename, model):
    plt.subplot(2, 1, 1)

    x = graph_spectrogram(filename)

    x = x.swapaxes(0, 1)
    x = np.expand_dims(x, axis=0)
    predictions = model.predict(x)
    plt.subplot(2, 1, 2)
    plt.plot(predictions[0, :, 1], label='on')
    plt.plot(predictions[0, :, 2], label='off')
    plt.ylabel('probability')
    plt.legend()
    plt.show()
    return predictions


def chime_on_activate(filename, predictions, threshold_on, threshold_off):
    chime_file = "./audio/chime.wav"
    beep_file = "./audio/beep.wav"
    audio_clip = AudioSegment.from_wav(filename)
    chime = AudioSegment.from_wav(chime_file)  # on
    beep = AudioSegment.from_wav(beep_file)  # off
    Ty = predictions.shape[1]

    consecutive_timesteps = 0

    for i in range(Ty):
        consecutive_timesteps += 1
        if predictions[0, i, 1] > threshold_on and predictions[0, i, 1] > predictions[0, i, 2] and consecutive_timesteps > 75:
            audio_clip = audio_clip.overlay(chime, position=((i / Ty) * audio_clip.duration_seconds)*1000)
            consecutive_timesteps = 0

        if predictions[0, i, 2] > threshold_off and predictions[0, i, 2] > predictions[0, i, 1] and consecutive_timesteps > 75:
            audio_clip = audio_clip.overlay(beep, position=((i / Ty) * audio_clip.duration_seconds)*1000)
            consecutive_timesteps = 0

    audio_clip.export("chime_output.wav", format='wav')


# if __name__ == "__main__":
#     # background_preprocessing()
#     # ons, negatives, backgrounds = load_raw_audio()
#     # for i in range(len(backgrounds)):
#     #     print(f"{i} is {len(backgrounds[i])}")

#     OLO = Datalize()
#     OLO.Create_train(10, '1')
#     OLO.Create_train(10, '2')

#     PATH = './XY_file/train/'
#     file_1 = 'X_1.npy'
#     file_2 = 'X_2.npy'
#     OLO.Combine(PATH, file_1, file_2, file_name='X_20')

#     X = np.load('./XY_file/train/X_20.npy')
#     print(X.shape)