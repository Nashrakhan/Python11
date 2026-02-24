# Function - Average of 3

def average(a, b, c = 17):
    return (a + b + c)/3

a = int(input('Enter 1st Number: '))
b = int(input('Enter 2nd Number: '))

print(f'Average: {average(a, b)}' )
