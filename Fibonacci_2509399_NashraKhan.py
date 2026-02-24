# Fibonacci Series

n_terms = int(input("Number of Terms: "))
n1 = 0
n2 = 1
i = 2

print(n1)
print(n2)

while i < n_terms:
    nth = n1 + n2
    print(nth)

    n1 = n2
    n2 = nth
    i += 1

