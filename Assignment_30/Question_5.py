filename = input("Enter file name: ")
word = input("Enter word to search: ")

with open(filename, 'r') as f:
    data = f.read()

if word in data:
    print("Word found")
else:
    print("Word not found")
