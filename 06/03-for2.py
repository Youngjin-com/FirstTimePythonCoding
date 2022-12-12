txt = input("알파벳 문자열을 입력하세요.: ")
result = {}
for t in txt:
    if result.get(t) is None:
        result[t] = 1
    else:
        result[t] += 1
print(result)