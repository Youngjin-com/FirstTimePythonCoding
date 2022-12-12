import time

def test_function():
    for i in range(3):
        time.sleep(1)

start_time = time.time()
test_function()
end_time = time.time() - start_time
print(f"함수 동작 시간: {end_time}")