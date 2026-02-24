# Recursive Function - Reverse a String

def reverse(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse(s[:-1])

string = 'HELLO'
print(reverse(string))
