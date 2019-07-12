# ----------------------------------
# Kwon Myung Joon (CauchyComplete)
# July 12, 2019
# ----------------------------------

import os

def rename_files(path, replace_old, replace_new):
    for file in os.listdir(path):
        f1, f2 = os.path.splitext(file)
        f1 = f1.replace(replace_old, replace_new)
        os.rename(os.path.join(path,file),os.path.join(path,f1+f2))

def main():
    path = "C:/Users/Frank/Desktop/ImageManipulationDetection-PengZhou-2018/data/COVERAGE/mask"
    replace_old = "forged"
    replace_new = ""
    rename_files(path, replace_old, replace_new)

if __name__ == "__main__":
    main()
