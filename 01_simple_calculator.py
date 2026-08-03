print("="*40)
print("      simple_calculator")
print("="*40)
print("Select the operation:")
print("1. -")
print("2. +")
print("3. ×")
print("4. ÷")

operator = input("Select the operator(1_4):  ")
num1 = float(input("Enter the first number:  "))
num2 = float(input("Enter the second number:  "))


if operator == '1':
    print("Answer ==",num1 - num2)
elif operator == '2':
    print("Answer ==",num1 + num2)
elif operator == '3':
    print("Answer ==",num1 * num2)
elif operator == '4':   
    
    if num2 == 0:
         print("Error: Cannot divide by zero!")
    else:
        print("Answer ==",num1/num2)

else:
    print("^^Invalid operator^^")
