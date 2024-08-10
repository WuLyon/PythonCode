"""
author: Lyon
Date: 28/07/2024
Description: This python script is able to change extensions of all the files in the directory where this script is situated.
"""

import os
import argparse

def get_args():
    parse = argparse.ArgumentParser(
        description="This python script is able to change extensions of all the files in the directory where this script is situated."
    )
    parse.add_argument(
        "ext", type=str, nargs=1, metavar="EXT", help="The new extension you want to use."
    )
    return vars(parse.parse_args())

def ext_change(ext):
    if ext[0] != '.':
        ext = '.' + ext
    dir = os.path.dirname(__file__)
    count = 0
    for file in os.listdir(dir):
        name, old_ext = os.path.splitext(file)
        if old_ext != '.py':
            new_file = name + ext
            os.rename(os.path.join(dir, file), os.path.join(dir, new_file))
            count += 1

    print(f"Done! {count} files extension is been changed!")
    for file in os.listdir(dir):
        print(file)

def main():
    args = get_args()
    ext_change(args["ext"][0])

if __name__ == "__main__":
    main()