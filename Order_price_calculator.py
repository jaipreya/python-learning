def calculate_total_price(price, quantity):
    return price*quantity
def apply_discount(total):
    if total >= 1000:
        total=total-(total*0.10)
        return total
    elif total >= 500:
        total=total-(total*0.05)
        return total
    else:
        return total

def apply_tax(amount):
    amount= amount + (amount*0.18)
    return amount
price=int(input("Enter price:"))
quantity=int(input("Enter quantity:"))
if price<=0 or quantity<=0:
    print("Invalid number entered please enter correct price and quantity")
        

total=calculate_total_price(price,quantity)
amount=apply_discount(total)
tax=apply_tax(amount)

print("Total:",total)
print("After Discount:",amount)
print("Final Price(with tax):",round(tax,2))

    
