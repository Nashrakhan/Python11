# Star Pattern

for i in range(5, 0, -1):
    print(" * " * i)

print()

rows = 4
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2*i + 1))

print()

rows = 5
for i in range(1, rows+1):
    print(" " * (rows - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print()

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

print()

rows = 5
for i in range(rows):
    ch = chr(65 + i)
    for j in range(i + 1):
        print(ch, end=" ")
    print()
