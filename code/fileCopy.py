# Kwon Myung Joon
# June 25, 2019

import os
import shutil
from removeAllFilesIn import removeAllFilesIn

def copyFiles(input, output, fileFormat, fileStarts, fileEnds, fileContains, fileNotContains):
    # EX: fileFormat = ('bmp', 'jpg', 'tif', 'png')
    # EX: fileStarts = 'img'
    # EX: fileEnds = ''
    # EX: fileContains = 'copy'
    # EX: fileNotContains = ['original','copy'] or None
    for root, dirs, files in os.walk(input):  # all files on directory including files in subdirectory
        for f in files:
            if f.split('.')[-1] not in fileFormat:
                continue

            fileNameWithoutFormat = os.path.splitext(f)[0]
            if not (fileNameWithoutFormat.startswith(fileStarts) and fileNameWithoutFormat.endswith(fileEnds)
                    and (fileContains in fileNameWithoutFormat)):
                continue
            if fileNotContains is not None:
                flag = True
                for s in fileNotContains:
                    if s in fileNameWithoutFormat:
                        flag=False
                        break
                if flag == False:
                    continue

            file = root + '/' + f
            copy_file = output + '/' + f
            shutil.copy2(file, copy_file)


def main():
    # CASIA processing
    # orig
    input = "C:/Users/Frank/Desktop/Zhou_Datasets/CASIA/benchmark_data"
    output = "C:/Users/Frank/Desktop/useful_data/CASIA/orig"
    fileFormat = ("png",)
    fileStarts = ""
    fileEnds = ""
    fileContains = ""
    fileNotContains = ["orig","bearb","1","2","3","4","5","6","copy"]
    removeAllFilesIn(output)
    copyFiles(input, output, fileFormat, fileStarts, fileEnds, fileContains, fileNotContains)

    # tamp
    input = "C:/Users/Frank/Desktop/Zhou_Datasets/CASIA/benchmark_data"
    output = "C:/Users/Frank/Desktop/useful_data/CASIA/tamp"
    fileFormat = ("png",)
    fileStarts = ""
    fileEnds = ""
    fileContains = "copy"
    fileNotContains = ["orig", "bearb", "1", "2", "3", "4", "5", "6"]
    removeAllFilesIn(output)
    copyFiles(input, output, fileFormat, fileStarts, fileEnds, fileContains, fileNotContains)

    # mask
    input = "C:/Users/Frank/Desktop/Zhou_Datasets/CASIA/benchmark_data"
    output = "C:/Users/Frank/Desktop/useful_data/CASIA/mask"
    fileFormat = ("png",)
    fileStarts = ""
    fileEnds = ""
    fileContains = "alpha"
    fileNotContains = ["orig", "bearb", "copy", "trim"]
    removeAllFilesIn(output)
    copyFiles(input, output, fileFormat, fileStarts, fileEnds, fileContains, fileNotContains)


    # Columbia processing
    # orig
    input = "C:/Users/Frank/Desktop/Zhou_Datasets/Columbia/ImSpliceDataset"
    output = "C:/Users/Frank/Desktop/useful_data/Columbia/orig"
    fileFormat = ("bmp",)
    fileStarts = "AU"
    fileEnds = ""
    fileContains = ""
    fileNotContains = None
    removeAllFilesIn(output)
    copyFiles(input, output, fileFormat, fileStarts, fileEnds, fileContains, fileNotContains)

    # tamp
    input = "C:/Users/Frank/Desktop/Zhou_Datasets/Columbia/ImSpliceDataset"
    output = "C:/Users/Frank/Desktop/useful_data/Columbia/tamp"
    fileFormat = ("bmp",)
    fileStarts = "SP"
    fileEnds = ""
    fileContains = ""
    fileNotContains = None
    removeAllFilesIn(output)
    copyFiles(input, output, fileFormat, fileStarts, fileEnds, fileContains, fileNotContains)

    # COVERAGE processing
    # orig
    input = "C:/Users/Frank/Desktop/Zhou_Datasets/COVERAGE/image"
    output = "C:/Users/Frank/Desktop/useful_data/COVERAGE/orig"
    fileFormat = ("tif",)
    fileStarts = ""
    fileEnds = ""
    fileContains = ""
    fileNotContains = ["t"]
    removeAllFilesIn(output)
    copyFiles(input, output, fileFormat, fileStarts, fileEnds, fileContains, fileNotContains)

    # tamp
    input = "C:/Users/Frank/Desktop/Zhou_Datasets/COVERAGE/image"
    output = "C:/Users/Frank/Desktop/useful_data/COVERAGE/tamp"
    fileFormat = ("tif",)
    fileStarts = ""
    fileEnds = "t"
    fileContains = ""
    fileNotContains = None
    removeAllFilesIn(output)
    copyFiles(input, output, fileFormat, fileStarts, fileEnds, fileContains, fileNotContains)

    # mask
    input = "C:/Users/Frank/Desktop/Zhou_Datasets/COVERAGE/mask"
    output = "C:/Users/Frank/Desktop/useful_data/COVERAGE/mask"
    fileFormat = ("tif",)
    fileStarts = ""
    fileEnds = ""
    fileContains = "forged"
    fileNotContains = None
    removeAllFilesIn(output)
    copyFiles(input, output, fileFormat, fileStarts, fileEnds, fileContains, fileNotContains)

if __name__ == "__main__":
    main()
