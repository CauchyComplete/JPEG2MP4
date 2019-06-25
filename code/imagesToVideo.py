# need ffmpeg installed and bin added to PATH

import os


def imagesToVideo(input, output, factor, size, bf, gp, frameRate):
    command = 'ffmpeg -r %d -start_number 1 -s:v %s -i %s -c:v libx264 -x264opts keyint=%d:min-keyint=%d:scenecut=-1 -r %d -b:v %s -bufsize %s -bf %d -an -y %s' % (
    frameRate, size, input, gp, gp, frameRate, factor, factor, bf, output)
    # EX: 'ffmpeg -r 30 -start_number 0 -s:v 128x128 -i ..\data\AU_S_%3d.bmp -c:v libx264 -x264opts keyint=1:min-keyint=1:scenecut=-1 -r 30 -b:v 1000k -bf 0 -an -y ..\output\output.mp4'
    os.system(command)

