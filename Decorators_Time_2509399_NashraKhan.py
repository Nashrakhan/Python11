# Decorators - Print Time

import time

def time_logger(func):
    def wrapper():
        print(f'Start Time: {time.ctime}')
        func()
        print(f'End Time: {time.ctime}')
    return wrapper

@time_logger
def display_message():
    print('This is a Sample Message')

display_message() # Calling the Function
    
            
