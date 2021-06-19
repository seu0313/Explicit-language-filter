import os
import io
import json
from google.cloud import speech
from google.auth.exceptions import DefaultCredentialsError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def transcribe_local(speech_file: str):
    '''
    - 구글 클라우드 플랫폼 STT 짧은 음성\n
    @status `Active Review` \\
    @params `"~/src/python/temp2.wav"` \\
    @returns `Response data` \\
    @author `seu0313`
    @since `2.0.0`
    '''
    try:
        register_gcp_credentials()

        # STT
        client = speech.SpeechClient()

        with io.open(speech_file, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
            sample_rate_hertz=44100,
            language_code="ko-KR",
            enable_word_time_offsets= True,
            use_enhanced= True
        )

        response = client.recognize(config=config, audio=audio)
        return response

    except Exception as Error:
        print(Error)

def transcribe_gcs(gcs_uri: str):
    '''
    - 구글 클라우드 플랫폼 STT 긴 음성 \n
    @status `Active Review` \\
    @params `"gs://버킷이름/파일명"` \\
    @returns `Response data` \\
    @author `seu0313`
    @since `2.0.0`
    '''
    try:
        register_gcp_credentials()
        
        # STT
        client = speech.SpeechClient()

        audio = speech.RecognitionAudio(uri=gcs_uri)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="ko-KR",
            enable_word_time_offsets= True,
            use_enhanced= True
        )

        operation = client.long_running_recognize(config=config, audio=audio)
        response = operation.result()
        return response

    except Exception as Error:
        print(Error)

def google_process_response(response):
    '''
    - 구글 STT Response 처리 로직 \n
    @status `Scheduled` \\
    @params `Response data` \\
    @returns `None` \\
    @author `seu0313`
    @since `2.0.0`
    '''
    imeline, swear_timeline, words = [], [], []
    
    try:
        for result in response.results:
            alternative = result.alternatives[0]
            
            for word in alternative.words:
                timeline.append([
                    int(word.start_time.seconds * 1000 + word.start_time.nanos * (10**-6)),
                    int(word.end_time.seconds * 1000 + word.end_time.nanos * (10**-6))
                ])
                
                words.append(word.word)

                # 비속어 처리
                for profanity in profanities :
                    if profanity in word.word:
                        swear_timeline.append((
                            int(word.start_time.seconds * 1000 + word.start_time.nanos * (10**-6)),
                            int(word.end_time.seconds * 1000 + word.end_time.nanos * (10**-6))
                        ))
    except Exception as err:
        print(err)

    return timeline, swear_timeline, words
    
def register_gcp_credentials():
    '''
    - 구글 클라우드 인증 파일 환경 변수에 등록 \n
    @status `Accepted` \\
    @author `seu0313`
    @since `2.0.0`
    '''
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(BASE_DIR, 'google.json')

if __name__ == "__main__":
    pass
    # response = transcribe_local(os.path.join(BASE_DIR, "src/python/temp2.wav"))
    # print(response)
    # with open("response1.txt", "w") as script:
    #     for result in response.results:
    #         script.write(u'{}'.format(result.alternatives[0].transcript)+"\n")

    # response = transcribe_gcs("gs://버킷이름/파일명")
    # print(response)
    # with open("response2.txt", "w") as script:
    #     for result in response.results:
    #         script.write(u'{}'.format(result.alternatives[0].transcript)+"\n")