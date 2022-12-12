filename = input("파일명을 입력하세요> ")
with open(filename, "w", encoding="utf-8") as f:
    while True:
        data = input()
        if data == "/bye":
            break
        f.write(data)
        f.write("\n")
print(f"{filename} 파일이 기록 되었습니다.")