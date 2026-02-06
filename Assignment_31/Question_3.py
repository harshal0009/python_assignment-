import os
import sys
import shutil

def DirectoryCopy(Src, Dest):
    if not os.path.isdir(Src):
        print("Invalid source directory")
        return

    if not os.path.exists(Dest):
        os.mkdir(Dest)

    for file in os.listdir(Src):
        srcpath = os.path.join(Src, file)
        destpath = os.path.join(Dest, file)
        if os.path.isfile(srcpath):
            shutil.copy(srcpath, destpath)

def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        return

    DirectoryCopy(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()