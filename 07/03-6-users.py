# 123456-1234567
users = []
count = 3
for i in range(count):
    name = input("사용자 이름을 입력하세요: ")
    jumin = input("주민번호를 입력하세요: ")
    jumin = jumin.replace("-", "")
    if len(jumin) == 13:
        g = jumin[6]
        if g == "1" or g == "3":
            gender = "남자"
        elif g == "2" or g == "4":
            gender = "여자"
        else:
            gender = ""
        users.append((name, gender))
print(users)