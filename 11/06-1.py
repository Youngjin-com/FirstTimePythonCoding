def mycasting(msg, vtype=str):
    while True:
        try:
            user_data = vtype(input(msg))
            return user_data
        except:
            print("잘못된 입력입니다.")
            continue

n = mycasting("숫자를 입력하세요: ", int)
print(f"입력된 숫자는 {n} 입니다.")
f = mycasting("실수를 입력하세요: ", float)
print(f"입력된 실수는 {f} 입니다.")
l = mycasting("리스트 요소를 입력하세요: ", list)
print(f"입력된 리스트는 {l} 입니다.")