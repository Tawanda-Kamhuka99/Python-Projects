#Set constants 
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

#Deposit function which collects user deposit amount
def deposit():
    while True:
        amount = input("\nPlease enter a deposit amount: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 10:
                print(f"\nYour balance is now ${amount}.")
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

#Function which gets the amount the user wants to bet on each line
def get_bet():
    while True:
        amount = input("\nHow much would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                print(f"\nYour bet amount is ${amount}.")
                break
            else:
                print(f"\nPlease enter a betting amount between ${MIN_BET} - ${MAX_BET}")
        else:
            print("\nPlease enter an amount.")
    
    return amount


#Create main function 
def main():
    balance = deposit()
    lines = get_lines()
    while True:
        bet_amount = get_bet()
        total_bet = lines * bet_amount
        if total_bet > balance:
            print(f"\nYou do not have enough funds. Your current balance is ${balance}. Please try again.")
        else:
            break

    print(f"\nYou are betting ${bet_amount} on {lines} lines. Total bet is: ${total_bet}.)")

main()