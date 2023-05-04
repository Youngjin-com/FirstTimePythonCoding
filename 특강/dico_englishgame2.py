import discord
import openai
import random
from discord.ext import commands

TOKEN = "디스코드 봇 토큰"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


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


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command(name="gpt", aliases=["g"])
async def gpt(ctx, *, prompt):
    await ctx.send("챗GPT 쿼리중....")
    result = get_word_from_gpt3(prompt)
    await ctx.send(f"```{result}```")

@bot.command(name="wordgame", aliases=["wg"])
async def wordgame(ctx):

    def check_auth(m):
        return m.author == ctx.author
    
    await ctx.send("어떤 언어의 단어 퀴즈를 내겠습니까? (ex: 영어)")
    response = await bot.wait_for('message', timeout=10.0, check=check_auth)
    LANG = response.content.strip()

    await ctx.send("어떤 수준의 퀴즈를 내겠습니까? (ex: 대학교수준)")
    response = await bot.wait_for('message', timeout=10.0, check=check_auth)
    TARGET = response.content.strip()

    await ctx.send("몇개의 퀴즈를 내겠습니까? (ex: 10)")
    response = await bot.wait_for('message', timeout=10.0, check=check_auth)
    COUNT = response.content.strip()
    
    await ctx.send("챗GPT가 단어 생성중....")
    with open("prompt_new.txt", "r", encoding="utf-8") as f:
        prompt = f.read()
        prompt = prompt.replace("[LANG]", LANG)
        prompt = prompt.replace("[TARGET]", TARGET)
        prompt = prompt.replace("[COUNT]", str(COUNT))
        result = get_word_from_gpt3(prompt)
        words_dict = eval(result)

        print(words_dict)
        #k = "여러 뜻을 포함하는 자세한 한국어뜻": 
        #v = {"word": "단어", "sentence": "[LANG] 예제문장", "kor":"한글번역"},

        outbreak = False
        for k, v in words_dict.items():
            if outbreak:
                break
            for j in range(chance):
                await ctx.send(f"`[{k}]`의 영어 단어를 입력하세요> ")
                response = await bot.wait_for('message', check=check_auth)
                answer = response.content.strip()
                if answer == "bye" or answer == "quit" or answer == "exit":
                    outbreak = True
                    break
                eng = v.get("word")
                ex = v.get("sentence")
                mask = '*' * len(eng)
                kor = v.get("kor")
                ex = ex.replace(eng, mask)

                if answer.lower() == eng.lower():
                    await ctx.send("정답입니다.!!!")
                    break
                else:
                    message = f"틀렸습니다. {chance - (j + 1)}의 기회가 남았습니다."
                    if chance - (j + 1) <= 1:
                        message += f"\n\n{ex}\n({kor})\n"
                        await ctx.send(f"{message}\n힌트: {eng[0]}{eng[1]}{eng[2]} {''.join(['_' for x in range(len(eng) - 3)])}")
                    elif chance - (j + 1) <= 2:
                        message += f"\n\n{ex}\n({kor})\n"
                        await ctx.send(f"{message}\n힌트: {eng[0]}{eng[1]}{''.join(['_' for x in range(len(eng) - 2)])}")
                    elif chance - (j + 1) <= 3:
                        message += f"\n\n{ex}\n({kor})\n"
                        await ctx.send(f"{message}\n힌트: {eng[0]}{''.join(['_' for x in range(len(eng) - 1)])}")
                    elif chance - (j + 1) > 3:
                        await ctx.send(f"{message}")
            if answer.lower() != eng.lower():
                await ctx.send(f"`정답은 {eng}입니다.`")

bot.run(TOKEN)