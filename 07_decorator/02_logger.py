from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger

def brew_chai(type):
    print(f"Brewing {type} chai")
brew_chai("masala")