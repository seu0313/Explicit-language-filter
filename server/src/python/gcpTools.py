import os
import io
import json
from google.cloud import speech
from google.auth.exceptions import DefaultCredentialsError

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def transcribe_local(speech_file: str):
    """구글 클라우드 플랫폼 SpeechToText를 사용하여 `짧은 오디오 (1분 미만)`에서 `한국어` 텍스트를 추출합니다.

    @status `Active Review` \\
    @params `"~/src/python/temp2.wav"` \\
    @returns `Response data` """

    try:
        register_gcp_credentials()

        # STT
        client = speech.SpeechClient()

        with io.open(speech_file, "rb") as audio_file:
            content = audio_file.read()

        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="ko-KR",
            enable_word_time_offsets= True,
            use_enhanced= True
        )

        response = client.recognize(config=config, audio=audio)

        return response

    except DefaultCredentialsError:
        print("Credential error")
        return None

    except Exception as Error:
        print(Error)
        return None


def transcribe_gcs(gcs_uri: str):
    """구글 클라우드 플랫폼 SpeechToText를 사용하여 `긴 오디오`에서 `한국어` 텍스트를 추출합니다.

    @status `Active Review` \\
    @params `"gs://버킷이름/파일명"` \\
    @returns `Response data` """

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

    except DefaultCredentialsError:
        print("Credential error")
        return None

    except Exception as Error:
        print(Error)
        return None


def process_google_response(response):
    """구글 클라우드 플랫폼 SpeechToText를 사용하여 추출한 `한국어` 텍스트를 처리합니다.

    @status `Scheduled` \\
    @params `Response data` \\
    @returns `None` """

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
        return None

    return timeline, swear_timeline, words
    

def register_gcp_credentials():
    """구글 클라우드 인증 파일(json)을 사용하여 환경 변수에 등록합니다.
    
    @status `Accepted` """
    
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.join(BASE_DIR, 'deep/google.json')


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