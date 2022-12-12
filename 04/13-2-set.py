a = {1, 2, 3}
print(f"집합 a: {a}")

a.add(3)
a.add(4)
print(f"add 후: {a}")

a.remove(4)
print(f"remove 후: {a}")

a.update((1, 2, 3, 4, 5))
a.update([1, 2, 3, 4, 5])
a.update({1, 2, 3, 4, 5})
print(f"update 후: {a}")