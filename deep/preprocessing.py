import numpy as np
import pandas as pd
from pprint import pprint
from hanJamo import hang_onehot, hang_to_jamo, TOTAL

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from keras.layers import Input, Embedding

# 구
def text_to_seq(texts):
    # text to lower
    texts = [s.lower() for s in texts]

    # Token initialize
    tk = Tokenizer(num_words=None, char_level=True, oov_token='UNK')
    
    # Fitting
    tk.fit_on_texts(texts)

    # -- classify char
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+~`-=[]{}\\|'\";:,./<>? ♥♡★☆\t\n"
    # alphabet = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+~`-=[]{}\\|'\";:,./<>? ♥♡★☆\t\n"
    # korean = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ_ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"

    # alphabet = korean

    # 자모 dictionary
    char_dict = {}
    for i, char in enumerate(alphabet):
        char_dict[char] = i + 1

    # OOV 토큰 추가
    tk.word_index = char_dict
    tk.word_index[tk.oov_token] = max(char_dict.values()) + 1

    # 시퀀스화
    sequences = tk.texts_to_sequences(texts)
    print(texts[0])
    print(sequences[0])

    # 패팅 과정 : 글자 수 차이 상쇄
    # 최대 길이 : 1014, 후위 패딩
    data = pad_sequences(sequences, maxlen=1014, padding='post')

    data = np.array(data)
    return data, tk

def sequence_to_embedding(texts, input_size, embedding_size):
    data, tk = text_to_seq(texts)

    vocab_size = len(tk.word_index)

    embedding_weights = []
    embedding_weights.append(np.zeros(vocab_size))

    for _, i in tk.word_index.items():
        onehot = np.zeros(vocab_size)
        onehot[i-1] = 1
        embedding_weights.append(onehot)

    embedding_weights = np.array(embedding_weights)
    
    pprint(embedding_weights)

    # Embedding 계층 초기화
    embedding_layer = Embedding(vocab_size+1, 
                                embedding_size, 
                                input_length=input_size,
                                weights=[embedding_weights])

    return embedding_layer

# 신
def hang_to_embedding(texts):
    vocab_size = len(TOTAL)

    embedding_weights = []
    # for text in texts:
    #     embedding_weights.append(hang_onehot(text))
    
    pprint(hang_onehot(texts))
    # embedding_layer = Embedding(vocab_size+1, 
    #                             embedding_size, 
    #                             input_length=input_size,
    #                             weights=[embedding_weights])


if __name__ == "__main__":
    # texts = ["wall st. bears claw back into the black (reuters)reuters - short-sellers, wall street's dwindling\\band of ultra-cynics, are seeing green again.",
    #    'carlyle looks toward commercial aerospace (reuters)reuters - private investment firm carlyle group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.',
    #    "oil and economy cloud stocks' outlook (reuters)reuters - soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums."]

    # texts = ['안녕하세요','반갑습니다','안녕히가세요']
    texts = '안'

    # input_size = 1014
    # embedding_size = 76

    # # test
    # embedding_size = 20

    # embedding_layer = sequence_to_embedding(texts, input_size, embedding_size)

    # embedding_layer = hang_to_embedding(texts)
