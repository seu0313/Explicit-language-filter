import numpy as np
from pydub import AudioSegment
from models import *
from preprocessing import *
from loadData import *
from training import *


if __name__ == "__main__":
    positives, negatives, backgrounds = load_raw_audio('train')

    sib, gae = positives[0], positives[1]

    print("background len: " + str(len(backgrounds[0])))
    print("on[0] len: " + str(len(sib[0])))     
    print("on[1] len: " + str(len(sib[1]))) 

    print("off[0] len: " + str(len(gae[0])))
    print("off[1] len: " + str(len(gae[1])))

    overlap1 = is_overlapping((950, 1430), [(2000, 2550), (260, 949)])
    overlap2 = is_overlapping((2305, 2950), [(824, 1532), (1900, 2305), (3424, 3656)])
    print("Overlap 1 = ", overlap1)
    print("Overlap 2 = ", overlap2)

    audio_clip, segment_time = insert_audio_clip(backgrounds[4], sib[3], [(3790, 4400)])
    audio_clip.export("./datasets/created_file/insert_test.wav", format="wav")
    print("Segment Time: ", segment_time)

    Ty = 5511
    x, y = create_training_example(backgrounds[4], positives, negatives, Ty)

    pprint(plt.plot(y[0]))
    pprint(x.shape)
    pprint(y.shape)