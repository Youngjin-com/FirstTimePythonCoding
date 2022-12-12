import time

def time_checker(func):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time() - start_time
        print(f"함수 수행 시간: {end_time}")
        return result
    return inner_function

@time_checker
def test_func1():
    for i in range(3):
        time.sleep(1)

@time_checker
def test_func2():
    for i in range(3):
        time.sleep(1)

@time_checker
def test_func3():
    for i in range(3):
        time.sleep(1)

test_func1()
test_func2()
test_func3()