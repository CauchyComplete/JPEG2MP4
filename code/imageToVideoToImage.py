# Kwon Myung Joon
# June 25, 2019

import os
import shutil
from imagesToVideo import imagesToVideo
from videoToImages import videoToImages


def imageToVideoToImage(input, output, factor, size, bf, gp, frameRate, outputFilePrefix=''):
    """
    First converts all images in 'input' to mp4 (video with one frame)
    Then converts them one by one to the original file format
    """
    # EX: input = '../data'
    # EX: output = '../output2' This must be an empty directory.
    # EX: outputFilePrefix = 'output%03d' or 'output' or ''
    tempDirectory = input + '/../temp'
    os.mkdir(tempDirectory)
    fileCount = 0
    for root, dirs, files in os.walk(input):  # all files on directory including files in subdirectory
        for f in files:
            fileCount +=1
            file = root + '/' + f

            # images to mp4
            copy_file = tempDirectory + '/im001.' + file.split('.')[-1]
            shutil.copy2(file, copy_file)
            input2 = tempDirectory + '/im%3d.' + file.split('.')[-1]
            output2 = tempDirectory + '/vid001.mp4'
            imagesToVideo(input2, output2, factor, size, bf, gp, frameRate)
            os.remove(copy_file)

            # mp4 to image
            input2 = output2
            if not outputFilePrefix == '':
                if '%' in outputFilePrefix:
                    temp = outputFilePrefix % fileCount
                else :
                    temp = outputFilePrefix
                output3 = output + '/' + temp + f
            else :
                output3 = output + '/' + f
            videoToImages(input2, output3)
            os.remove(input2)

    os.rmdir(tempDirectory)
