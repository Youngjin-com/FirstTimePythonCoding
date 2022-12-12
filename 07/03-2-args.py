def add_users(*users):
    print(users)

def add_users2(num, *users):
    print(f"num={num}, users={users}")

add_users("홍길동", "김길동", "박길동")
add_users2(1000, "홍길동", "김길동", "박길동")