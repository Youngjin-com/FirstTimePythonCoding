money_units = [10000, 5000, 1000, 500, 100, 10]
money_value = []
money = int(input("금액을 만원 이상 입력하세요: "))

money_value.append(money // money_units[0])
money %= money_units[0]

money_value.append(money // money_units[1])
money %= money_units[1]

money_value.append(money // money_units[2])
money %= money_units[2]

money_value.append(money // money_units[3])
money %= money_units[3]

money_value.append(money // money_units[4])
money %= money_units[4]

money_value.append(money // money_units[5])
money %= money_units[5]

print(f"만원권: {money_value[0]}")
print(f"오천원권: {money_value[1]}")
print(f"천원권: {money_value[2]}")
print(f"오백원: {money_value[3]}")
print(f"백원: {money_value[4]}")
print(f"십원: {money_value[5]}")
