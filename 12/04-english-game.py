import random

words_dict = {
    "사자": "lion", "호랑이": "tiger", "고양이": "cat", "사과": "apple",
    "비행기": "airplane", "동물원": "zoo", "태양": "sun", "함수": "function"
}

words = list(words_dict)
random.shuffle(words)
chance = 5
for q in words:
    for j in range(chance):
        answer = input(f"{q}에 해당하는 영어 단어를 입력하세요> ")
        english = words_dict[q]
        if answer.strip().lower() == english.lower():
            print("정답입니다!!")
            break
        else:
            print(f"틀렸습니다. {chance-(j+1)}의 기회가 남았습니다.")
    if answer != english:
        print(f"정답은 {english} 입니다.")
print("더이상 문제가 없습니다.")