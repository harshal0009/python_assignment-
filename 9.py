# 1. Write a program which accepts one number and checks whether it is prime or not.

def CheckPrime(no):
    if no <= 1:
        print("Not Prime Number")
        return

    for i in range(2, no):
        if no % i == 0:
            print("Not Prime Number")
            return

    print("Prime Number")

def main():
    no = int(input("Enter number : "))
    CheckPrime(no)

if __name__ == "__main__":
    main()


# 2. Write a program which accepts one number and prints count of digits in that number.

def CountDigits(no):
    count = 0
    while no > 0:
        count += 1
        no //= 10
    print(count)

def main():
    no = int(input("Enter number : "))
    CountDigits(no)

if __name__ == "__main__":
    main()


# 3. Write a program which accepts one number and prints sum of digits.

def SumDigits(no):
    sum = 0
    while no > 0:
        sum += no % 10
        no //= 10
    print(sum)

def main():
    no = int(input("Enter number : "))
    SumDigits(no)

if __name__ == "__main__":
    main()


# 4. Write a program which accepts one number and prints reverse of that number.

def Reverse(no):
    rev = 0
    while no > 0:
        rev = (rev * 10) + (no % 10)
        no //= 10
    print(rev)

def main():
    no = int(input("Enter number : "))
    Reverse(no)

if __name__ == "__main__":
    main()


# 5. Write a program which accepts one number and checks whether it is palindrome or not

def Palindrome(no):
    temp = no
    rev = 0

    while no > 0:
        rev = (rev * 10) + (no % 10)
        no //= 10

    if temp == rev:
        print("Palindrome")
    else:
        print("Not Palindrome")

def main():
    no = int(input("Enter number : "))
    Palindrome(no)

if __name__ == "__main__":
    main()
