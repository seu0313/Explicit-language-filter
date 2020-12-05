# from google.cloud import speech_v1p1beta1
# from google.cloud.speech_v1p1beta1 import enums
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
from pydub import AudioSegment
import numpy as np
import io
from profanity import get_profanity

profanities = get_profanity()

def sample_recognize(local_file_path):
    client = speech_v1.SpeechClient()

    language_code = "ko-KR"
    sample_rate_hertz = 44100

    encoding = enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED
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

    response = client.recognize(config, audio)
    
    timeline, swear_timeline, words = [], [], []

    for result in response.results:
        alternative = result.alternatives[0]
        print(u"\nTranscript: {}".format(alternative.transcript))
        
        for word in alternative.words:
            timeline.append([
                int(word.start_time.seconds * 1000 + word.start_time.nanos * (10**-6)),
                int(word.end_time.seconds * 1000 + word.end_time.nanos * (10**-6))
            ])
            
            words.append(word.word)

            for profanity in profanities :
                if profanity in word.word:
                    swear_timeline.append([
                        int(word.start_time.seconds * 1000 + word.start_time.nanos * (10**-6)),
                        int(word.end_time.seconds * 1000 + word.end_time.nanos * (10**-6))
                    ])
                
    return timeline, swear_timeline, words

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