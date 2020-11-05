import os
from typing import NoReturn
from pydub import AudioSegment

def mp3_to_wav(folder_path: str) -> NoReturn:

    for filename in os.listdir(folder_path):
        if filename.endswith("mp3"):
            sound = AudioSegment.from_mp3("./source_mp3/" + filename)
            sound.export('./convert_wav/' + filename.replace('mp3','wav'), format='wav')


if __name__ == "__main__":
    mp3_to_wav("./source_mp3")
