"""
author: Lyon
Date: 28/07/2024
Description: This script is to create a directory if it's not exist.
"""

import os
import argparse

def get_args():
    parse = argparse.ArgumentParser(
        description="This script is to create a directory if it's not exist."
    )
    parse.add_argument(
        "dir_name", type=str, nargs=1, metavar="FILE_NAME", help="The name of the directory you want to create."
    )
    return vars(parse.parse_args())

def main():
    args = get_args()
    dir_name = args["dir_name"][0]
    try:
        dir = os.path.dirname(__file__)
        if not os.path.exists(
            os.path.join(dir, dir_name)
        ):
            os.makedirs(
                os.path.join(dir, dir_name)
            )
            print("Create sucessfully!")
        else:
            print("The directory is already exist.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()