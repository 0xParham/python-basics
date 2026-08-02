print("=" * 40)
print("      Temperature Converter")
print("=" * 40)
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))
print("  ")
Action2 = float(input("Enter the amount:  "))

if choice == 1:
    print("Faherenheit:",(Action2*1.8)+32)
elif choice == 2:
    print("Celsius:",(Action2-32)/1.8)   
else: 
    print("Unsuccessful operation! Please enter 1 or 2.")   
