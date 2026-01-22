# 1.Write a program which accepts one character and checks whether it is vowel or consonant.

def Check(ch):
    if ch in ['a','e','i','o','u','A','E','I','O','U']:
        print("Vowel")
    else:
        print("Consonant")

def main():
    ch = input("Enter character : ")
    Check(ch)

if __name__ == "__main__":
    main()


# 2.Write a program which accepts one number and prints its factors.

def Factors(no):
    for i in range(1, no+1):
        if no % i == 0:
            print(i, end=" ")

def main():
    no = int(input("Enter number : "))
    Factors(no)

if __name__ == "__main__":
    main()


# 3.Write a program which accepts two numbers and prints addition, subtraction, multiplication and division.

def Arithmetic(a, b):
    print("Addition :", a + b)
    print("Subtraction :", a - b)
    print("Multiplication :", a * b)
    print("Division :", a / b)

def main():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    Arithmetic(a, b)

if __name__ == "__main__":
    main()


# 4.Write a program which accepts one number and prints that many numbers starting from 1.

def Display(no):
    for i in range(1, no+1):
        print(i, end=" ")

def main():
    no = int(input("Enter number : "))
    Display(no)

if __name__ == "__main__":
    main()


# 5.Write a program which accepts one number and prints that many numbers in reverse order.

def Reverse(no):
    for i in range(no, 0, -1):
        print(i, end=" ")

def main():
    no = int(input("Enter number : "))
    Reverse(no)

if __name__ == "__main__":
    main()
