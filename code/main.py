# Kwon Myung Joon
# June 25, 2019

from imagesToVideo import imagesToVideo
from videoToImages import videoToImages
from imageToVideoToImage import imageToVideoToImage
from removeAllFilesIn import removeAllFilesIn

# Disclaimer : Every path must not contain blank(' ') character.
# Every path must use '/' not '\'.
# If 'temp' directory already exists, please rename it or modify code.
# Every directory you mentioned must exist before running the code.

def main():
    factor = '1000k'
    bf = 0
    gp = 1
    frameRate = 1

    input = "C:/Users/Frank/Desktop/useful_data/CASIA/orig"
    output = "C:/Users/Frank/Desktop/output3/CASIA/orig"
    imageToVideoToImage(input, output, factor, None, bf, gp, frameRate)

    input = "C:/Users/Frank/Desktop/useful_data/CASIA/tamp"
    output = "C:/Users/Frank/Desktop/output3/CASIA/tamp"
    imageToVideoToImage(input, output, factor, None, bf, gp, frameRate)

    input = "C:/Users/Frank/Desktop/useful_data/Columbia/orig"
    output = "C:/Users/Frank/Desktop/output3/Columbia/orig"
    imageToVideoToImage(input, output, factor, None, bf, gp, frameRate)

    input = "C:/Users/Frank/Desktop/useful_data/Columbia/tamp"
    output = "C:/Users/Frank/Desktop/output3/Columbia/tamp"
    imageToVideoToImage(input, output, factor, None, bf, gp, frameRate)

    input = "C:/Users/Frank/Desktop/useful_data/COVERAGE/orig"
    output = "C:/Users/Frank/Desktop/output3/COVERAGE/orig"
    imageToVideoToImage(input, output, factor, None, bf, gp, frameRate)

    input = "C:/Users/Frank/Desktop/useful_data/COVERAGE/tamp"
    output = "C:/Users/Frank/Desktop/output3/COVERAGE/tamp"
    imageToVideoToImage(input, output, factor, None, bf, gp, frameRate)


    assert False
    # image -> mp4 with one frame -> image
    input = '../data'  # EX: '../data'
    output = '../output2' # EX: '../output2'
    factor = '1000k'
    bf = 0
    gp = 1
    frameRate = 1
    removeAllFilesIn(output)
    imageToVideoToImage(input, output, factor, None, bf, gp, frameRate)


    # images to mp4
    input = '../data/AU_S_%3d.bmp'  # EX: '../data/AU_S_%3d.bmp'
    output = '../output1/vid.mp4'  # EX: '../output1/vid.mp4'
    factor = '1000k'
    bf = 0
    gp = 1
    frameRate = 1
    imagesToVideo(input, output, factor, None, bf, gp, frameRate)


    # mp4 to tif
    input = '../output1/vid.mp4'
    output = '../output2/img%03d.tif'  # EX: '../output2/img%03d.tif'
    videoToImages(input, output)



if __name__ == "__main__":
    main()


