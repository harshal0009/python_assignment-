1.
import os
import sys

def DirectoryFileSearch(DirName, Extension):
    if not os.path.isdir(DirName):
        print("Invalid directory")
        return

    for file in os.listdir(DirName):
        if file.endswith(Extension):
            print(file)

def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        return

    DirectoryFileSearch(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()