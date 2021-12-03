class BankAccount:

    def __init__(self, name: str, account_number: str, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def print_balance(self):
        print(self.balance)

    def withdrawal(self, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            print("Sikeres pénzfelvétel!")
        else:
            print("Sikertelen pénzfelvétel! Nincs elég pénz a számlán!")

    def deposit(self, amount: int):
        self.balance += amount

    def send(self, other, amount: int):
        if self.balance >= amount:
            self.balance -= amount
            other.balance += amount
            print("Sikeres átutalás!")
        else:
            print("Sikertelen átutalás! Nincs elég pénz a számlán!")


account1 = BankAccount("User1", "00000000", 100000)
account2 = BankAccount("User2", "22222222")
account1.print_balance()
account2.print_balance()
account1.withdrawal(50000)
account2.withdrawal(50000)
account1.print_balance()
account2.print_balance()
account1.deposit(20000)
account2.deposit(20000)
account1.print_balance()
account2.print_balance()
account1.send(account2, 30000)
account1.print_balance()
account2.print_balance()
