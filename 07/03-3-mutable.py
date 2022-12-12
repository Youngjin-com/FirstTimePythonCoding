def add_member(users, data):
    users.append("박길동")
    data["efgh"] = 5678
    print(users)
    print(data)

members = ["홍길동"]
data = {"abcd": 1234}
add_member(members, data)
print(members)
print(data)