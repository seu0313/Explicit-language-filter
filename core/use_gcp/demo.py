import os
from get_data import *
from process_gcp import *
from data_out import *
from p_color import Pcolor
from credentials import credentials
from google.auth.exceptions import DefaultCredentialsError

if __name__ == "__main__":
    try:
        credentials()

        # get_data
        print(Pcolor.HEADER+'Youtube URL을 입력하세요 : ',end=''+Pcolor.ENDC)
        url = input()

        get_data(url)
        video_to_audio()

        # preprocessing
        timeline, swear_timeline, words = sample_recognize('audio_file/audio.mp3')

        print(timeline)
        print(words)
        print(swear_timeline)

        sound = AudioSegment.from_file('audio_file/audio.mp3', format='mp3')

        print(len(sound))
        sound

        beep = create_beep(duration=1000)
        beep
        
        i = 0
        mixed = sound.overlay(beep, position=swear_timeline[i][0], gain_during_overlay=-20)
        mixed

        mixed_final = sound

        for i in range(len(swear_timeline)):
            beep = create_beep(duration=swear_timeline[i][1] - swear_timeline[i][0])
            mixed_final = mixed_final.overlay(beep, position=swear_timeline[i][0], gain_during_overlay=-20)
            
        mixed_final

        mixed_final.export('audio_file/result.mp3', format='mp3')

        overlay()
    except DefaultCredentialsError:
        print(Pcolor.FAIL+"Google API Credential 문제입니다. https://cloud.google.com/docs/authentication/getting-started 을 확인해주세요.")
        

    

