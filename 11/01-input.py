try:
    age = int(input("나이를 입력하세요: "))
    if age > 18:
        print("성인 입니다.")
except:
    print("입력 값에 문제가 있습니다.")
