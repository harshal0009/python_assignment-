class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def Factors(self):
        print("Factors of", self.Value, "are :")
        for i in range(1, self.Value):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i
        return Sum

    def ChkPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False

def main():
    Obj1 = Numbers(28)

    if Obj1.ChkPrime():
        print("Number is Prime")
    else:
        print("Number is Not Prime")

    Obj1.Factors()
    print("Sum of Factors :", Obj1.SumFactors())

    if Obj1.ChkPerfect():
        print("Number is Perfect")
    else:
        print("Number is Not Perfect")

if __name__ == "__main__":
    main()