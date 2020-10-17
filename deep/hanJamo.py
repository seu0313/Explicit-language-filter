from pprint import pprint
import re
import hgtk
import numpy as np
from hgtk.letter import decompose as decom_ltr
from hgtk.text import decompose as decom_txt

# 자모, 특수문자, 알파벳, 숫자 목록
INITIAL = ['ㄱ','ㄲ','ㄴ','ㄷ','ㄸ','ㄹ','ㅁ','ㅂ','ㅃ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']  # 19
MIDIAL = ['ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']  # 21
FINAL = ['ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']  # 27 (null+)
# SINGLE = ['ㄱ','ㄲ','ㄳ','ㄴ','ㄵ','ㄶ','ㄷ','ㄸ','ㄹ','ㄺ','ㄻ','ㄼ','ㄽ','ㄾ','ㄿ','ㅀ','ㅁ','ㅂ','ㅃ','ㅄ','ㅅ','ㅆ','ㅇ','ㅈ','ㅉ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','ㅏ','ㅐ','ㅑ','ㅒ','ㅓ','ㅔ','ㅕ','ㅖ','ㅗ','ㅘ','ㅙ','ㅚ','ㅛ','ㅜ','ㅝ','ㅞ','ㅟ','ㅠ','ㅡ','ㅢ','ㅣ']  # 51
# ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']  # 26
# NUMBER = ['0','1','2','3','4','5','6','7','8','9']  # 10
# SPECIAL = ['!','@','#','$','%','^','&','*','(',')','_','+','~','`','-','=','[',']','{','}','\\','|',"'",'"',';',':',',','.','/','<','>','?',' ','♥','♡','★','☆','\t','\n']  # 39

TOTAL = INITIAL + MIDIAL + FINAL  # 67 (초성, 중성, 종성) => 종성이 없는 경우 포함 68
# TOTAL_ALL = TOTAL + SINGLE + ALPHABET + NUMBER + SPECIAL  # 193 (초,중,종,단일의미,알파벳,숫자,특수문자) => 종성이 없는 경우 포함 194

# *** 음성으로 나온 text에서 욕설을 찾아내는 것이므로 단일어, 알파벳, 특수문자, 숫자의 구분이 필요가 없다.

# 이전 구현 내용
def hang_to_jamo(string, end_char='_'):
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

        initial = INITIAL[initial_idx]
        midial = MIDIAL[midial_idx]
        final = FINAL[final_idx]

        if final_idx == 0:
            final = end_char

        result.append(initial)
        result.append(midial)
        result.append(final)

    return ''.join(result)
    # return result

def jamo_to_hang(string):
    result = ""
    index = 0

    while index < len(string):
        try:
            init = INITIAL.index(string[index]) * 21 * 28
            mid = MIDIAL.index(string[index + 1]) * 28
            fin = FINAL.index(string[index + 2])

            result += chr(init + mid + fin + 0xAC00)
            index += 3

        except:
            result += string[index]
            index += 1

    return result

# hgtk를 활용
def cho2onehot(s):
    res = np.zeros(len(INITIAL))
    if s in INITIAL:
        res[INITIAL.index(s)]=1
    return res

def cwu2onehot(s):
    res = np.zeros(len(MIDIAL))
    if s in MIDIAL:
        res[MIDIAL.index(s)]=1
    return res

def con2onehot(s):
    res = np.zeros(len(FINAL))
    if s in FINAL:
        res[FINAL.index(s)]=1
    return res

def hang_onehot(s): # ex) s = '각'
    z = decom_ltr(s)
    res = np.zeros((len(TOTAL),3))
    res[:len(INITIAL),0] = cho2onehot(z[0])
    res[len(INITIAL):len(INITIAL)+len(MIDIAL),1] = cwu2onehot(z[1])
    res[len(INITIAL)+len(MIDIAL):len(TOTAL),2] = con2onehot(z[2])
    return res  # shape (67, 3)

if __name__ == "__main__":
    # print(0xD7A3)  # 55203
    # print(0xAC00)  # 44032
    print(cho2onehot('ㄱ'))
    print(hang_onehot('각'))