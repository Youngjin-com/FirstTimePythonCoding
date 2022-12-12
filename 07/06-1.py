def is_prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

results = {True: "소수 입니다.", False: "소수가 아닙니다."}
while True:
    n = int(input("소수 검사를 할 정수를 입력하시오 : "))
    if n == 0:
        break
    print(f"입력한 수 {n}은 {results.get(is_prime_number(n))}")