def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling function with arguments:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet('wekiat')