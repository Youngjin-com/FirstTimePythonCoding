import os
 
def dir_list(dir):
    for d in os.scandir(dir):
        print(d.path)
        if d.is_dir():
            dir_list(d)
 
tar_dir = 'c:\\부모폴더'
dir_list(tar_dir)