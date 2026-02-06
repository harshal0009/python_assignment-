import os
import sys
import shutil

def DirectoryCopyExt(Src, Dest, Extension):
    if not os.path.isdir(Src):
        print("Invalid source directory")
        return

    if not os.path.exists(Dest):
        os.mkdir(Dest)

    for file in os.listdir(Src):
        if file.endswith(Extension):
            srcpath = os.path.join(Src, file)
            destpath = os.path.join(Dest, file)
            shutil.copy(srcpath, destpath)

def main():
    if len(sys.argv) != 4:
        print("Invalid number of arguments")
        return

    DirectoryCopyExt(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()