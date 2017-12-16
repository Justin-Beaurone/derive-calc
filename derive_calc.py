# This code was initially to test and understand the
# python gui module Tkinter. It developed into a derivative
# calculator, and is still a work in progress.

import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk
import logo

# Creates logo with random colors each time the script is run.
logo.MakeLogo()

# Calculates and displays first derivative of user input.
def derive(input):
    no_x = False
    if 'x' not in input:
        no_x = True
    if 'x' in input:
        input = input.split('x')
    if input[-1] == '':
        input.pop()
    if input[0] == '':
        input[0] = '1'
    if no_x == False:
        for i in range(len(input)):
            input[i] = input[i].strip('^')
            input[i] = float(input[i])
    if len(input) == 2:
        coeff = input[0]*input[1]
        expon = input[1] - 1
    if len(input) == 1:
        coeff = input[0]
    popup = tk.Tk()
    tframe = tk.Frame(popup, padx='100', pady='100')
    tframe.pack(side='top')
    btframe = tk.Frame(popup, width='150', height='150')
    btframe.pack(side='bottom')
    if len(input) == 2:
        if expon == 1:
            msg = tk.Message(tframe, text='First derivative: \n' \
                             +str(coeff)+'x',).pack(side='top')
        elif expon > 1:
            msg = tk.Message(tframe, text='First derivative: \n' \
                             +str(coeff)+'x^'+str(expon),).pack(side='top')
        elif expon == 0:
            msg = tk.Message(tframe, text='First derivative: \n' \
                             +str(coeff),).pack(side='top')
    if no_x == True:
        msg = tk.Message(tframe, text='First derivative: \n' \
                         +str(0),).pack(side='top')
    if len(input) == 1 and no_x == False:
        msg = tk.Message(tframe, text='First derivative: \n' \
                         +str(coeff),).pack(side='top')
    button1 = tk.Button(btframe, text='Close',
                        command=lambda: popup.destroy())
    button1.pack(side='bottom')


if __name__ == "__main__":

# This is the main window.
    window = tk.Tk()

    frame = tk.Frame(window, padx='75',pady='75')
    frame.pack(side = 'top')

    bframe = tk.Frame(window, padx='25', pady='25')
    bframe.pack(side='bottom')

    enter = tk.Entry(frame,)
    enter.pack(side='bottom')

    submit1 = tk.Button(bframe, text = 'Submit', fg = 'purple', bg = 'black',
                    command=lambda: derive(enter.get()))
    submit1.pack(side = 'left')

    quit1 = tk.Button(bframe, text='Cancel', fg = 'black', bg = 'purple',
                  command=lambda: quit())
    quit1.pack(side='right')

    logo = Image.open('logo.png')
    logo1 = ImageTk.PhotoImage(logo)
    message00 = tk.Label(frame, text='courtesy of').pack(side='top')
    message01 = tk.Label(frame, text='Justin Beaurone').pack(side='top')
    message2 = tk.Label(frame,  image = logo1,).pack(side='top')
    text_ = 'Find the derivative of a single term\n with respect to x:'
    message3 = tk.Label(frame, text=text_).pack(side='top')

    tk.mainloop()
