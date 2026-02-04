import sys

source = sys.argv[1]
destination = "Demo.txt"

with open(source, 'r') as f1:
    data = f1.read()

with open(destination, 'w') as f2:
    f2.write(data)

print("Content copied successfully")
