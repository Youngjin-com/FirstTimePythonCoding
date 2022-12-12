num = int(input("임의의 정수 입력: "))
start = 0
while start <= num:
    start += 1
    if start % 2 == 0:
        continue
    print(start)