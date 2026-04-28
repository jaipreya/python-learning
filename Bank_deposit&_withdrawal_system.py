def deposit(balance, amount):
    if amount <= 0:
        return "Invalid deposit amount"
    else:
        balance=balance+amount
        return balance
def withdraw(balance, amount):
    if amount<=0:
        return "Invalid withdrawal amount"
    elif amount > balance:
        return "Insufficient balance"
    else:
        balance=balance-amount
        return balance
def check_balance(balance):
    return balance

balance=1000
while True:
    print("\nSelect an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    i = input("Enter your choice (1/2/3/4):")
    if i=="1":
        amount=int(input("Enter Amount to Deposit:"))
        result=deposit(balance,amount)
        if isinstance(result,int):
            balance=result
            print("Balance:",balance)
        else:
            print(result)
    elif i=="2":
        amount=int(input("Enter Amount to withdraw:"))
        result=withdraw(balance,amount)
        if isinstance(result,int):
            balance=result
            print("Balance:",balance)
        else:
            print(result)
    elif i=="3":
        print("Currentbalance:",check_balance(balance))
    elif i=="4":
        print("EXIT")
        break
    else:
        print("Invalid option Please try again")
    
