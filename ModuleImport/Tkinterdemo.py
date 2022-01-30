# Tkinter Module in Python
# This module and Python provides access to the TK widget toolkit.
# It allows GUI Programs to be created.
# Tk toolkit was developed to work with scripting language called TCL and the Tkinter Python binding works by actively sending TCL code to a TCL interpreter but that's actually embedded in the python.
# Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications.
# Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit. Import the Tkinter module.
# The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit.
# Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.
# Tkinter is a pert of standard python language, so it is available without installing anything
# There are 3 different geometry managers in Tkinter - most IMP is 'grid' manager, 'pack' manager - most commonly used, 'place' manager - useful in specific situation
# 'Place' manager - works by specifying absolute positions for at least one window

# try:
import tkinter
# except ImportError: #python2
#     import Tkinter as tkinter
#
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)

tkinter._test()

# mainWindow = tkinter.Tk()
#
# mainWindow.title("Hello world ")
# mainWindow.geometry('600x800')
#
#
# label = tkinter.Label(mainWindow, text="Hello World")
# label.pack(side='top')
#
# leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side='left', anchor='n', fill=tkinter.Y, expand=False)
#
# canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
# canvas.pack(side='left', anchor='n')
#
# rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right', anchor='n', expand=True)
#
# button1 = tkinter.Button(rightFrame, text='button1')
# button2 = tkinter.Button(rightFrame, text='button2')
# button3 = tkinter.Button(rightFrame, text='button3')
# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='top')
#
# mainWindow.mainloop()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------- #


mainWindow = tkinter.Tk()

mainWindow.title("Hello world ")
mainWindow.geometry('640x480+8+200')


label = tkinter.Label(mainWindow, text="Hello World")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=1)
canvas.grid(row=1, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2, sticky='n')


button1 = tkinter.Button(rightFrame, text='button1')
button2 = tkinter.Button(rightFrame, text='button2')
button3 = tkinter.Button(rightFrame, text='button3')
button1.grid(row=0, column=0)                           # We can set sticky property to position them more accurately, it takes the same compass points as 'anchor' does when using packs, default value for sticky is centered...
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)


leftFrame.config(relief='sunken', borderwidth=1)
rightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky='ew')
mainWindow.mainloop()






























































