# Kwon Myung Joon
# June 25, 2019

from imagesToVideo import imagesToVideo
from videoToImages import videoToImages
from imageToVideoToImage import imageToVideoToImage
from removeAllFilesIn import removeAllFilesIn


def main():
    input = '../data'
    output = '../output2'
    factor = '1000k'
    bf = 0
    gp = 1
    frameRate = 1
    removeAllFilesIn(output)
    imageToVideoToImage(input, output, factor, None, bf, gp, frameRate)

    """
    SAMPLE USAGE
    # images to mp4
    input = '../data/AU_S_000.bmp'  # EX: '../data/AU_S_%3d.bmp'
    output = '../output1/vid.mp4'  # EX: '../output1/vid.mp4'
    factor = '1000k'
    bf = 0
    gp = 1
    frameRate = 1
    imagesToVideo(input, output, factor, None, bf, gp, frameRate)

    # mp4 to tif
    input = output
    output = '../output2/img%03d.tif'  # EX: '../output2/img%03d.tif'
    videoToImages(input, output)
    """

if __name__ == "__main__":
    main()


