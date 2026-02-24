# Function - Perfect Numbers

def perfect(n):
    sum = 0

    for i in range(1, n):  # Find all Divisors excluding n
        if n % i == 0:
            sum += i
    return sum == n

print(perfect(28))
