def test():
    global b
    a = 10
    print(f"local a={a}, global b={b}")

a = 100
b = 200
test()
print(f"global a={a}, global b={b}")