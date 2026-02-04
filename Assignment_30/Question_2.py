filename = input("Enter file name: ")

with open(filename, 'r') as f:
    data = f.read()
    words = data.split()

print("Total words:", len(words))
