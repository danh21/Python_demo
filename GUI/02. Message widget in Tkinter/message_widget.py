from tkinter import *
master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'),bd = 50, fg = 'blue', relief = RIDGE)
msg.pack( )
mainloop( )