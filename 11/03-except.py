try:
    age = int(input("나이를 입력하세요: "))
    ename = input("영문 이름을 입력하세요: ").encode("ascii")
except UnicodeEncodeError:
    print("이름은 영문으로 작성해야 합니다.")
except ValueError:
    print("나이를 정수 형태로 입력하세요!")
