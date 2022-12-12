a = 5
c = a << 1
d = a >> 1
e = (a << 1) == (a * 2)
f = (a >> 1) == (a // 2)
print(f"{a} << 1 == {c}")
print(f"{a} >> 1 == {d}")
print(f"(a << 1) == (a * 2) = {e}")
print(f"(a >> 1) == (a // 2) = {f}")