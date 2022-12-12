try:
    u = int(input("1부터 10사이의 정수를 입력하세요: "))
    if 0 >= u or u > 10:
        raise Exception
    print(f"사용자는 {u}를 입력했습니다.")
except Exception as e:
    print("입력 범위 오류!")