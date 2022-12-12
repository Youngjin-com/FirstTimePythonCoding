names = ["홍길동", "이순신", "이세종"]
a = names[0]
b = names[-1]
c = names[1:]
d = names[:-1]
e = names[0:2]
f = names[0:1]
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))

print(f"변경전: {names}")
names[0] = "고길동"
names[1] = "김순신"
names[2] = "박세종"
print(f"변경후: {names}")