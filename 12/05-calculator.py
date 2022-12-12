import os

def calculator(data):
    input_list = []
    last_operator_pos = 0
    operator = ["+", "-", "*", "/", "="]
    if data[-1] not in operator:
        data += "="
    for i, s in enumerate(data):
        if s in operator:
            input_list.append(data[last_operator_pos : i])
            input_list.append(s)
            last_operator_pos = i + 1
    while True:
        if len(input_list) == 2:
            break
        if len(input_list) > 2 and input_list[1] in operator:
            temp = input_list[0] + input_list[1] + input_list[2]
            del input_list[0:3]
            input_list.insert(0, str(eval(temp)))
            print(input_list)
    return float(input_list[0])

while True:
    os.system("cls")
    data = input("계산식 입력> ")
    if data == "/exit":
        break
    result = calculator(data)
    print(f"결과는 {result} 입니다.")
    os.system("pause")
