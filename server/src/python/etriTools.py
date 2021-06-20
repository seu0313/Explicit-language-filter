#-*- coding:utf-8 -*-
import os
import io
import json
import base64
import urllib3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def transcribe_etri(audio_file_path: str):
    """ETRI 음성처리 모듈입니다. 오디오 파일을 받으면 음성을 인식한 후 `한국어` 텍스트 데이터를 반환합니다.

    @status `Active Review` \\
    @params `"~/src/python/temp2.wav"` \\
    @returns `Response data` """

    etri_json_file = os.path.join(BASE_DIR, "deep/etri.json")
    etri_key = json.loads(open(etri_json_file).read())

    access_key = etri_key["private_key"]
    open_api_URL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
    language_code = "korean"

    with io.open(audio_file_path, "rb") as audio_file:
        audio_contents = base64.b64decode(audio_file.read()).decode("utf8")
    
    request_json = {
        "access_key": access_key,
        "argument": {
            "language_code": language_code,
            "audio": audio_contents
        }
    }
    
    http = urllib3.PoolManager()
    response = http.request(
        "POST",
        open_api_URL,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        body=json.dumps(request_json)
    )
    
    # debug
    print("[responseCode] " + str(response.status))
    print("[responBody]")
    print(str(response.data, "utf-8"))

    return response


if __name__ == "__main__":
    audio_file_path = os.path.join(BASE_DIR, "src/python/temp2.wav")
    response = transcribe_etri(audio_file_path) 
    print(response)