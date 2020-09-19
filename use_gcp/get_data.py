import os
from moviepy.editor import *
from pytube import *
from p_color import Pcolor

def is_path():
    VIDEO_PATH = './video_file'
    AUDIO_PATH = './audio_file'
    
    PATHS = [VIDEO_PATH, AUDIO_PATH]
    for PATH in PATHS:
        if not os.path.exists(PATH):
            os.mkdir(PATH)

def get_data(urls='https://www.youtube.com/watch?v=dd9gN8DU8QE'):
    is_path()
    try:
        yt = YouTube(urls)
        yt_info = {'영상 제목':yt.title, '영상 길이':yt.length, '영상 평점':yt.rating,\
            '영상 조회수':yt.views, '영상 설명':yt.description}

        print(Pcolor.OKGREEN+"데이터를 성공적으로 가져왔습니다\n"+Pcolor.ENDC)
        for k, v in yt_info.items():
            print(f'{k} : {v}')
    except:
        print(Pcolor.FAIL+"# 데이터를 가져오는데 실패했습니다"+Pcolor.ENDC)
        return False

    stream = yt.streams
    # for i,v in enumerate(stream.filter(file_extension='mp4').all()):
    #     print(f'{i} : {v}')

    stream = stream.filter(progressive=True, file_extension='mp4').order_by('resolution').first()
    stream.download('./video_file', filename='video')

def video_to_audio():
    try:
        videoClip = VideoFileClip("./video_file/video.mp4")
        audioClip = videoClip.audio
        audioClip.write_audiofile("./audio_file/audio.mp3")
    except OSError:
        print(Pcolor.WARNING+'# 파일명: ./video_file/video.mp4 을 찾을 수 없습니다.'+Pcolor.ENDC)

if __name__ == "__main__":
    get_data('')
    video_to_audio()




    


    





