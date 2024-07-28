1. os
    __file__
    os.path.listdir(`dir`)
    os.path.join(`dir`, `filename`)
    os.path.abspath(__file__)
    os.path.dirname(__file__)
    os.path.splitext(`filename`)
    os.rename(`file1`, `file2`)
    os.getcwd()
    os.makedirs()
    os.exists()

2. argparse
    def get_args():
        parse = argparse.ArgumentParser(
            description="Here is the description of the script"
        )
        parse.add_argument(
            "arg_name", type=str, nargs=1, metavar="ARG", help="Here is the description of this arguemnt"
        )
        return vars(parse.parse_args())                 # vars(): Get the attributes and attribute values of an object

    def main():
        args = get _args()                              # dictionary
        print(f"args: {args["arg_name"][0]}")           # usage

3. tkinter

4. from threading import Thread
    def threading():
        # Call work function
        `thread_name` = Thread(target=`func_name`)
        `theread_name`.start()
    