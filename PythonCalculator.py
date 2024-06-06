# -----------kar dar kelas 1

from tkinter import Tk, Label, Entry, Button, Toplevel, IntVar, Spinbox, PhotoImage, Menu
from tkinter.ttk import Combobox, Checkbutton, Radiobutton


def plus():
    result = int(e1.get())+int(e2.get())
    lb.config(text=result)


def minus():
    result = int(e1.get())-int(e2.get())
    lb.config(text=result)


def mult():
    result = int(e1.get())*int(e2.get())
    lb.config(text=result)


def div():
    result = int(e1.get())//int(e2.get())
    lb.config(text=result)


def clean():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    lb.config(text='')


def from1_create():
    # design for form1
    frm1 = Toplevel()
    frm1.title('Form1 loading')
    frm1.geometry('300x300')
    frm1.resizable(False, False)
    frm1.config()
    frm1.iconbitmap('Generals.ico')
    # form2(labels)
    Label(frm1, text='Computer Class:').place(x=10, y=50)
    # form2(combobox)
    cmb = Combobox(frm1, values=('C++', 'C#', 'Python', 'PHP'), state='readonly')
    cmb.place(x=110, y=50)
    cmb.current(0)
    # form2(checkbutton)
    ch1 = IntVar()
    Checkbutton(frm1, text='1', variable=ch1).place(x=10, y=120)
    ch2 = IntVar()
    Checkbutton(frm1, text='2', variable=ch2).place(x=10, y=140)
    ch3 = IntVar()
    Checkbutton(frm1, text='3', variable=ch3).place(x=10, y=160)
    ch4 = IntVar()

    def selectall():
        if ch4.get():
            ch1.set(1)
            ch2.set(1)
            ch3.set(1)
        else:
            ch1.set(0)
            ch2.set(0)
            ch3.set(0)
    Checkbutton(frm1, text='Select all', command=selectall, variable=ch4).place(x=10, y=100)
    # form2(radiobutton)
    rd = IntVar()
    Radiobutton(frm1, text='Female', variable=rd, value=1).place(x=200, y=100)
    Radiobutton(frm1, text='male', variable=rd, value=2).place(x=200, y=120)
    # form2(spinbox)
    sp = IntVar()
    Spinbox(frm1, from_=1350, to=1402, textvariable=sp, state='readonly').place(x=110, y=70)
    frm1.mainloop()


# main form
frm = Tk()
frm.title('First visual programming')
frm.geometry('400x300')
frm.resizable(False, False)
frm.config(bg='#7AA082')
pic = PhotoImage(file='Pici.png')
Label(frm, image=pic).pack()
frm.overrideredirect(True)
# file menu
m = Menu(frm)
filemenu = Menu(m, tearoff=0)
m.add_cascade(label='File', menu=filemenu)
filemenu.add_cascade(label='New Form', command=from1_create)
filemenu.add_cascade(label='Open')
filemenu.add_separator()
filemenu.add_cascade(label='Save')
filemenu.add_cascade(label='Save as')
filemenu.add_separator()
filemenu.add_cascade(label='Exit', command=frm.destroy)
# help menu
helpmenu = Menu(m, tearoff=0)
m.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About us')
frm.config(menu=m)
# main form(labels)
Label(frm, text='num1:', bg='#7AA082', font=('Ariel', 14, 'bold')).place(x=20, y=160)
Label(frm, text='num2:', bg='#7AA082', font=('Ariel', 14, 'bold')).place(x=20, y=190)
lb = Label(frm, text='', bg='#7AA082', font=('Ariel', 12))
lb.place(x=105, y=220)
# main form(Entries)
e1 = Entry(frm, bg='lightyellow', font=('Ariel', 12), bd=3)
e1.place(x=110, y=160)
e2 = Entry(frm, bg='lightyellow', font=('Ariel', 12), bd=3)
e2.place(x=110, y=190)
# main form(Buttons)
Button(frm, text='Exit', bg='lightblue', command=frm.destroy).place(x=340, y=250)
Button(frm, text='delete', bg='red', fg='white', command=clean).place(x=325, y=170)
Button(frm, text='+', bg='lightpink', command=plus).place(x=20, y=250)
Button(frm, text='-', bg='lightgreen', command=minus).place(x=50, y=250)
Button(frm, text='*', bg='lightyellow', command=mult).place(x=80, y=250)
Button(frm, text='/', bg='lightblue', command=div).place(x=110, y=250)
# Button(frm, text='form1', command=from1_create).place(x=20, y=20)
frm.mainloop()
