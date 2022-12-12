age = 30
weight = 13.5
number = 125
name = "홍길동"

a = "제 성은 %c 입니다." % name[0]
b = "제 이름은 %s 입니다." % name
c = "제 나이는 %d 살 입니다." % age
d = "몸무게는 %f kg 입니다." % weight
e = "십진수 %d 는 8진수로 %o 입니다." % (number, number)
f = "십진수 %d 는 16진수로는 %x 입니다." % (number, number)

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)