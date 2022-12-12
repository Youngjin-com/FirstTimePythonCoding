with open("애국가.txt", "r", encoding="utf-8") as source, \
    open("애국가_복사.txt", "w", encoding="utf-8") as target:
    for line in source:
        target.write(line)
