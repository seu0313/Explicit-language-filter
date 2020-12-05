import os
from moviepy.editor import *
from pydub import AudioSegment
from pytube import YouTube
import time

def crawl_youtube(url: str):
    yt = YouTube(url=url)

    yt_info = {'영상 제목':yt.title, '영상 길이':yt.length, '영상 평점':yt.rating,\
        '영상 조회수':yt.views, '영상 설명':yt.description}

    for k, v in yt_info.items():
        print(f'{k} : {v}')
        # print(Pcolor.FAIL+"# 데이터를 가져오는데 실패했습니다"+Pcolor.ENDC)
        # return False

    stream = yt.streams
    # for i,v in enumerate(stream.filter(file_extension='mp4').all()):
    #     print(f'{i} : {v}')

    filename = time.strftime("%Y%m%d-%H%M%S")
    print(filename)

    stream = stream.filter(progressive=True, file_extension='mp4').order_by('resolution').first()
    stream.download('./video_file', filename=filename)

    videoClip = VideoFileClip(f"./video_file/{filename}.mp4")
    audioClip = videoClip.audio
    audioClip.write_audiofile(f"./audio_file/{filename}.mp3")
    
    sound = AudioSegment.from_mp3(file=f"./audio_file/{filename}.mp3")
    wav_filename = './audio_wav/' + filename + '.wav'
    sound.export(wav_filename, format='wav')

    # os.remove(f"./video_file/{filename}.mp4")
    # os.remove(f"./audio_file/{filename}.mp3")

if __name__ == "__main__":

    crawl_youtube(url=input('url 입력:'))
    
