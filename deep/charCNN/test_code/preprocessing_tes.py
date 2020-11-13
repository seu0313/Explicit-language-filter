import numpy as np
import pandas as pd
from pprint import pprint

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# 구현해야할 기능
# 문장 -> 자모단위로 양자화(quantization)  # len = 194
class Jamo:
    def __init__(self):
        self.result = []

        # 문자 단위 모음 (194개) : private
        self.__init_char = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"  # 19
        self.__midial_char = "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"  # 21
        self.__final_char = " ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"  # 28
        self.__single_char = 'ㄱㄲㄳㄴㄵㄶㄷㄸㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅃㅄㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'  # 51
        self.__alphabet_char = 'abcdefghijklmnopqrstuvwxyz'  # 26
        self.__number_char = '0123456789'  # 10
        self.__special_char = "!@#$%^&*()_+~`-=[]{}\\|'\";:,./<>? ♥♡★☆\t\n"  # 39
        self.__total_char = self.__init_char + self.__midial_char + self.__final_char + self.__single_char + self.__alphabet_char + self.__number_char + self.__special_char 

    def tokenize(self):
        char_dict = {}
        for i, char in enumerate(self.__total_char):
            char_dict[char] = i

        tk = Tokenizer(num_words=None, char_level=True, oov_token='UNK')
        tk.word_index = char_dict
        tk.word_index[tk.oov_token] = max(char_dict.values()) + 1
        # tk.word_index[max(char_dict.keys()) + 1] = tk.oov_token
        pprint(char_dict)

        return tk

    def separate(self, string):
        """
            초성 중성 종성 분리 하기
            유니코드 한글은 0xAC00 으로부터
            초성 19개, 중성21개, 종성28개로 이루어지고
            이들을 조합한 11,172개의 문자를 갖는다.
            한글코드의 값 = ((초성 * 21) + 중성) * 28 + 종성 + 0xAC00
            (0xAC00은 'ㄱ'의 코드값)
            따라서 다음과 같은 계산 식이 구해진다.
            유니코드 한글 문자 코드 값이 X일 때,
            초성 = ((X - 0xAC00) / 28) / 21
            중성 = ((X - 0xAC00) / 28) % 21
            종성 = (X - 0xAC00) % 28
            이 때 초성, 중성, 종성의 값은 각 소리 글자의 코드값이 아니라
            이들이 각각 몇 번째 문자인가를 나타내기 때문에 다음과 같이 다시 처리한다.
            초성문자코드 = 초성 + 0x1100 //('ㄱ')
            중성문자코드 = 중성 + 0x1161 // ('ㅏ')
            종성문자코드 = 종성 + 0x11A8 - 1 // (종성이 없는 경우가 있으므로 1을 뺌)
        """

        for char in string:

            character_code = ord(char)

            # Do not process unless it is in Hangul syllables range.
            if 0xD7A3 < character_code or character_code < 0xAC00:
                continue

            init_index = (character_code - 0xAC00) // 21 // 28
            midial_index = (character_code - 0xAC00 - (init_index * 21 * 28)) // 28
            final_index = character_code - 0xAC00 - (init_index * 21 * 28) - (midial_index * 28)

            self.result.append(self.__init_list[init_index])
            self.result.append(self.__midial_list[midial_index])
            self.result.append(self.__final_list[final_index])
            
        return self.result

if __name__ == "__main__":
    jamo = Jamo()
    tk = jamo.tokenize()
    train_sequences = tk.texts_to_sequences('ㅇㅏㄴㄴㅕㅇ')
    pprint(train_sequences)

    # train_data = np.array(pad_sequences(train_sequences, maxlen=512, padding='post'), dtype='float32')

    # pprint(train_data)