import random

def input_check(msg):
    while True:
        try:
            user_input = int(input(msg))
            return user_input
        except:
            continue

chance = 10
number = random.randint(1, 99)
print(f"1 부터 99 까지의 숫자를 {chance}번 안에 맞춰보세요.")
while chance > 0:
    chance -= 1
    user_input = input_check("숫자를 입력하세요: ")
    if number == int(user_input):
        break
    elif user_input < number:
        print(f"{user_input} 보다 큰 숫자 입니다.")
    elif user_input > number:
        print(f"{user_input} 보다 작은 숫자 입니다.")

if user_input == number:
    print(f"성공!! {user_input}이 맞습니다.")
else:
    print(f"실패!! 정답은 {number} 입니다.")