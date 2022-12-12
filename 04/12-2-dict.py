a = {"한국": "서울", "영국": "론돈",
    "미국": "워싱턴D.C", "독일": "베를린", 
    "영국": "런던", "북한": "평양"}
print(f"a: {a}, 개수: {len(a)}")

del a["미국"]
print(f"a: {a}, 개수: {len(a)}")

p = a.pop("북한")
print(f"a: {a}, 개수: {len(a)}")
print(f"팝업됨: {p}")

a.clear()
print(f"a: {a}, 개수: {len(a)}, 자료형: {type(a)}")