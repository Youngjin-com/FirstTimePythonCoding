file = open("test_file.txt", "w")
file.write("안녕하세요")
file.close()

file2 = open("test_file2.txt", "w", encoding="utf-8")
file2.write("안녕하세요")
file2.close()