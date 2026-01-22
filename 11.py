# 1.Write a program which accepts length and width of rectangle and prints area.

def AreaRect(l, w):
    print("Area :", l * w)

def main():
    l = float(input("Enter length : "))
    w = float(input("Enter width : "))
    AreaRect(l, w)

if __name__ == "__main__":
    main()


# 2.Write a program which accepts radius of circle and prints area of circle.

def AreaCircle(r):
    pi = 3.14
    print("Area :", pi * r * r)

def main():
    r = float(input("Enter radius : "))
    AreaCircle(r)

if __name__ == "__main__":
    main()


# 3.Write a program which accepts one number and checks whether it is perfect number or not.

def Perfect(no):
    sum = 0
    for i in range(1, no):
        if no % i == 0:
            sum = sum + i

    if sum == no:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

def main():
    no = int(input("Enter number : "))
    Perfect(no)

if __name__ == "__main__":
    main()


# 4.Write a program which accepts one number and prints binary equivalent of that number.

def Binary(no):
    print(bin(no)[2:])

def main():
    no = int(input("Enter number : "))
    Binary(no)

if __name__ == "__main__":
    main()


# 5.Write a program which accepts marks and displays grade.

# Condition:[≥ 75 → Distinction,≥ 60 → First Class,≥ 50 → Second Class,< 50 → Fail]


def Grade(marks):
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 50:
        print("Second Class")
    else:
        print("Fail")

def main():
    marks = int(input("Enter marks : "))
    Grade(marks)

if __name__ == "__main__":
    main()
