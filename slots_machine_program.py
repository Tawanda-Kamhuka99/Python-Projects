#Import random module to randomize slot machine values
import random

#Set constants 
MAX_LINES = 3

MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

#Symbols and number of symbols per reel
symbol_count = {
    'A': 2,
    'B': 3,
    'C': 4,
    'D': 4,
}

#Symbols value per reel
symbol_values = {
    'A': 10,
    'B': 8,
    'C': 6,
    'D': 4,
}

#Function which checks if user won or not
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line] 
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


#Function which generates slot machine outcome
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

#Function which prints slot machine results
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()
    

#Function which collects user deposit amount
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
                print(f"\nYou have chosen to bet on {lines} lines.")
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
                break
            else:
                print(f"\nPlease enter a betting amount between ${MIN_BET} - ${MAX_BET}")
        else:
            print("\nPlease enter an amount.")
    
    return amount

#Function which allows player to keep playing
def spin(balance):
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"\nYou do not have enough funds for that bet.\n\tRequested bet is: ${total_bet}\n\tYour current balance is ${balance}.\n\tPlease try again.")
        else:
            break

    print(f"\nYou are betting ${bet} on {lines} lines. Total bet is: ${total_bet}.\n")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"\nYou have won: ${winnings}.")
    print(f"\nYou won on line", *winning_lines)

    return winnings - total_bet

#Main function 
def main():
    balance = deposit()
    while True:
        print(f"\nCurrent balance is ${balance}")
        answer = input("\nPress enter to spin or q to quit: ")
        if spin == 'q':
            break
        balance += spin(balance)

    print(f"\nYou are left with ${balance}.")


main()
