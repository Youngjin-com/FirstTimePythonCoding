import openpyxl

datas = [
    ["홍길동", 100, 99, 88, 77, 66, 77, 44],
    ["김길동", 95, 93, 85, 67, 86, 63, 84],
    ["최길동", 77, 46, 78, 89, 93, 78, 98],
    ["박길동", 96, 94, 96, 95, 91, 91, 85],
    ["차길동", 87, 91, 89, 99, 95, 94, 92],
    ["구길동", 78, 83, 88, 65, 58, 72, 68],
]

filename = "save_excel.xlsx"
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "파이썬데이터"
for r, row in enumerate(datas):
    for c, data in enumerate(row):
        sheet.cell(r+1, c+1).value = data
workbook.save(filename)
