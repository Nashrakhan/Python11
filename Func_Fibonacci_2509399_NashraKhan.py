# Function - Fibonacci Series

def fibonacci(n):
    a , b = 0, 1
    for _ in range(n):
        print(a, end = ' ')
        a, b = b, a + b
    print()
n = int(input('Enter Number: '))
fibonacci(n)
