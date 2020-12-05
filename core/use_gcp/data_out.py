from moviepy.editor import *
from p_color import Pcolor

def overlay():
    videoClip = VideoFileClip("./video_file/video.mp4")
    audioClip = AudioFileClip("./audio_file/result.mp3")

    # audioClip = CompositeAudioClip([videoClip.audio, audioClip])
    # videoClip.audio = audioClip

    videoClip = videoClip.set_audio(audioClip)
    videoClip.write_videofile("./processed_video.mp4", \
        codec='libx264', 
        audio_codec='aac', 
        temp_audiofile='temp-audio.m4a', 
        remove_temp=True)
    print(Pcolor.OKBLUE+'# 비속어 처리가 완료되었습니다.',Pcolor.ENDC)
    print(Pcolor.OKBLUE+'# 다음의 파일을 확인해주세요 : processed_video.mp4',Pcolor.ENDC)

if __name__ == "__main__":
    overlay()