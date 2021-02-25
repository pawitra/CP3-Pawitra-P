def vatCalculate(price):
    return price + (price*7/100)

totalPrice = float(input("Price: "))
print(vatCalculate(totalPrice))