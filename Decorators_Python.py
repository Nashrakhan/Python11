# Python Decorator

def changecase(func):
    def myinner(*x, **y):
        return func(*x, **y).upper()
    return myinner

@changecase
def myfunction(*name):
    return ' Hello ' + name[1] # 0 for Madinah & 1 for Nashra Khan

@changecase
def otherfunction(age):
    return ' I am ' + age

print(myfunction('Madinah!', 'Nashra Khan'))
print(otherfunction('17'))
