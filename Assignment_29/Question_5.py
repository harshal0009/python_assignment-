filename = input("Enter file name: ")
word = input("Enter string to search: ")

count = 0

with open(filename, 'r') as f:
    data = f.read()
    count = data.count(word)

print("Frequency:", count)
