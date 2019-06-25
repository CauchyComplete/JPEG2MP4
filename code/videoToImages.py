import skvideo.io  # install sk-video
from PIL import Image  # install Pillow


def videoToImages(input, output, startIndex = 1):
    # EX input = '../output1/vid.mp4'
    # EX output = '../output2/img%03d.tif' or '../output2/img.tif'
    videogen = skvideo.io.vreader(input)
    for i, frame in enumerate(videogen):
        im = Image.fromarray(frame)
        if '%' in output:
            filename = output % (i+startIndex)
        else:
            filename = output
        im.save(filename)

