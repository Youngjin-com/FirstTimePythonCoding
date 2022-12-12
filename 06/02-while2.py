txt = input("알파벳 문자열을 입력하세요.: ")
result = {}
while len(txt) > 0:
    if result.get(txt[0]) is None:
        result[txt[0]] = 1
    else:
        result[txt[0]] += 1
    txt = txt[1:]
print(result)