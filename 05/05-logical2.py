a = 10
b = 30
c = a == 10 and b == 30
d = a == 10 or b == 50
e = not a == 20
f = not a == 10 and b == 30
g = not not a == 10 and b == 30
print(f"{c} = {a == 10} and {b == 30}, {type(c)}")
print(f"{d} = {a == 10} or {b == 50}, {type(d)}")
print(f"{e} = not {a == 20}, {type(e)}")
print(f"{f} = not {a == 10} and {b == 30}, {type(f)}")
print(f"{g} = not not {a == 10} and {b == 30}, {type(g)}")