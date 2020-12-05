## src
import re
import numpy as np
from typing import List, Optional, Union

## code
# cho, jung, jong & total
chosung = list('ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ')  # 19개
jungsung = list('ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ') # 21개
jongsung = list('_ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ')  # 27개 + null(없는 경우) == 28개
number = list('0123456789')
alphabet = list('abcdefghijklmnopqrstuvwxyz')

total = sorted(set(chosung + jungsung + jongsung + number + alphabet)) # 52개 (중복 제거)


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