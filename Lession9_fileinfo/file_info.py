import sys
import os
import stat
import time

# file_name = input('Please input the file name: ')
dir = os.path.dirname(__file__)
file_name = 'data.txt'
file_path = os.path.join(dir, file_name)

line_num = 0
char_num = 0

try:
    with open(file_path) as f:
        line_num = sum(1 for line in f)
        f.seek(0)
        char_num = sum(len(line)-1 for line in f)
except Exception as e:
    print(f"!!!Error: {e}")
    sys.exit(1)

_, ext = os.path.splitext(file_name)
ext = ext[1:]

file_stat = os.stat(file_path)
file_info = {
    'name': file_name,
    'lines': line_num,
    'characters': char_num,
    'extention': ext,
    # 'size': str(file_stat[stat.ST_SIZE]) + ' bytes',
    'size': str(file_stat.st_size) + ' bytes',
    'file_atime': time.strftime('%Y/%m/%d %a %H:%M:%S', time.localtime(file_stat.st_atime)),
    'file_mtime': time.strftime('%Y/%m/%d %a %H:%M:%S', time.localtime(file_stat.st_mtime)),
    'file_ctime': time.strftime('%Y/%m/%d %a %H:%M:%S', time.localtime(file_stat.st_birthtime)),
}

print("\nHere is some infomation of this file:\n------------------------------------")
for key, value in file_info.items():
    print(f'{key}: {value}')
print("------------------------------------\n")


