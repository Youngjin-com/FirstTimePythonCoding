def outer_function(func):
    def inner_function(*args, **kwargs):
        print(f"함수명: {func.__name__}")
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        result = func(*args, **kwargs)
        return result
    return inner_function

def add(a, b):
    return a + b

f = outer_function(add)
f(10, 20)