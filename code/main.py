# Kwon Myung Joon
# June 25, 2019

from imagesToVideo import imagesToVideo
from videoToImages import videoToImages
from imageToVideoToImage import imageToVideoToImage
from removeAllFilesIn import removeAllFilesIn

# Disclaimer : Every path must not contain blank(' ') character.
# If 'temp' directory already exists, please rename it or modify code.
# Every directory you mentioned must be exist before running the code.

def main():
    # image -> mp4 with one frame -> image
    input = 'C:/Users/Frank/Desktop/Zhou_Datasets/Columbia/ImSpliceDataset'  # '../data'
    output = '../output2/Columbia/tampered'
    factor = '1000k'
    bf = 0
    gp = 1
    frameRate = 1
    removeAllFilesIn(output)
    imageToVideoToImage(input, output, factor, None, bf, gp, frameRate, fileStarts='SP', outputFilePrefix='Columbia_spliced_%03d_')


    # images to mp4
    """
    input = '../data/AU_S_000.bmp'  # EX: '../data/AU_S_%3d.bmp'
    output = '../output1/vid.mp4'  # EX: '../output1/vid.mp4'
    factor = '1000k'
    bf = 0
    gp = 1
    frameRate = 1
    imagesToVideo(input, output, factor, None, bf, gp, frameRate)
    """

    # mp4 to tif
    """
    input = output
    output = '../output2/img%03d.tif'  # EX: '../output2/img%03d.tif'
    videoToImages(input, output)
    """


if __name__ == "__main__":
    main()


