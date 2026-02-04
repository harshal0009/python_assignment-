filename = input("Enter file name: ")

count = 0

with open(filename, 'r') as f:
    for line in f:
        count += 1

print("Total lines:", count)
