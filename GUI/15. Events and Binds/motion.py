from tkinter import *
def motion(event):
    print("Mouse position: (%s %s)" % (event.x, event.y))
    return
master = Tk()
whatever_you_do = "Hover mouse around GUI and check log of terminal"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<Motion>', motion)
msg.pack()
mainloop()