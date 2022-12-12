menus = [
    ("우유", 1200),
    ("샌드위치", 6800),
    ("커피", 5500),
    ("도너츠", 3000),
    ("드립커피", 7000)
]

orders = []
while True:
    print(f"{'메뉴':-^60}")
    for i, m in enumerate(menus):
        name, price = m
        print(f"{i+1}. {name} : {price}원")
    print()
    order = int(input("주문하실 메뉴 번호를 입력하세요: "))
    cnt = int(input("수량을 입력하세요: "))
    orders.append((order, cnt))
    yn = input("더 주문하시겠습니까 (y/n)? ")
    if yn == "n":
        break

print()
print(f"{'주문정보':*^60}")
total_price = 0
for i, o in enumerate(orders):
    menu, cnt = o
    name, price = menus[menu-1]
    total_price += cnt * price
    print(f"{i+1}. {name} {cnt}개 {price}원 total:{price * cnt}원")
print(f"{'합계':=^60}")
print(f"결제 금액은 총 {total_price}원 입니다.")

while True:
    payment = int(input("지불 금액을 입력하세요: "))
    if payment > total_price:
        break
    print("지불 금액이 부족합니다.")

money_units = [10000, 5000, 1000, 500, 100, 10]
money_names = ["만원권", "오천원권", "천원권", "오백원", "백원", "십원"]
changes_value = []

changes = payment - total_price
saved_changes = changes
for mu in money_units:
    if mu <= changes:
        changes_value.append(changes // mu)
        changes %= mu
    else:
        changes_value.append(0)

print(f"거스름돈: {saved_changes} ", end="")
for i, c in enumerate(changes_value):
    if c > 0:
        print(f"{money_names[i]}: {c}", end=" ")

print()