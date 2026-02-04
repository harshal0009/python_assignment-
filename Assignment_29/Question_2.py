filename = input("Enter file name: ")

try:
    with open(filename, 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File not found")
filename = input("Enter file name: ")

try:
    with open(filename, 'r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("File not found")
