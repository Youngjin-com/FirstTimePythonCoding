def add_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

v = 5
print(f"1부터 {v}까지의 합: {add_n(v)}")

def add_r(n):
    if n == 0:
        return 0
    n += add_r(n-1)
    return n

print(f"1부터 {v}까지의 합: {add_r(v)}")