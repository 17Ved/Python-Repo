# Parabola is a very interesting shape
# Parabolic reflectors can be used to focus light or sound and are also used to focus the satellite signals used for modern TV broadcast.
# 'canvas' - The Canvas is a rectangular area intended for drawing pictures or other complex layouts. You can place graphics, text, widgets or frames on a Canvas.
# canvas coordinate system has 00 at the top left
# 'Scope' - The location where we can find a variable and also access it if required is called the scope of a variable.
# Global Variable - Global variables are the ones that are defined and declared outside any function and are not specified to any function.
#                               They can be used by any part of the program.
# Local Variable -
import math
try:
    import tkinter

except ImportError:     # python 2
    import Tkinter as tkinter


def parabola(canvas, size):
    for x in range(size):           # -size
        y = x * x / size
        plot(canvas, x, y)
        plot(canvas, -x, y)


def circle(page, radius, g, h, colour="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=colour, width=2)
    # for x in range(g * 100, (g + radius) * 100):
    #     x /= 100
    #     print(x)
    #     y = h + (math.sqrt(radius ** 2 - ((x-g) ** 2)))
    #     plot(page, x, y)
    #     plot(page, x, 2 * h - y)
    #     plot(page, 2 * g - x, y)
    #     plot(page, 2 * g - x, 2 * h - y)


def draw_axes(canvas):                              # 1st is to draw the 'axis' function
    canvas.update()                             # update() function make sure that we can actually access width and height.
    x_origin = canvas.winfo_width() / 2               # Now the function just divides those values by 2 to get the values for the 'X' origin
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))           # 'scroll region' is just a box with one corner at minus x origin & minus y origin
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")                     # Here we are drawing a horizontal line for the 'x' axis and vertical line for 'y' axis
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, y + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("parabola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

# canvas2 = tkinter.Canvas(mainWindow, width=320, height=480, background="blue")
# canvas2.grid(row=0, column=1)


# print(repr(canvas), repr(canvas2))              # The repr() function returns the string representation of the value passed to eval function by default.
draw_axes(canvas)                               # So when we call the draw_axes() function we're going to reposition the canvases origin and draw the 'x' & 'y' axes on the canvas.
# draw_axes(canvas2)

parabola(canvas, 100)
parabola(canvas, 200)
circle(canvas, 100, 100, 100, "green")
circle(canvas, 100, 100, -100, "yellow")
circle(canvas, 100, -100, 100, "black")
circle(canvas, 100, -100, -100, "blue")
circle(canvas, 10, 30, 30)
circle(canvas, 10, 30, -30)
circle(canvas, 10, -30, 30)
circle(canvas, 10, -30, -30)
circle(canvas, 30, 0, 0)


# for x in range(-100, 100):
#     y = parabola(x)
#     plot(canvas, x, -y)

mainWindow.mainloop()

































































