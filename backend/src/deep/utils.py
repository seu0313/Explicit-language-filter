import io
import os
import json
import time
import datetime
import pydub
from datetime import timedelta
from pydub import AudioSegment
# from google.cloud import speech_v1p1beta1
# from google.cloud.speech_v1p1beta1 import enums
from google.cloud import speech_v1
# from google.cloud.speech_v1 import enums
# from google.auth.exceptions import DefaultCredentialsError
import numpy as np

from moviepy.editor import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

def credentials():
    SECRETS_DIR = os.path.join(BASE_DIR, 'secrets/Abusive-Language-detection-30258f70228e.json')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = SECRETS_DIR

def get_profanity():
    profanity = '''
        갈보 개십새끼 니미씹 띠발 뻐큐 시부럴 띠발놈 띠발럼
        갈보년 개쐑 니아배 띠불 뻑큐 시부리 띠발놈들 띠발럼들
        같은년 개씹 니아베 띠팔 뽁큐 시불 띠벨놈 띠벨 띠벨럼들
        같은뇬 개아들 니아비 메친넘 사까시 시브랄 띠발롬들
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

def create_beep(duration):
    sps = 44100
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

# gcp 처리
def sample_recognize(local_file_path):
    credentials()

    client = speech_v1.SpeechClient()

    language_code = "ko-KR"
    sample_rate_hertz = 44100

    encoding = speech_v1.enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
        "enable_word_time_offsets": True,
        "use_enhanced": True,
    }
    
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    
    audio = {"content": content}

    response = client.recognize(config=config,audio=audio)
    
    timeline, swear_timeline, words = [], [], []

    profanities = get_profanity()

    for result in response.results:
        alternative = result.alternatives[0]
        print(u"\nTranscript: {}".format(alternative.transcript))
        
        for word in alternative.words:
            timeline.append([
                int(word.start_time.seconds * 1000 + word.start_time.microseconds * (10**-9)),
                int(word.end_time.seconds * 1000 + word.end_time.microseconds * (10**-9))
            ])
            
            words.append(word.word)

            # 비속어 처리
            for profanity in profanities :
                if profanity in word.word:
                    swear_timeline.append([
                        int(word.start_time.seconds * 1000 + word.start_time.microseconds * (10**-9)),
                        int(word.end_time.seconds * 1000 + word.end_time.microseconds * (10**-9))
                    ])
                
    return timeline, swear_timeline, words

def video_processing(file_path):
    print(os.path.join(MEDIA_DIR, file_path.name))
    MEDIAPATH = os.path.join(MEDIA_DIR, file_path.name)
    AUDIOPATH = os.path.join(MEDIA_DIR, file_path.name.replace('.mp4','.mp3'))

    # time.sleep(5)

    print(AUDIOPATH)

    videoClip = VideoFileClip(MEDIAPATH)
    print(f'비디오 파일 {videoClip}')
    audioClip = videoClip.audio
    print(f'오디오 파일 {audioClip}')
    audioClip.write_audiofile(AUDIOPATH)
    
    # preprocessing
    timeline, swear_timeline, words = sample_recognize(AUDIOPATH)
    
    print(f'timeline : {timeline}')
    print(f'swear_timeline : {swear_timeline}')
    print(f'words : {words}')
    
    print(f'오디오 확인: {AUDIOPATH}')
    sound = AudioSegment.from_file(AUDIOPATH, format='mp3')

    print(len(sound))

    beep = create_beep(duration=1000)
    
    i = 0
    mixed = sound.overlay(beep, position=swear_timeline[i][0], gain_during_overlay=-20)
    mixed

    mixed_final = sound

    for i in range(len(swear_timeline)):
        beep = create_beep(duration=swear_timeline[i][1] - swear_timeline[i][0])
        mixed_final = mixed_final.overlay(beep, position=swear_timeline[i][0], gain_during_overlay=-20)
        
    mixed_final

    mixed_final.export(AUDIOPATH, format='mp3')

    videoClip = VideoFileClip(MEDIAPATH)
    audioClip = AudioFileClip(AUDIOPATH)

    # audioClip = CompositeAudioClip([videoClip.audio, audioClip])
    # videoClip.audio = audioClip

    videoClip = videoClip.set_audio(audioClip)
    videoClip.write_videofile(MEDIAPATH, \
        codec='libx264', 
        audio_codec='aac', 
        temp_audiofile='temp-audio.m4a', 
        remove_temp=True)
    # print(Pcolor.OKBLUE+'# 비속어 처리가 완료되었습니다.',Pcolor.ENDC)
    # print(Pcolor.OKBLUE+'# 다음의 파일을 확인해주세요 : processed_video.mp4',Pcolor.ENDC)

    return file_path

