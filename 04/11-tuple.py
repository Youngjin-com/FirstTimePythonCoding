a = (1, 2, 3)
b = tuple((4, 5, 6))
c = tuple([7, 8, 9])
d = (1, )
e = (1)
f = "홍길동", "이순신", "강감찬"
name1, name2, name3 = f

print(f"a: {a}, {type(a)}")
print(f"b: {b}, {type(b)}")
print(f"c: {c}, {type(c)}")
print(f"d: {d}, {type(d)}")
print(f"e: {e}, {type(e)}")
print(f"e: {f}, {type(f)}")
print(f"name1: {name1}, name2: {name2}, name3: {name3}")