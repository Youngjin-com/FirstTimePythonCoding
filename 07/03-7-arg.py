def add_number(a, b):
    return a + b

def calc(func, a, b):
    print(f"func={func.__name__}")
    c = func(a, b)
    print(f"결과: {c}")

calc(add_number, 100, 30)