import os
import shutil
from imagesToVideo import imagesToVideo
from videoToImages import videoToImages


def imageToVideoToImage(input, output, factor, size, bf, gp, frameRate):
    """
    First converts all images in 'input' to mp4 (video with one frame)
    Then converts them one by one to the original file format
    """
    # EX: input = '../data'
    # EX: output = '../output2'
    tempDirectory = input+'/../temp'
    os.mkdir(tempDirectory)
    for root, dirs, files in os.walk(input):  # all files on directory including files in subdirectory
        for f in files:
            if f.split('.')[-1] == 'txt':
                continue

            file = root + '/' + f

            # images to mp4
            copy_file = tempDirectory + '/im001.' + file.split('.')[-1]
            shutil.copy2(input + '/' + file, copy_file)
            input2 = tempDirectory + '/im%3d.' + file.split('.')[-1]
            output2 = tempDirectory + '/vid001.mp4'
            imagesToVideo(input2, output2, factor, size, bf, gp, frameRate)
            os.remove(copy_file)

            # mp4 to image
            input2 = output2
            output3 = output + '/' + f
            videoToImages(input2, output3)
            os.remove(input2)

    os.rmdir(tempDirectory)
