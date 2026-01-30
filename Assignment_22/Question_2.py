class BankAccount:
    ROI = 10.5     # Class Variable

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder Name :", self.Name)
        print("Account Balance :", self.Amount)

    def Deposit(self, Value):
        self.Amount = self.Amount + Value

    def Withdraw(self, Value):
        if Value <= self.Amount:
            self.Amount = self.Amount - Value
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

def main():
    Obj1 = BankAccount("Utkarsh", 10000)
    Obj1.Display()

    Obj1.Deposit(2000)
    Obj1.Display()

    Obj1.Withdraw(3000)
    Obj1.Display()

    print("Interest Amount :", Obj1.CalculateInterest())

if __name__ == "__main__":
    main()