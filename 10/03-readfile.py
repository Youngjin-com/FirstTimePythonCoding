file = open("test_file.txt", "r")
data = file.read()
file.close()
print(data)

file2 = open("test_file2.txt", "r", encoding="utf-8")
data2 = file2.read()
file2.close()
print(data2)