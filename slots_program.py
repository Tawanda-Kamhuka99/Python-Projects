#Deposit function which collects user deposit amount
def deposit():
    while True:
        amount = input("Please enter a deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 10:
                print(f"You deposited ${amount}.")
                break
            else:
                print("Please enter an amount greater than $10.")
        else:
            print("Please enter a number.")
    
    return amount

deposit()

