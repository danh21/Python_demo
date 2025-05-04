from tkinter import *
canvas_width = 600
canvas_height = 400
master = Tk()
canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack()
img = PhotoImage(file="assets\chetot.ppm")
canvas.create_image(20, 20, anchor=NW, image=img)
mainloop()