import random

def random_number(numbers):
    rand_num = random.randint(1, 46)
    for i in range(len(numbers), 6):
        while rand_num in numbers:
            rand_num = random.randint(1, 45)
        numbers.append(rand_num)
    numbers.sort()

def make_lotto(**kwargs):
    lotto = []
    if kwargs.get("include"):
        include = kwargs.get("include")
        lotto.extend(include)
    if kwargs.get("exclude"):
        exclude = kwargs.get("exclude")
        while len(lotto) != 6:
            random_number(lotto)
            lotto = list(set(lotto) - set(exclude))
    if kwargs.get("continuty"):
        count = kwargs.get("continuty")
        start_num = random.randint(1, 46 - count)
        for i in range(start_num, start_num + count):
            lotto.append(i)
    random_number(lotto)
    lotto.sort()
    return lotto
print(f"로또번호 기본: {make_lotto()}")
print(f"로또번호 포함(2, 4, 6): {make_lotto(include=[2, 4, 6])}")
print(f"로또번호 제외(1~10): {make_lotto(exclude=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])}")
print(f"로또번호 연속(3): {make_lotto(continuty=3)}")
