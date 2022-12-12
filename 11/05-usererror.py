class NumberCheckError(Exception):
    def __init__(self, msg="Error"):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    num = int(input("숫자를 입력하세요: "))
    if num < 0:
        raise NumberCheckError("0보다 작습니다.")
except NumberCheckError as e:
    print(e)