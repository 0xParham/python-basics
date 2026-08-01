print("=" * 40)
print("      Body Mass Index Calculator")
print("=" * 40)

Weight = float(input("Enter the weight(kg):  "))
Height = float(input("Enter height(cm) "))/100

bmi = Weight / (Height**2)

if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal weight")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obesity")    
