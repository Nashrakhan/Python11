# Decorator

def welcome_decorator(func):
    def wrapper():
        print('Welcome')
        func()
    return wrapper

@welcome_decorator
def atlas():
    print('To ATLAS')

atlas()
