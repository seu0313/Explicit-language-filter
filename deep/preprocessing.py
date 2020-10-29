from pydub import AudioSegment
from typing import List, Tuple
import numpy as np
import random

from loadData import match_target_amplitude, graph_spectrogram, get_spectrogram

''' 
+------------------+
 Data preprocessing
+------------------+
'''
# 랜덤 시간 분할 (배경에 삽입을 위해)
def get_random_time_segment(segment_ms: int) -> Tuple[int, int]:
    segment_start = np.random.randint(low=0, high=10000-segment_ms)
    segment_end = segment_start + segment_ms - 1

    return (segment_start, segment_end)


# 오버랩 체크
def is_overlapping(segment_time: Tuple[int, int], previous_segments: List) -> bool:
    segment_start, segment_end = segment_time
    overlap = False  # overlap을 False로 초기화

    # 오버랩 체크
    for previous_start, previous_end in previous_segments:
        if segment_start <= previous_end and segment_end >= previous_start:
            overlap = True

    return overlap


# 배경 소음을 overlay 하기 위해
def insert_audio_clip(background: AudioSegment, audio_clip: AudioSegment, previous_segments: List) -> Tuple[AudioSegment, Tuple]:
    segment_ms = len(audio_clip)
    segment_time = get_random_time_segment(segment_ms)

    while is_overlapping(segment_time, previous_segments):
        segment_time = get_random_time_segment(segment_ms)
    previous_segments.append(segment_time)
    new_background = background.overlay(audio_clip, position=segment_time[0])

    return new_background, segment_time

def insert_ones(y: List, segment_end_ms: int, index: int) -> List:
    Ty = y.shape[1]
    segment_end_y = int(segment_end_ms * Ty / 10000.0)
    for i in range(segment_end_y + 1, segment_end_y + 51):
        if i < Ty:
            y[0, i] = index

    return y


# insert_audio_clip과 insert_ones를 이용하여 새로운 training 예제를 만듬
def create_training_example(background: AudioSegment, positives: List[List], negatives: List, Ty: int) -> Tuple[List, List]:
    background = background - 20  # 배경 소리 크기 줄이기 위함

    y = np.zeros((1, Ty))

    previous_segments = []
    
    # positive insertion
    for index, positive in enumerate(positives):
        number_of_positives = np.random.randint(1, 3)
        random_indices = np.random.randint(len(positive), size=number_of_positives)
        random_positives = [positive[i] for i in random_indices]

        for random_positive in random_positives:
            background, segment_time = insert_audio_clip(background, random_positive, previous_segments)
            segment_start, segment_end = segment_time
            y = insert_ones(y, segment_end, index + 1)

    # negative insertion
    number_of_negatives = np.random.randint(0, 2)
    random_indices = np.random.randint(len(negatives), size=number_of_negatives)
    random_negatives = [negatives[i] for i in random_indices]
    
    for random_negative in random_negatives:
        background, _ = insert_audio_clip(background, random_negative, previous_segments)
    background = match_target_amplitude(background, -20.0)

    file_handle = background.export("./datasets/created_file/train.wav", format="wav")  # _io.BufferedRandom

    x = get_spectrogram("./datasets/created_file/train.wav")

    # # 생성된 데이터가 잘 만들어 졌는 지 하나하나 체크하기 위함
    # sequence = time.time()
    # file_handle = background.export(f"./raw_data/created_file/train_{sequence}"+".wav", format="wav")
    # x = graph_spectrogram(f"./raw_data/created_file/train_{sequence}"+".wav")

    return x, y

''' +-----------------------------------------------+ '''

if __name__ == "__main__":
    print(get_spectrogram('./test_wav.wav'))
