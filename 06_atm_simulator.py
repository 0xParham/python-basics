balance = 1000

while True:
    
    print("="*40)
    print("   atm_simulator")
    print("="*40)

    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")   
    
    choice = int(input("Select the operation:  "))
    
    if choice == 1:
       print("Your balance is:", balance)
    
    elif choice == 2:
        deposit = float(input("Enter the deposit amount: "))
        balance = deposit+balance
        print("New Balance =", balance)

    elif choice == 3:
        Withdraw = float(input("Enter the Withdraw amount:"))
        if Withdraw > balance:
            print("<Unsuccessful withdrawal>")
        else:
            balance = balance-Withdraw
            print("New Balance =",balance)
            
    elif choice == 4:
        break
    else:
        print("Enter a valid number!!")
