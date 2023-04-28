import openai
import random
import argparse

OPENAI_KEY = "sk-"
openai.api_key = OPENAI_KEY

LANG = "영어"
TARGET = "7세수준의"
COUNT = 10
chance = 5

def get_word_from_gpt3(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content

def main():
    with open("prompt.txt", "r", encoding="utf-8") as f:
        prompt = f.read()
        prompt = prompt.replace("[LANG]", LANG)
        prompt = prompt.replace("[TARGET]", TARGET)
        prompt = prompt.replace("[COUNT]", str(COUNT))
        result = get_word_from_gpt3(prompt)
        words_dict = eval(result)

        words = [w for w in words_dict]
        random.shuffle(words)
        for w in words:
            for j in range(chance):
                answer = input(f"[{w}]의 영어 단어를 입력하세요> ").strip()
                eng = words_dict[w]
                if answer.lower() == eng.lower():
                    print("정답입니다.!!!")
                    break
                else:
                    message = f"틀렸습니다. {chance - (j + 1)}의 기회가 남았습니다."
                    if chance - (j + 1) <= 1:
                        print(f"{message} 힌트: {eng[0]}{eng[1]}{eng[2]} {''.join(['_' for x in range(len(eng) - 3)])}")
                    elif chance - (j + 1) <= 2:
                        print(f"{message} 힌트: {eng[0]}{eng[1]}{''.join(['_' for x in range(len(eng) - 2)])}")
                    elif chance - (j + 1) <= 3:
                        print(f"{message} 힌트: {eng[0]}{''.join(['_' for x in range(len(eng) - 1)])}")
                    elif chance - (j + 1) > 3:
                        print(f"{message}")

            if answer.lower() != eng.lower():
                print(f"정답은 {eng}입니다.")

if __name__ == "__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument("--chance", type=int, default=chance)
    parse.add_argument("--lang", type=str, default=LANG)
    parse.add_argument("--target", type=str, default=TARGET)
    parse.add_argument("--count", type=int, default=COUNT)
    args = parse.parse_args()
    
    if args.chance:
        chance = args.chance
    if args.lang:
        LANG = args.lang
    if args.target:
        TARGET = args.target
    if args.count:
        COUNT = args.count
    main()
