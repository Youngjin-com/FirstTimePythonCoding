import os
import chardet
import argparse

TARGET_EXTS = []

def search_dir(dirname):
    results = []
    file_list = os.listdir(dirname)
    for file in file_list:
        full_path = os.path.join(dirname, file)
        if os.path.isdir(full_path):
            sub_lists = search_dir(full_path)
            results.extend(sub_lists)
        else:
            results.append(full_path)
    return results

def change_encode(tar_path):
    file_list = search_dir(tar_path)
    for file in file_list:
        filename, ext = os.path.splitext(file)
        if ext.lower() in TARGET_EXTS:
            tempfile = filename + "_tmp" + ext
            encode = {}
            with open(file, "rb") as f:
                encode = chardet.detect(f.read())
            if encode.get("encoding").lower().find("utf") < 0:
                with open(file, "r") as rfile, \
                    open(tempfile, "w", encoding="utf-8") as wfile:
                    wfile.write(rfile.read())
                os.unlink(file)
                os.rename(tempfile, file)
                print(f"{file}의 인코딩을 변경하였습니다.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, required=True, help="[대상 폴더명]")
    parser.add_argument("-e", nargs="+", help="[대상 확장자]")
    args = parser.parse_args()

    if not os.path.exists(args.f):
        print("대상 폴더가 존재하지 않습니다.")
    else:
        for e in args.e:
            if e[0:1] == ".":
                TARGET_EXTS.append(e.lower())
            else:
                TARGET_EXTS.append(f".{e.lower()}")
    change_encode(args.f)