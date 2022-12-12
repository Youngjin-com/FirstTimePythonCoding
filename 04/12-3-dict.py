caps = {"한국": "서울", "영국": "론돈",
        "미국": "워싱턴D.C", "독일": "베를린"}
keys = caps.keys()
values = caps.values()
items = caps.items()

print(keys, type(keys))
print(values, type(values))
print(items, type(items))

keys = list(caps.keys())
values = list(caps.values())
items = list(caps.items())

print(keys, type(keys))
print(values, type(values))
print(items, type(items))