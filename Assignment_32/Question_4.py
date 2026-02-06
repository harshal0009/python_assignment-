import os
import sys
import hashlib
import time

def CalculateChecksum(FilePath):
    fd = open(FilePath, 'rb')
    hobj = hashlib.md5()
    buffer = fd.read(1024)
    while buffer:
        hobj.update(buffer)
        buffer = fd.read(1024)
    fd.close()
    return hobj.hexdigest()

def DeleteDuplicate(DirName):
    checksum = {}
    log = open("Log.txt", "w")

    for file in os.listdir(DirName):
        filepath = os.path.join(DirName, file)
        if os.path.isfile(filepath):
            hashvalue = CalculateChecksum(filepath)
            if hashvalue in checksum:
                os.remove(filepath)
                log.write(file + "\n")
            else:
                checksum[hashvalue] = file

    log.close()

def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        return

    if not os.path.isdir(sys.argv[1]):
        print("Invalid directory")
        return

    starttime = time.time()
    DeleteDuplicate(sys.argv[1])
    endtime = time.time()

    print("Execution time:", endtime - starttime)

if __name__ == "__main__":
    main()