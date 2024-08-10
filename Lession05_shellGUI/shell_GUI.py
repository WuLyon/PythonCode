'''
This script is able to list all the files and directory by giving a path with a GUI interface.
Notice: Only for Linux
'''
import subprocess
import os
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("List Directory GUI")
root.geometry('500x250+1000+500')
root.resizable(True, True)

def run_shell():
    try:
        dir_path =  input_box.get()
        shell_path = os.path.join(os.path.dirname(__file__), 'show_files.sh')
        input_box.delete(0, 'end')
        # output = subprocess.check_output(f"bash {shell_path} {dir_path}", shell=True, universal_newlines=True)
        output_obj = subprocess.run(
            f"bash {shell_path} {dir_path}", 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE, 
            universal_newlines=True)
        print(output_obj)
        output = vars(output_obj)['stdout']
        error = vars(output_obj)['stderr']
        if error == '':
            print(output)
            tkinter.messagebox.showinfo(dir_path, output)
        else:
            print(error)
            tkinter.messagebox.showerror(dir_path, error)
    except Exception as e:
        print(e)
    return 0

tkinter.Label(
    root,
    text="directory:"
).place(x=50, y=30)

input_box = tkinter.Entry(
    root,
    width=50
)
input_box.place(x=50, y=60)

btn = tkinter.Button(
    root,
    text='confirmed',
    command=run_shell
)
btn.place(x=50, y=90)

root.mainloop()