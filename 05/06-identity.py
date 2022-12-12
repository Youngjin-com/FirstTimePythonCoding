a = 10
b = 10
c = [1, 2, 3, 4, 5]
d = [1, 2, 3, 4, 5]

print(f"{a}, {id(a)}")
print(f"{b}, {id(b)}")
print(f"{c}, {id(c)}")
print(f"{d}, {id(d)}")

e = a == b
f = a is b
g = c == d
h = c is d

print(f"{e} = {a} == {b}")
print(f"{f} = {a} is {b}")
print(f"{g} = {c} == {d}")
print(f"{h} = {c} is {d}")