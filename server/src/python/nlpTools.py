import os
import numpy as np

# keras
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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def detect_swear(timeline: list, words: str) -> list:
    """타임라인과 텍스트를 바탕으로 욕설을 인식하는 모듈입니다. 

    @status `Scheduled` \\
    @params `timeline=[[0, 1000], [1000, 2000] ...]` \\
    @params `words="안녕하세요"` \\
    @returns `[[0, 1000], [3000, 4000] ...]` """

    tk = Tokenizer(num_words=None, char_level=True, oov_token="UNK")

    # Create Char Dictionary
    char_dict = create_char_dict()

    # Tokenizer, toSequence
    tk.word_index = char_dict
    tk.word_index[tk.oov_token] = max(char_dict.values()) + 1

    texts = hangToJamo(hangul=words)
    sequences = tk.texts_to_sequences([texts])

    pad_sequence = pad_sequences(sequences, maxlen=1024, padding='post')
    data = np.array(pad_sequence[0], dtype='float32') # [61. 69. 42. ...  0.  0.  0.]

    try:
        model = load_model("./model/model.h5")
        prediction = model.predict(data)
        swear_timeline = detect_predict(prediction)
        return swear_timeline
    except:
        print("Can't load model. Give me model!")
        return []


def detect_predict(prediction: list) -> list:
    """예측된 수치를 바탕으로 욕설을 처리하는 모듈입니다.

    @status `Scheduled` \\
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


# if __name__ == "__main__":
#     print(create_char_dict())