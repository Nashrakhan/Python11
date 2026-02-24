# NUMBER DIVISIBLE BY 3 & 5 OR BOTH

number = int(input('Enter a Number: '))

if (number % 3 == 0) and (number % 5 == 0):
    print(f'{number} is divisible by both 3 & 5')
elif (number % 3 == 0) and (number % 5 != 0):
    print(f'{number} is divisible only by 3')
elif (number % 3 != 0) and (number % 5 == 0):
    print(f'{number} is divisible only by 5')
else:
    print(f'{number} is neither divisible by 3 or 5')
