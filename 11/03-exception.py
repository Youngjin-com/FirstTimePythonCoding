try:
    age = int(input("나이를 입력하세요: "))
    ename = input("영문 이름을 입력하세요: ").encode("ascii")
except Exception as e:
    print(e)
