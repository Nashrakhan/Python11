# Function - Prime Number

def prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    for x in range(2, int(n/2) + 1):  # check up to n/2
        if n % x == 0:  # divisible by x
            return False
    return True

n = int(input('Enter a Number: '))

if prime(n):
    print(f'{n} is Prime')
else:
    print(f'{n} is Not Prime')

