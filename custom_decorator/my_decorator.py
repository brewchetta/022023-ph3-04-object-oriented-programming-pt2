def my_decorator(func):
    # func is the function that we've added the decorator to
    def wrapper(*args, **kargs):
        # the *args and **kargs just let us properly pass arguments and special keyword
        # arguments from the decorator to the inner function
        print("Decorator is happening")
        func(*args, **kargs)
        print("Decorator is happening again")
    return wrapper

@my_decorator
def say_name_and_age(name, age):
    print(f'my name is {name} and my age is {age}')

@my_decorator
def something():
    print('something')

def another_func():
    print("I am another function")

# this is how we might use a decorator without the @ syntax
another_func2 = my_decorator(another_func)

# this works due to the fact that python functions are 'first class functions'
# once we define a function we can pass it like any common variable
