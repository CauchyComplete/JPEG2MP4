# Kwon Myung Joon
# June 25, 2019

import os


def removeAllFilesIn(dir):
    for file in os.listdir(dir):
        os.remove(dir+'/'+file)
