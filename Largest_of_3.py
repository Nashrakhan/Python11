# LARGEST OF 3 NUMBERS USING CONDITION STATEMENTS

a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))

if a > b and a > c:
    print(f'{a} is the Largest Number')
elif b > a and b > c:
    print(f'{b} is the Largest Number')
else:
    print(f'{c} is the Largest Number')
