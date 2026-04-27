def withdraw(balance,amount):
    if amount>balance:
        return "insufficient balance"
    elif amount<=0:
        return "Invalid amount"
    else:
        balance=balance - amount
        return balance
    
def check_balance(balance):
    return balance

balance=2000
 
print("Balance:",balance)
amount=int(input("Enter amount to withdraw:"))
result=withdraw(balance,amount)
if isinstance(result,int):
    balance=result
    remaining_balance=check_balance(balance)
    print("Remaining Balance",remaining_balance)
else:
    print(result)