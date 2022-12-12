foods = {"탕수육": 18000, "짜장면": 7000, "볶음밥": 8000}
desert = {"아이스크림": 12000, "아이스 아메리카노": 6000}

money = int(input("돈이 얼마 있나요? "))
hungry = int(input("[0.배 안고픔, 1.배고픔] "))

if hungry:
    print(foods)
    sel = input("메뉴 이름를 입력하세요 : ")
    if sel in foods:
        price = foods.get(sel)
        if money < price:
            print("가진 돈 보다 비싼 메뉴입니다.")
        else:
            print(f"{sel} 을 맛있게 먹습니다.")
            print(f"{money - price} 잔돈이 남았습니다.")
    else:
        print("존재하지 않는 메뉴명 입니다.")
else:
    print(desert)
    sel = input("메뉴 이름를 입력하세요 : ")
    if sel in desert:
        price = desert.get(sel)
        if money < price:
            print("가진 돈 보다 비싼 메뉴입니다.")
        else:
            print(f"{sel} 을 맛있게 먹습니다.")
            print(f"{money - price} 잔돈이 남았습니다.")
    else:
        print("존재하지 않는 메뉴명 입니다.")