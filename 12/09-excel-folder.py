import openpyxl
import os
from datetime import datetime

def recursive_search(dir):
    results = []
    filenames = os.listdir(dir)
    for filename in filenames:
        full_path = os.path.join(dir, filename)
        if os.path.isdir(full_path):
            results.extend(recursive_search(full_path))
        else:
            access_time = os.path.getatime(full_path)
            modified_time = os.path.getmtime(full_path)
            a_time = datetime.fromtimestamp(access_time)
            m_time = datetime.fromtimestamp(modified_time)
            a_str = f"{a_time:%Y-%m-%d %H:%M:%S}"
            m_str = f"{m_time:%Y-%m-%d %H:%M:%S}"
            file_size = os.stat(full_path).st_size
            results.append((f"{full_path}", file_size, a_str, m_str))
    return results

filename = "save_excel_folder.xlsx"
target_dir = "C:\\PythonStudy"
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "폴더목록"
results = recursive_search(target_dir)
for r, d in enumerate(results):
    for c, col in enumerate(d):
        sheet.cell(r+1, c+1).value = col
wb.save(filename)
