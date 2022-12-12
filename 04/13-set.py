a = set()
b = {}
c = {1, 2, 3}
d = {1, 1, 1, 2, 2, 2, 2, 3, 3, 3}
e = set(["한국", "한국", "영국", "미국"])
f = set((1, 3, 3, 5, 5))

print(f"a: {a}, {type(a)}")
print(f"b: {b}, {type(b)}")
print(f"c: {c}, {type(c)}")
print(f"d: {d}, {type(d)}")
print(f"e: {e}, {type(e)}")
print(f"f: {f}, {type(f)}")

g = [1, 2, 3, 3, 5, 5]
g = list(set(g))
h = (1, 1, 1, 3, 3, 3)
h = tuple(set(h))
print(f"g: {g}, {type(g)}")
print(f"f: {h}, {type(h)}")