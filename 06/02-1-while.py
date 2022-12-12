while True:
    num1 = int(input("첫번째 수를 입력하세요: "))
    if num1 == 0:
        break
    op = input("연산자를 입력하세요: ")
    num2 = int(input("두번째 수를 입력하세요: "))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        result = 0
    print(f"결과: {num1} {op} {num2} = {result}")
print("프로그램 종료")