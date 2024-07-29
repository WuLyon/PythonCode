# What did you learn
## 1. os
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

## 2. argparse
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

## 3. tkinter
[tkinter_example](https://github.com/WuLyon/PythonCode/blob/main/Lession3_youtube/set_max_velocity.py)
## 4. from threading import Thread
    def threading():
        # Call work function
        `thread_name` = Thread(target=`func_name`)
        `theread_name`.start()
    
## 5. from PIL import Image, ImageDraw, ImageFont
    pip install Pillow
    image_obj = Image.open(`the path to image.jpg`)
    draw_obj = ImageDraw.Draw(image)
    font_obj = ImageFont.turetype(`the path to font.ttf`, size=`int`)  
    # C:\Windows\Fonts covers all the system fonts could be useful
    draw_obj.text(`position`, `text`, font=`font_obj`, fill=`color`)
    image_obj.save(`path`, `type`)   # "jpg" must be "jpeg"

## 6. subprocess
    subprocessCompleted_obj = subprocess.run(
            `command`,                          # Should be in the format like: ['ls', '-a']   
            shell=True,                         # Could make `command` using string directly
            check=True,                         # Check if the returncode is 0. if not, raise an error
            stdout=subprocess.PIPE,             # capture the output with the format of byte
            stderr=subprocess.PIPE,             # capture the error with the format of byte
            universal_newlines=True)            # Change the output and error from byte format into string format

    # To get the output, you need to:
    vars(subprocessCompleted_obj)['stdout']

    # To get the error, you need to:
    vars(subprocessCompleted_obj)['stderr']

    # For simple usage:
    output = subprocess.check_output(`command`, shell=True, universal_newlines=True)

More info:
    [RUNOOB.com]https://www.runoob.com/w3cnote/python3-subprocess.html
    [csdn.net]https://blog.csdn.net/qq_43331089/article/details/124421661


## Tips:
    -There are 3 way to type the path in Windows:
        r"C:\Path\to\the\file.ext"
        "C:\\path\\to\\the\\file.ext"
        "C:/path/to/the/fiile.ext"


