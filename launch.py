import sys
import os
from tkinter import filedialog
import tkinter as tk



if __name__=="__main__":
    cwd = os.getcwd()
    len_arguments = len(sys.argv)
    if len_arguments > 1:
        print(sys.argv[1])
        print(type(sys.argv[1]))
    else:
        root = tk.Tk()
        root.withdraw()
        input = filedialog.askopenfile(initialdir=cwd)
        print(input.name)

