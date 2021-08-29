import os
import numpy as np
from django.conf import settings
from api.lib.excepion import *

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model


# cho, jung, jong & total
chosung = list("ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ")  # 19개
jungsung = list("ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ") # 21개
jongsung = list("_ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ")  # 27개 + null(없는 경우) == 28개
number = list("0123456789") # 10개
alphabet = list("abcdefghijklmnopqrstuvwxyz") # 26개
special = list(" ") # 1개
total = sorted(set(chosung + jungsung + jongsung + number + alphabet + special)) # 중복 제거


def detect_swear(timeline: list, words: str) -> list:
    """타임라인과 텍스트를 바탕으로 욕설을 인식하는 모듈입니다. 

    @status `Active Review` \\
    @params `timeline=[[0, 1000], [1000, 2000] ...]` \\
    @params `words="안녕하세요"` \\
    @returns `[[0, 1000], [3000, 4000] ...]` """

    # 임시
    timeline = [[0, 1900], [1900, 2800], [2800, 4700], [4700, 5600], [5600, 6000], [6000, 6500], [6500, 6700], [6700, 6900], [6900, 7100], [7100, 7300], [7300, 7600], [7600, 8500], [8500, 8900], [8900, 9500], [9500, 10000], [10000, 10200], [10200, 10400], [10400, 10900], [10900, 12600], [12600, 12800], [12800, 13300], [13300, 14100], [14100, 14200], [14200, 15100], [15100, 16100], [16100, 17100], [17100, 17100], [17100, 22900], [22900, 24500], [24500, 26400], [26400, 39500], [39500, 47300], [47300, 47900], [47900, 48800], [48800, 49800], [49800, 50300], [50300, 50500], [50500, 50700], [50700, 50900], [50900, 51200], [51200, 51600], [51600, 52900], [52900, 53300], [53300, 57000], [57000, 57800], [57800, 58100], [58100, 58600], [58600, 58800], [58800, 58900], [59900, 60800], [60800, 61100], [61100, 62200], [62200, 62900], [62900, 63400], [63400, 64300], [64300, 64700], [64700, 65300], [65300, 65600], [65600, 66800], [66800, 67700], [67700, 68000], [68000, 68200], [68200, 68900], [68900, 70100], [70100, 70400], [70400, 70600], [70600, 71100], [71100, 71600], [71600, 74300], [74300, 74600], [74600, 74900], [74900, 75500], [75500, 77600], [77600, 78600], [78600, 78800], [78800, 79200], [79200, 79700], [79700, 79900], [79900, 80000], [80000, 80300], [80300, 80400], [80400, 84200], [84200, 84700], [84700, 85000], [85000, 85400], [85400, 85600], [85600, 98400], [98400, 102900], [102900, 103100], [103100, 103400], [103400, 104100]]
    words = ['시간', '우리가', '5,000원', '녹음해서', '모닝콜로', '들어가는데', '욕', '한번', '시원하게', '해', '주세요', '가지고', '사람들이', '모닝콜로', '쓰고', '싶대', '아', '그래', '아침', '못', '일어나', '일어나', '이', '씨발놈아', '개새끼야', '야', '이', '씨발년아', '씨발년아', '됐지', '짓는다는', '많이', '이제는', '대한민국에서', '지각하는', '사람은', '단', '한', '명도', '없어요', '너', '시간', '약속', '없지', '너', '축구', '경기', '할', '때', '경기할', '때', '마지막', '지금동', '점인데', '자', '지금', '1분', '남았습니다', '지금', '타임', '보고', '있어', '그때', '20초', '남겨', '놓고', '골드', '기도하자', '보고', '있잖아', '다', '나는', '지금', '보려고', '그래', '호루라기', '이럴', '때', '하나', '넣어', '봐', '얼굴이', '생각이', '개', '같은', '년들', '반납이', '시간을', '못', '지킨', '불쌍한']

    tk = Tokenizer(num_words=None, char_level=True, oov_token="UNK")

    # Create Char Dictionary
    char_dict = create_char_dict()

    # Tokenizer, toSequence
    tk.word_index = char_dict
    tk.word_index[tk.oov_token] = max(char_dict.values()) + 1

    texts = hangToJamo(hangul=words)
    sequences = tk.texts_to_sequences([texts])

    pad_sequence = pad_sequences(sequences, maxlen=1024, padding='post')
    data = np.array(pad_sequence[0], dtype='float32')

    try:
        model_path = os.path.join(settings.BASE_DIR, 'env/model/model.h5')
        model = load_model(model_path)

        if not model: raise LoadModelFailException()

        prediction = model.predict(data)
        swear_timeline = detect_predict(timeline, prediction)

        return swear_timeline
        
    except Exception as err:
        print(err)
        return []


def detect_predict(timeline, prediction: list) -> list:
    """예측된 수치를 바탕으로 욕설을 처리하는 모듈입니다.

    @status `Active Review` \\
    @params `None` \\
    @returns `None` """

    swears = []
    for pred in prediction:
        if round(pred[1] == 1.0 and round(pred[0]) == 0.0):
            swears.append(True)
        else:
            swears.append(False)

    # 수정이 필요함 (개 같은 -> ['개', '같은'] 문제 수정을 위해)
    swear_timeline = []
    for time, swear in zip(timeline, swears):
        if swear:
            swear_timeline.append((time[0], time[1]))

    return swear_timeline


def hangToJamo(hangul: str):
    """한글을 자소 단위(초, 중, 종성)로 분리하는 모듈입니다.

    @status `Accepted` \\
    @params `"안녕하세요"` \\
    @returns `"ㅇㅏㄴㄴㅕㅇㅎㅏ_ㅅㅔ_ㅇㅛ_"` """

    result = []
    for char in hangul:
        char_code = ord(char)

        if not 0xAC00 <= char_code <= 0xD7A3:
            result.append(char)
            continue
        
        initial_idx = int((((char_code - 0xAC00) / 28) / 21) % 19)
        midial_idx = int(((char_code - 0xAC00) / 28) % 21)
        final_idx = int((char_code - 0xAC00) % 28)

        initial = chosung[initial_idx]
        midial = jungsung[midial_idx]
        final = jongsung[final_idx]

        result.append(initial)
        result.append(midial)
        result.append(final)

    return ''.join(result)


def jamoToHang(jamo: str):
    """자소 단위(초, 중, 종성)를 한글로 결합하는 모듈입니다.

    @status `Accepted` \\
    @params `"ㅇㅏㄴㄴㅕㅇㅎㅏ_ㅅㅔ_ㅇㅛ_"` \\
    @returns `"안녕하세요"` """

    result, index = "", 0
    
    while index < len(jamo):
        try:
            initial = chosung.index(jamo[index]) * 21 * 28
            midial = jungsung.index(jamo[index + 1]) * 28
            final = jongsung.index(jamo[index + 2])

            result += chr(initial + midial + final + 0xAC00)
            index += 3
        except:
            result += jamo[index]
            index += 1

    return result
    
    
def create_char_dict():
    """자소 단위 사전을 생성하는 모듈입니다.

    @status `Accepted` \\
    @returns `{" ": 1, "0": 2, "1": 3 ... "|": 89}` """

    char_dict, i = {}, 0

    for char in total:
        if char in char_dict.keys():
            continue
        i += 1
        char_dict[char] = i

    return char_dict
