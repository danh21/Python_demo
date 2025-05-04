from tkinter import *
from tkinter.messagebox import *
def answer():
    showerror("Answer", "Sorry, no answer available")

def quit():
    if askyesno('Verify', 'Really quit?'):
        showwarning('Yes', 'Not yet implemented')
    else:
        showinfo('No', 'Quit has been cancelled')
        
Button(text='Quit', command=quit).pack(fill=X)
Button(text='Answer', command=answer).pack(fill=X)
mainloop()