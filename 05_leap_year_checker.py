print("="*40)
print("   leap year checker")
print("="*40)

year = int(input("Enter the year:  ")) 

if (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0):
    print("Leap Year!")
else:
    print("not Leap Year!")    
