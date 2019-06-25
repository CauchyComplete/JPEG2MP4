# Kwon Myung Joon
# June 25, 2019


from imagesToVideo import imagesToVideo
from videoToImages import videoToImages

def main():
    # images to mp4
    input = '..\data\AU_S_%3d.bmp'  # EX: '..\data\AU_S_%3d.bmp'
    output = '..\output1\output.mp4'  # EX: '..\output1\output.mp4'
    factor = '1000k'
    size = '128x128'
    bf = 0
    gp = 1
    frameRate = 1
    imagesToVideo(input, output, factor, size, bf, gp, frameRate)

    # mp4 to tif
    input = output
    output = '..\output2\img%03d.tif'  # EX: '..\output2\img%03d.tif'
    videoToImages(input, output)


if __name__ == "__main__":
    main()


