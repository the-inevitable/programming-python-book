import sys

from tkinter import *


def quit_handler():
    print('Exiting...')
    sys.exit()


widget = Button(None, text='Just a button', command=quit_handler)
widget.pack(expand=YES, fill=BOTH)
widget.mainloop()
