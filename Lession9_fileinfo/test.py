import sys
import os
import stat
import time

# file_name = input('Please input the file name: ')
file_name = 'data'

line_num = 0
char_num = 0

try:
    with open(file_name) as f:
        line_num = sum(1 for line in f)
        f.seek(0)
        char_num = sum(len(line)-1 for line in f)
except Exception as e:
    print(f"!!!Error: {e}")
    sys.exit(1)

file_stat = os.stat(file_name)
file_size = file_stat[stat.ST_SIZE]
file_mtime = file_stat[stat.ST_CTIME]
print(file_mtime)
print(time.ctime(file_mtime))
print(time.localtime(file_mtime))
print(time.strftime('%d/%m/%Y %a %H:%M:%S', time.localtime(file_mtime)))