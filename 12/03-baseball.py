import random

cnt_strike = 0
cnt_total = 0
numbers = []

rand_num = random.randint(0, 9)
for i in range(3):
    while rand_num in numbers:
        rand_num = random.randint(0, 9)
    numbers.append(rand_num)

while cnt_strike < 3:
    cnt_strike = 0
    cnt_ball = 0
    num = input("숫자 3자리를 입력하세요: ")
    if len(num) == 3:
        for i in range(3):
            for j in range(3):
                if num[i] == str(numbers[j]) and i == j:
                    cnt_strike += 1
                elif num[i] == str(numbers[j]) and i != j:
                    cnt_ball += 1
        if cnt_strike == 0 and cnt_ball == 0:
            print("아웃!!")
        else:
            output = ""
            if cnt_strike > 0:
                output += f"{cnt_strike}스트라이크"
            if cnt_ball > 0:
                output += f" {cnt_ball}볼"
            print(output)
        cnt_total += 1
print(f"{cnt_total}회 만에 성공!!")