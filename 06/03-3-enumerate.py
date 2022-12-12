txt = input("임의의 알파벳을 입력하세요: ")
cnt = 0
for pos, c in enumerate(txt):
    if c == "a":
        cnt += 1
        print(f"a 가 {cnt}번 {pos}에서 등장 했습니다.")
