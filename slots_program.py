#Set constants 
MAX_LINES = 3

#Deposit function which collects user deposit amount
def deposit():
    while True:
        amount = input("\nPlease enter a deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 10:
                print(f"\nYou deposited ${amount}.")
                break
            else:
                print("\nPlease enter an amount greater than $10.")
        else:
            print("\nPlease enter a number.")
    
    return amount

#Function which gets number of lines user wants to bet on
def get_lines():
    while True:
        lines = input("\nSelect the number of lines to bet on (1-" + str(MAX_LINES) + ") : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                print(f"\nYou have chosen {lines} lines.")
                break
            else:
                print("\nPlease enter a valid amount of lines.")
        else:
            print("\nPlease enter number of lines.")
    
    return lines


#Create main function 
def main():
    balance = deposit()
    lines = get_lines()

main()