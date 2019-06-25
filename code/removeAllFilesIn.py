import os


def removeAllFilesIn(dir):
    for file in os.listdir(dir):
        os.remove(dir+'/'+file)
