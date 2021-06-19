import os
from pydub import AudioSegment
from moviepy.editor import VideoClip, VideoFileClip, AudioClip, AudioFileClip

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def create_processed_video(video_file: str):
    '''
    - 영상과 처리된 비속어 음성 합성 \n
    @status `Scheduled` \\
    @params `None` \\
    @returns `None` \\
    @author `seu0313`
    @since `2.0.0`
    '''
    video_clip = VideoFileClip(video_file.temporary_file_path())
    video_clip.write_videofile(os.path.join(MEDIA_DIR, 'temp.mp4'))
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(os.path.join(MEDIA_DIR, 'temp.mp3'))

    try:
        sound = AudioSegment.from_file(file=(os.path.join(MEDIA_DIR, 'temp.mp3')), format='mp3')
        
    except Exception as err:
        print(f'오디오 load에서 문제 발생 {err}')

    durations = len(sound)

    # preprocessing
    timeline, gcp_swear_timeline, words = sample_recognize(os.path.join(MEDIA_DIR, 'temp.mp3'))

    # print(f'timeline : {timeline}\n')
    print(f'gcp_swear_timeline : {gcp_swear_timeline}\n')
    # print(f'words : {words}\n')

    # deep
    deep_swear_timeline = detect_swear(timeline=timeline, words=words)

    print(f'deep swear_timeline : {deep_swear_timeline}')

    # swear_timeline = list(set(gcp_swear_timeline) & set(deep_swear_timeline))  # 테스트
    # swear_timeline = list(set(gcp_swear_timeline) | set(deep_swear_timeline))  # 실사용
    swear_timeline = deep_swear_timeline

    print(f'swear_timeline : {swear_timeline}')

    beep = create_beep(duration=1000)
    
    i = 0
    mixed = sound.overlay(beep, position=swear_timeline[i][0], gain_during_overlay=-50)
    mixed_final = sound

    for i in range(len(swear_timeline)):
        beep = create_beep(duration=swear_timeline[i][1] - swear_timeline[i][0])
        mixed_final = mixed_final.overlay(beep, position=swear_timeline[i][0], gain_during_overlay=-50)

    mixed_final.export(os.path.join(MEDIA_DIR, 'temp.mp3'), format='mp3')

    video_clip = VideoFileClip(os.path.join(MEDIA_DIR, 'temp.mp4'))
    audio_clip = AudioFileClip(os.path.join(MEDIA_DIR, 'temp.mp3'))
    video_clip = video_clip.set_audio(audio_clip)

    video_clip.write_videofile(video_file.temporary_file_path(), \
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a', 
        remove_temp=True
    )
    video_clip.close()
    audio_clip.close()

    # os.remove(os.path.join(MEDIA_DIR, 'temp.mp3'))
    # os.remove(os.path.join(MEDIA_DIR, 'temp.mp4'))

    return (video_file, durations)

def create_beep(duration: int):
    '''
    - 비프음 생성 모듈 \n
    @status `Accepted` \\
    @params `duration(ms): int` \\
    @returns `beep audio file` \\
    @author `seu0313`
    @since `2.0.0`
    '''
    sps = 44100 # 44.1khz
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