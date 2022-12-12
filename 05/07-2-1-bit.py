a = 0b0101
b = 0b0001
c = a & b
d = a | b
e = a ^ b
print(f"a={a}, b={b}, {type(a)}, {type(b)}")
print(f"{a:04b} & {b:04b} = {c:04b}")
print(f"{a:04b} | {b:04b} = {d:04b}")
print(f"{a:04b} ^ {b:04b} = {e:04b}")