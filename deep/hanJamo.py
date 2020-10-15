from pprint import pprint
import re

# 자모, 특수문자, 알파벳, 숫자 목록
INITIAL = [char for char in "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"]  # 19
MIDIAL = [char for char in "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"]  # 21
FINAL = [char for char in "_ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"]  # 28
SINGLE = [char for char in "ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"]  # 51
ALPHABET = [char for char in "abcdefghijklmnopqrstuvwxyz"]  # 26
NUMBER = [char for char in "0123456789"]  # 10
SPECIAL = [char for char in "!@#$%^&*()_+~`-=[]{}\\|'\";:,./<>? ♥♡★☆\t\n"]  # 39

TOTAL = INITIAL + MIDIAL + FINAL  # 68 (초성, 중성, 종성)
TOTAL_ALL = TOTAL + SINGLE + ALPHABET + NUMBER + SPECIAL  # 194 (초,중,종,단일의미,알파벳,숫자,특수문자)

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

if __name__ == "__main__":
    # print(0xD7A3)  # 55203
    # print(0xAC00)  # 44032

    text = input()
    jamo = hang_to_jamo(text)   # 'ㅇㅏㄴㄴㅕㅇㅎㅏ_ㅅㅔ_ㅇㅛ_ ㅈㅔ_ ㅇㅣ_ㄹㅡㅁㅇㅡㄴ'

    pprint(jamo)
    pprint(jamo_to_hang(jamo))

   