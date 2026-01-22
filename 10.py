# 1.Write a program which accepts one number and prints multiplication table of that number.

def Table(no):
    for i in range(1, 11):
        print(no * i, end=" ")

def main():
    no = int(input("Enter number : "))
    Table(no)

if __name__ == "__main__":
    main()


# 2.Write a program which accepts one number and prints sum of first N natural numbers.

def Sum(no):
    total = 0
    for i in range(1, no+1):
        total = total + i
    print(total)

def main():
    no = int(input("Enter number : "))
    Sum(no)

if __name__ == "__main__":
    main()


# 3.Write a program which accepts one number and prints factorial of that number.

def Factorial(no):
    fact = 1
    for i in range(1, no+1):
        fact = fact * i
    print(fact)

def main():
    no = int(input("Enter number : "))
    Factorial(no)

if __name__ == "__main__":
    main()


# 4.Write a program which accepts one number and prints all even numbers till that number.

def Even(no):
    for i in range(2, no+1, 2):
        print(i, end=" ")

def main():
    no = int(input("Enter number : "))
    Even(no)

if __name__ == "__main__":
    main()


# 5.Write a program which accepts one number and prints all odd numbers till that number.

def Odd(no):
    for i in range(1, no+1, 2):
        print(i, end=" ")

def main():
    no = int(input("Enter number : "))
    Odd(no)

if __name__ == "__main__":
    main()
