class Numbers:
    def __init__(self, value):
        self.Value = value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i
        if sum == self.Value:
            return True
        else:
            return False

    def SumFactors(self):
        sum = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum = sum + i
        return sum


def main():
    obj = Numbers(6)

    print("Prime :", obj.ChkPrime())
    print("Perfect :", obj.ChkPerfect())
    print("Sum of Factors :", obj.SumFactors())


if __name__ == "__main__":
    main()