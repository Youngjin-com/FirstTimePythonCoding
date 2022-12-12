money = int(input("돈이 얼마 있나요? "))
hungry = int(input("[0.배 안고픔, 1.배고픔] : "))
if money >= 20000:
    if hungry:
        print("탕수육을 먹는다")
    else:
        print("아이스크림을 먹는다")
elif money >= 8000:
    if hungry:
        print("짜장면을 먹는다")
    else:
        print("아이스 아메리카노를 먹는다")
else:
    print("굶는다")