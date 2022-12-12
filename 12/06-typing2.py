import random
import time
import os

CHO = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 
        'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
JUNG = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 
        'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
JONG = ['', 'ㄱ','ㄲ','ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 
        'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ',
        'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

WORDS_LIST = [
    "한글 타자 연습 게임 만들기",
    "독도는 우리땅",
    "ord()함수는 문자의 유니코드 값을 10진수로 반환합니다.",
    "chr()함수는 십진수에 해당하는 유니코드 문자를 반환합니다."
]

def break_korean(input_data):
    break_words = []
    for c in input_data:
        if "가" <= c <= "힣":
            c_index = ord(c) - ord("가")
            c_cho = int((c_index / 28) / 21)
            c_jung = int((c_index / 28) % 21)
            c_jong = int(c_index % 28)
            break_words.append(CHO[c_cho])
            break_words.append(JUNG[c_jung])
            if c_jong > 0:
                break_words.append(JONG[c_jong])
        else:
            break_words.append(c)
    return break_words

random.shuffle(WORDS_LIST)
for q in WORDS_LIST:
    os.system("cls")
    start_time = time.time()
    input_data = input(f"{q}\n")
    duration = time.time() - start_time
    src = break_korean(q)
    tar = break_korean(input_data)
    correct = 0
    for i, c in enumerate(tar):
        if i >= len(src):
            break
        if src[i] == c:
            correct += 1
    src_len = len(src)
    per_correct = correct / src_len * 100
    per_error = (src_len - correct) / src_len * 100
    speed = (correct / duration) * 60
    
    print(f"총 글자수:{len(q)}, 타수:{src_len}, 입력타수:{len(tar)}")
    print(f"속도: {speed:.2f} 정확도: {per_correct:.2f}%", end=" ")
    print(f"오타율: {per_error:.2f}%")
    os.system("pause")
