
print("                   BANK ACCOUNT MANAGEMENT SYSTEM           ")

class bankaccount:

    def __init__(self, name, pin, balance):
        self.name = name
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print("Your balance is", self.balance)

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))

        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
            print("new amount",self.balance)
        else:
            print("INVALID AMOUNT!!")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))

        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("NOT SUCCESSFUL!!")


account = bankaccount("Taimoor", 345, 2000)

attempts = 3

while attempts > 0:

    pin = int(input("Enter your PIN: "))

    if pin == account.pin:

        print("Login successful!")

        while True:

            print("\nHERE IS YOUR BANK ACCOUNT MENU")
            print("1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                account.check_balance()
                

            elif choice == 2:
                account.deposit()
                break
        

            elif choice == 3:
                account.withdraw()

            elif choice == 4:
                print("Thank you!")
                break

            else:
                print("Invalid input!")

        break

    else:
        attempts -= 1
        print("Wrong PIN!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("No attempts left! Account locked.")


                    