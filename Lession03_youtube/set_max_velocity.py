import tkinter
import tkinter.messagebox

def confirmed():
    try:
        velocity = input_box.get()
        input_box.delete(0, 'end')
        velocity = int(velocity)
        if velocity <= 40:
            tkinter.messagebox.showinfo('Success!', f'{velocity}km/h is set!')
        else:
            tkinter.messagebox.showwarning('Too large!', 'The velocity should below 40km/h!')
    except Exception as e:
        tkinter.messagebox.showerror('Wrong input!', 'You need to input a number!')

root = tkinter.Tk()
root.title('rviz_gui')
root.geometry('640x360+640+360')
root.configure(bg='lightblue')
root.resizable(True, True)
label = tkinter.Label(
    root, 
    text="Set the maximum velocity",
    width=30,
    # relief='flat',
    # bd=2,
    font=('chiller', 20),
    fg='black',
    bg='lightblue')
label.place(x=80, y=60)

tkinter.Label(
    root,
    text='km/h',
    width=10,
    font=('chiller', 20),
    fg='black',
    bg='lightblue'
).place(x=500, y=100)

input_box = tkinter.Entry(
    root,
    font=('arial', 20),
    width=30)
input_box.place(x=80, y=100)

btn = tkinter.Button(
    root,
    text='confirmed',
    font=('sans-serif', 14),
    relief='raised',
    bd=2,
    command=confirmed
).place(x=80, y=140)


root.mainloop()