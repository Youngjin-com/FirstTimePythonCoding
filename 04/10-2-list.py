names = []
names.append("홍길동")
names.append("이순신")
print(names)
names.insert(0, "이세종")
print(names)

names.remove("이순신")
print(names)
del names[0]
print(names)
a = names.pop(0)
print(a)
print(names)