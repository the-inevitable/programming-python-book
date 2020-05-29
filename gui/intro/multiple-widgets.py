from tkinter import *


def greeting():
    print('Hello standard output stream!')


win = Frame()
win.pack(expand=YES, fill=BOTH)

Button(win, text='Hello', command=greeting).pack(side=LEFT, fill=Y)
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, fill=X)

win.mainloop()
