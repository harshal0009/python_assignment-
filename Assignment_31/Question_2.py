import os
import sys

def DirectoryRename(DirName, OldExt, NewExt):
    if not os.path.isdir(DirName):
        print("Invalid directory")
        return

    for file in os.listdir(DirName):
        if file.endswith(OldExt):
            oldpath = os.path.join(DirName, file)
            newfile = file.replace(OldExt, NewExt)
            newpath = os.path.join(DirName, newfile)
            os.rename(oldpath, newpath)

def main():
    if len(sys.argv) != 4:
        print("Invalid number of arguments")
        return

    DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()