import sys

from tkinter import *


def quit_handler(some_arg):
    print(f'Exiting... {some_arg}')
    sys.exit()


widget = Button(None, text='Just a button', command=lambda: quit_handler('some value'))
widget.pack(expand=YES, fill=BOTH)
widget.mainloop()
