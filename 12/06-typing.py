import time

msg = "타이핑 게임 연습 문장입니다."
start_time = time.time()
user_input = input(f"{msg}\n")
end_time = time.time()
duration = end_time - start_time
correct = 0
for i, c in enumerate(user_input):
    if i >= len(msg):
        break
    if c == msg[i]:
        correct += 1
src_len = len(msg)
per_correct = correct / src_len * 100
per_error = (src_len - correct) / src_len * 100
speed = (correct / duration) * 60
print(f"속도: {speed:.2f} 정확도: {per_correct:.2f}%", end=" ")
print(f"오타율: {per_error:.2f}%")
