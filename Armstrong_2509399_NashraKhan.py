# Armstrong

num = int(input('Enter a Number: '))

num_str = str(num)
n = len(num_str)
sum_of_powers = 0

for digit in num_str:
    sum_of_powers += int(digit) ** n

if num == sum_of_powers:
    print(f'{num} is an Armstrong Number ')
else:
    print(f'{num} is not an Armstrong Number ')

    
