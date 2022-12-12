a = 10
b = bin(a)
c = oct(a)
d = hex(a)

print(f"10진수 {a}, {type(a)}")
print(f"2진수 bin() 결과:{b}, {type(b)}")
print(f"8진수 oct() 결과 {c}, {type(c)}")
print(f"16진수 hex() 결과 {d}, {type(d)}")
print("=" * 50)
print(f"10진수 표현 {a}")
print(f"문자열 표현(접두어):{a:#b}, (접두어X):{a:b}")
print(f"문자열 표현(접두어):{a:#o}, (접두어X):{a:o}")
print(f"문자열 표현(접두어):{a:#x}, (접두어X):{a:x}")