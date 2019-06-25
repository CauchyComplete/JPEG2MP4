import os
import skvideo.io  # install sk-video
from PIL import Image  # install Pillow


def videoToImages(input, output):
    videogen = skvideo.io.vreader(input)
    for i, frame in enumerate(videogen):
        im = Image.fromarray(frame)
        if '%' in output:
            filename = output % i
        else:
            filename = output
        im.save(filename)

