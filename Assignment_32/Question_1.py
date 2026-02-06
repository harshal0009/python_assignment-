import os
import sys
import hashlib

def CalculateChecksum(FilePath):
    fd = open(FilePath, 'rb')
    hobj = hashlib.md5()
    buffer = fd.read(1024)
    while buffer:
        hobj.update(buffer)
        buffer = fd.read(1024)
    fd.close()
    return hobj.hexdigest()

def DirectoryChecksum(DirName):
    if not os.path.isdir(DirName):
        print("Invalid directory")
        return

    for file in os.listdir(DirName):
        filepath = os.path.join(DirName, file)
        if os.path.isfile(filepath):
            print(file, ":", CalculateChecksum(filepath))

def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return

    DirectoryChecksum(sys.argv[1])

if __name__ == "__main__":
    main()