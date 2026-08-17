# Initializing the starting balance
balance = 1000

while True:
    print("=" * 40)
    print("      ATM Simulator")
    print("=" * 40)

    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")   
    
    choice = int(input("Select the operation:  "))
    
    if choice == 1:
        print("Your balance is:", balance)
    
    elif choice == 2:
        deposit_amount = float(input("Enter the deposit amount: "))
        # Updating the balance after deposit
        balance = balance + deposit_amount
        print("New Balance =", balance)

    elif choice == 3:
        withdraw_amount = float(input("Enter the withdraw amount: "))
        
        # Checking for sufficient funds
        if withdraw_amount > balance:
            print("<Unsuccessful withdrawal: Insufficient funds>")
        else:
            balance = balance - withdraw_amount
            print("New Balance =", balance)
            
    elif choice == 4:
        print("Goodbye!")
        break
        
    else:
        print("Enter a valid number!!")
