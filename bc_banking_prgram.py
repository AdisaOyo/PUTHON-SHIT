def show_balance(balance):
    print("**********************************")
    print(f"Your balance is ${balance:,.2f}")
    print("**********************************")
def deposite(balance):
    print("**********************************")
    amount = float(input("Enter an amount to be deposited: "))
    print("**********************************")
    if amount<0:
        print("**********************************")
        print("Not a valid amount")
        print("**********************************")
        return 0
    else:
        return amount 

def withdraw(balance):
    print("**********************************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("**********************************")
    if amount > balance:
        print("**********************************")
        print("Insufficient funds")
        print("**********************************")
        return 0
    elif amount < 0:
        print("**********************************")
        print("Amount must be greater than zero")
        print("**********************************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:

        print("**********************************")
        print("Banking program")
        print("**********************************")
        print("1. Show balance")
        print("2. Deposite")
        print("3. Withdrawal")
        print("4. Exit")
        print("**********************************")
        choice = input("Enter your choice [1-4]: ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposite()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("**********************************")
            print("Invalid choice")
            print("**********************************")
    print("**********************************")
    print("Thank you for banking with us!")
    print("**********************************")

if __name__ == '__main__':
    main()