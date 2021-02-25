usernameInput = input("Username : ")
passwordInput = input("Password : ")
btc = 1000000
eth = 50000
xrp = 20
if usernameInput == "user" and passwordInput == "1111":
    print("Welcome to Crypto minishop")
    print("----------------------")
    print("[1] BTC", btc, "THB.")
    print("[2] ETH", eth, "THB.")
    print("[3] XRP", xrp, "THB.")
    coin = input("Please input [number] of coin: ")
    if coin == "1":
        coin = btc
    elif coin == "2":
        coin = eth
    else:
        coin = xrp
    amount = float(input("Amount: "))
    print("Result:",coin*amount)
else:
    print("Username/Password Incorrect!!!")

