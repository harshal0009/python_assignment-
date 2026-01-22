# 1.Write a program which contains one function named as Display() that prints "Jay Ganesh" on console.

def Display():
    print("Jay Ganesh")

def main():
    Display()

if __name__ == "__main__":
    main()


# 2.Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number.

def ChkGreater(a, b):
    if a > b:
        print(a, "is greater")
    else:
        print(b, "is greater")

def main():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    ChkGreater(a, b)

if __name__ == "__main__":
    main()


# 3.Write a program which accepts one number and prints square of that number.

def Square(no):
    print(no * no)

def main():
    no = int(input("Enter number : "))
    Square(no)

if __name__ == "__main__":
    main()


# 4.Write a program which accepts one number and prints cube of that number.

def Cube(no):
    print(no * no * no)

def main():
    no = int(input("Enter number : "))
    Cube(no)

if __name__ == "__main__":
    main()


# 5.Write a program which accepts one number and checks whether it is divisible by 3 and 5.

def Divisible(no):
    if no % 3 == 0 and no % 5 == 0:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible")

def main():
    no = int(input("Enter number : "))
    Divisible(no)

if __name__ == "__main__":
    main()
