## src
import os
import re
import tensorflow
import numpy as np
import pandas as pd

from pydub import AudioSegment
from typing import List, Optional, Union

# keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.wrappers.scikit_learn import KerasClassifier
from keras.layers import Input, Embedding, Activation, Flatten, Dense
from keras.layers import Conv1D, MaxPooling1D, Dropout
from keras.models import Model, load_model, Sequential
from keras.utils import to_categorical
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.layers import Dense, Activation, Dropout, Input, Masking, TimeDistributed, LSTM, Conv1D
from keras.layers import GRU, Bidirectional, BatchNormalization, Reshape
from keras.optimizers import Adam, SGD, RMSprop

# dir
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# cho, jung, jong & total
chosung = list('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ')  # 19개
jungsung = list('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ') # 21개
jongsung = list('_ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')  # 27개 + null(없는 경우) == 28개
number = list('0123456789')
alphabet = list('abcdefghijklmnopqrstuvwxyz')

total = sorted(set(chosung + jungsung + jongsung + number + alphabet)) # 52개 (중복 제거)

## code
def detect_swear(timeline: List, 
                words: List) -> List:

    tk = Tokenizer(num_words=None, char_level=True, oov_token='UNK')

    char_dict = {}
    i = 0
    for char in total:
        if char in char_dict.keys():
            continue
        else:
            i = i + 1
            char_dict[char] = i
    
    tk.word_index = char_dict.copy() # deep copy
    tk.word_index[tk.oov_token] = max(char_dict.values()) + 1

    model = load_model(os.path.join(BASE_DIR, 'deep/feature/models/nlp.h5'))

    texts = hang_to_jamo(' '.join(words), return_type_number=3)
    # print(texts)
    sequences = tk.texts_to_sequences(texts)
    # print(sequences)
    data = pad_sequences(sequences, maxlen=1024, padding='post')
    data = np.array(data, dtype='float32')
    # print(data)
    
    prediction = model.predict(data) # [정상, 욕설]
    # print(prediction)

    swears = []
    for pred in prediction:
        # print( round(pred[0]),  round(pred[1]))
        if round(pred[1]) == 1.0 and round(pred[0]) == 0.0:
            swears.append(True)
        else:
            swears.append(False)

    swear_timeline = []
    for time, swear in zip(timeline, swears):
        if swear:
            swear_timeline.append((time[0], time[1]))

    return swear_timeline


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

# 한글 -> 자모
def hang_to_jamo(string: str, return_type_number: int=1) -> Union[List, str]:
    '''
        # ex 1) ㄱ == ㄱ (1) \n
        # ex 2) 가 == ㄱㅏ_ (3) \n
        # ex 2) 가. == ㄱㅏ_ (3) \n
        # ex 3) 간 == ㄱㅏㄴ (3) 이다. \n
        ----------------------- \n
        ex) '한글 자소' \n 
        return_type_number: 1 (default)\n 
        : ['ㅎ', 'ㅏ', 'ㄴ', 'ㄱ', 'ㅡ', 'ㄹ', ' ', 'ㅈ', 'ㅏ', 'ㅅ', 'ㅗ'] \n
        return_type_number: 2 \n
        : ㅎㅏㄴㄱㅡㄹ ㅈㅏㅅㅗ \n
        return_type_number: 3 \n
        : ['ㅎㅏㄴㄱㅡㄹ','ㅈㅏㅅㅗ'] \n
        return_type_number: 4 \n
        : ['한글', '자소'] \n        
    '''
    result = []

    # 정규 표현식으로 특수문자 제거
    string = re.sub(r'[^ㄱ-ㅎㅏ-ㅣ가-힣0-9a-zA-Z ]', '', string)

    for char in string:
        char_code = ord(char)

        if 0xD7A3 < char_code or char_code < 0xAC00:
            result.append(char)
            continue

        initial_idx = int((((char_code - 0xAC00) / 28) / 21) % 19)
        midial_idx = int(((char_code - 0xAC00) / 28) % 21)
        final_idx = int((char_code - 0xAC00) % 28)

        # print(initial_idx, midial_idx, final_idx)

        initial = chosung[initial_idx]
        midial = jungsung[midial_idx]
        final = jongsung[final_idx]

        result.append(initial)
        result.append(midial)
        if not final == ' ':
            result.append(final)

    if return_type_number == 1:
        return list(''.join(result))
    elif return_type_number == 2:
        return ''.join(result)
    elif return_type_number == 3:
        return ''.join(result).split(' ')
    else:
        return string.split(' ')
    

# 자모 -> 한글
def jamo_to_hang(string: Union[str, List]) -> str:
    result = ""
    index = 0

    while index < len(string):
        try:
            init = chosung.index(string[index]) * 21 * 28
            mid = jungsung.index(string[index + 1]) * 28
            fin = jongsung.index(string[index + 2])
                
            result += chr(init + mid + fin + 0xAC00)
            index += 3
            
        except:
            result += string[index]
            index += 1

    return result


# one-hot-encoding (한글만 가능 / 띄어쓰기는 [0,0,...,0]로 변환 / 특수문자, 영어 제거)
# max_len 카운트에서 특수문자, 영어는 제외됨 
# ex 1) ㄱ == ㄱ (1)
# ex 2) 가 == ㄱㅏ_ (3)
# ex 2) 가. == ㄱㅏ_ (3)
# ex 3) 간 == ㄱㅏㄴ (3) 이다.
def text_to_onehot(text: str, max_len: int = 1014, transpose: bool = True, return_type_number: int=1) -> List:
    '''
        (52, 1014) \n
        [[0. 0. 0. ... 0. 0. 0.] \n
        [0. 0. 0. ... 0. 0. 0.] \n
        [0. 0. 0. ... 0. 0. 0.] \n
        ... \n
        [0. 0. 0. ... 0. 0. 0.] \n
        [0. 0. 0. ... 0. 0. 0.] \n
        [0. 0. 0. ... 0. 0. 0.]] \n

        1) transpose == True:
            return np.array -> shape(52, 1014)
        2) transpose == False:
            return np.array -> shape(1014, 52)
    '''
    res = []

    char = hang_to_jamo(text, return_type_number=return_type_number)
    for s in char:
        temp = np.zeros((len(total)))
        if s in total:
            temp[total.index(s)]=1
        res.append(temp)
    
    # print(len(res))
    if len(res) > max_len:
        raise OverLenException(len(res))
    
    if transpose:
        result = np.array(res).T
        result = np.pad(result, ((0, 0),(0, max_len-len(res))), 'constant', constant_values=0)
    else:
        result = np.array(res)
        result = np.pad(result, ((0, max_len-len(res)),(0, 0)), 'constant', constant_values=0)

    return result


# max_len custom exception
class OverLenException(Exception):
    def __init__(self, current_len):
        self.current_len = current_len

    def __str__(self):
        return f'Current length : {self.current_len}'

# 금칙어 기반 (1차 필터)
def get_profanity():
    profanity = '''
        갈보 개십새끼 니미씹 띠발 뻐큐 시부럴 띠발놈 띠발럼
        갈보년 개쐑 니아배 띠불 뻑큐 시부리 띠발놈들 띠발럼들
        같은년 개씹 니아베 띠팔 뽁큐 시불 띠벨놈 띠벨 띠벨럼들
        같은뇬 개아들 니아비 메친넘 사까시 시브랄 띠발롬들
        개같은 개자슥 니애미 메친놈 상넘이 시팍 개같은
        개구라 개자지 니어매 미췬 상놈을 시팔
        개년 개접 니어메 미췬 상놈의 시펄
        개놈 개좆 니어미 미친넘 상놈이 심탱
        개뇬 개좌식 니에미 미친년 새갸 십라
        개대중 개허접 닝기리 미친놈 새꺄 십새
        개독 걔새 닝기미 미친새끼 새끼 십새끼
        개돼중 걔수작 대가리 미틴 새새끼 십세
        개랄 걔시끼 뎡신 미틴넘 새키 십쉐
        개보지 걔시키 도라이 미틴년 색끼 십쉐이
        개뻥 걔썌 돈놈 미틴놈 생쑈 십스키
        개뿔 게색기 돌아이 바랄년 세꺄 십쌔
        개새 게색끼 돌은놈 병자 세끼 십창
        개새기 관종 되질래 뱅마 쇼하네 십탱
        개새끼 광뇬 뒈져 뱅신 쉐기 싶알
        개새키 구녕 뒈져라 벼엉신 쉐끼 싸가지
        개색기 구라 뒈진 병쉰 쉐리 싹아지
        개색끼 구멍 뒈진다 병신 쉐에기 쌉년
        개색키 그년 뒈질 보지 쉐키 쌍넘
        개색히 그새끼 뒤질래 보지년 쉑 쌍년
        개섀끼 꼬추 등신 부랄 쉣 쌍놈
        개세 개년아 디져라 부럴 쉬발 쌍뇬
        개세끼 뀨년 디진다 불알 쉬밸 쌔끼
        개세이 뀨놈 디질래 불할 쉬벌 쌕
        개소리 냄비 딩시 붕가 쉬뻘 쌩쑈
        개쑈 놈현 따식 붙어먹 쉬펄 쌴년
        개쇳기 뇬 때놈 뷰웅 쉽알 썅
        개수작 눈깔 또라이 븅 스패킹 썅년
        개쉐 뉘미럴 똘아이 븅신 스팽 썅놈
        개쉐리 느금 똘아이 빌어먹 시끼 썅놈
        개쉐이 느금마 뙈놈 빙시 시댕 썅뇬
        개쉑 니귀미 뙤놈 빙신 시뎅 썡쇼
        개쉽 니기미 뙨넘 빠가 시랄 써벌
        개스끼 니미 뙨놈 빠구리 시발 썩을년
        개시키 니미랄 뚜쟁 빠굴 시벌 썩을놈
        개십새기 니미럴 띠바 빠큐 시부랄 쎄꺄
        갈보 개십새끼 니미씹 띠발 뻐큐 시부럴
        갈보년 개쐑 니아배 띠불 뻑큐 시부리
        같은년 개씹 니아베 띠팔 뽁큐 시불
        같은뇬 개아들 니아비 메친넘 사까시 시브랄
        개같은 개자슥 니애미 메친놈 상넘이 시팍
        개구라 개자지 니어매 미췬 상놈을 시팔
        개년 개접 니어메 미췬 상놈의 시펄
        개놈 개좆 니어미 미친넘 상놈이 심탱
        개뇬 개좌식 니에미 미친년 새갸 십라
        개대중 개허접 닝기리 미친놈 새꺄 십새
        개독 걔새 닝기미 미친새끼 새끼 십새끼
        개돼중 걔수작 대가리 미틴 새새끼 십세
        개랄 걔시끼 뎡신 미틴넘 새키 십쉐
        개보지 걔시키 도라이 미틴년 색끼 십쉐이
        개뻥 걔썌 돈놈 미틴놈 생쑈 십스키
        개뿔 게색기 돌아이 바랄년 세꺄 십쌔
        개새 게색끼 돌은놈 병자 세끼 십창
        개새기 관종 되질래 뱅마 쇼하네 십탱
        개새끼 광뇬 뒈져 뱅신 쉐기 싶알
        개새키 구녕 뒈져라 벼엉신 쉐끼 싸가지
        개색기 구라 뒈진 병쉰 쉐리 싹아지
        개색끼 구멍 뒈진다 병신 쉐에기 쌉년
        개색키 그년 뒈질 보지 쉐키 쌍넘
        개색히 그새끼 뒤질래 보지년 쉑 쌍년
        개섀끼 꼬추 등신 부랄 쉣 쌍놈
        개세 개년아 디져라 부럴 쉬발 쌍뇬
        개세끼 뀨년 디진다 불알 쉬밸 쌔끼
        개세이 뀨놈 디질래 불할 쉬벌 쌕
        개소리 냄비 딩시 붕가 쉬뻘 쌩쑈
        개쑈 놈현 따식 붙어먹 쉬펄 쌴년
        개쇳기 뇬 때놈 뷰웅 쉽알 썅 
        개수작 눈깔 또라이 븅 스패킹 썅년
        개쉐 뉘미럴 똘아이 븅신 스팽 썅놈
        개쉐리 느금 똘아이 빌어먹 시끼 썅놈
        개쉐이 느금마 뙈놈 빙시 시댕 썅뇬
        개쉑 니귀미 뙤놈 빙신 시뎅 썡쇼
        개쉽 니기미 뙨넘 빠가 시랄 써벌
        개스끼 니미 뙨놈 빠구리 시발 썩을년
        개시키 니미랄 뚜쟁 빠굴 시벌 썩을놈
        개십새기 니미럴 띠바 빠큐 시부랄 쎄꺄
        씨발 개같은 개같은년 씨발놈아 개새끼야
        년들 병신 병신새끼 병신같은 시발놈아 지랄하네
        지랄 저새끼 좆밥 조옷밥 좇밥 좁밥 호로 씨이발
        씹 새끼들아 새끼야 새키 새이키 쌔키 세키 셰키
        쉬벨롬들 쉬벨럼들 쉬발놈들 쉬벨넘들 쉬벨놈들 쉬발놈들
        쉬발넘들 쉐벨 쉬벨럼 쉬벨놈 쉬발 쉬발놈 쉬발럼
        슈발 슈발놈 슈발럼 슈발놈들 슈발넘들 슈벨 슈벨럼 슈벨놈 슈벨놈들
        슈벨넘들 슈발럼들 
        '''
        # 추후 추가.
    return list(profanity.split())

## exec
if __name__ == "__main__":
    text = '한글 자소 변환 후 원핫 인코딩 테스트 0102호 hello 입니닥'
    # text = '가가'
    # text = '''
    #     한글 자소 변환 후 원핫 인코딩 테스트 입니다 한글 자소 변환 후 원핫 인코딩 테스트 입니다 
    #     한글 자소 변환 후 원핫 인코딩 테스트 입니다 한글 자소 변환 후 원핫 인코딩 테스트 입니다 
    #     한글 자소 변환 후 원핫 인코딩 테스트 입니다 한글 자소 변환 후 원핫 인코딩 테스트 입니다 
    #     한글 자소 변환 후 원핫 인코딩 테스트 입니다 한글 자소 변환 후 원핫 인코딩 테스트 입니다 
    #     한글 자소 변환 후 원핫 인코딩 테스트 입니다 한글 자소 변환 후 원핫 인코딩 테스트 입니다 
    #     한글 자소 변환 후 원핫 인코딩 테스트 입니다 한글 자소 변환 후 원핫 인코딩 테스트 입니다 
    #     한글 자소 변환 후 원핫 인코딩 테스트 입니다 한글 자소 변환 후 원핫 인코딩 테스트 입니다 
    #     한글 자소 변환 후 원핫 인코딩 테스트 입니다 한글 자소
    # '''
    print(hang_to_jamo(text, return_type_number=2))
    print(jamo_to_hang(hang_to_jamo(text, return_type_number=2)))
    transpose = text_to_onehot(text, max_len=1014, transpose=True, return_type_number=2)
    print(transpose.shape)
    print(transpose)