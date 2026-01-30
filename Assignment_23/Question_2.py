class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.Name = name
        self.Amount = amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self, value):
        self.Amount = self.Amount + value

    def Withdraw(self, value):
        if value <= self.Amount:
            self.Amount = self.Amount - value
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    acc = BankAccount("Sarthak", 10000)

    acc.Display()
    print()

    acc.Deposit(5000)
    acc.Withdraw(2000)

    acc.Display()
    print()

    print("Interest :", acc.CalculateInterest())


if __name__ == "__main__":
    main()