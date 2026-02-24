# Decorators - Print Welcome!

def welcome_decorator(func):
    def wrapper():
        print('Welcome!')
        func()
    return wrapper

@welcome_decorator
def greet():
    print('Have a nice day')

greet() # Call the function
