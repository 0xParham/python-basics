while True:
    print("=" * 40)
    print("      Smart Multiplication")
    print("=" * 40)

    num = int(input("Enter your number:  "))
    limit = int(input("Number continuation: "))
    
    print("-" * 40)
    
    for i in range(1, limit + 1):
        result = num * i
        
        print(f"{num} * {i} = {result}")
        
    print("-" * 40)
    print("End of commands (yes/no)?")
    end = input("    :")
     
    if end.lower() == "yes":
        print("Goodbye!")
        break
