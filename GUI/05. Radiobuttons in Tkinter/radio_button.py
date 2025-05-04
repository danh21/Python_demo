from tkinter import *
root = Tk()
v = IntVar()
#Label(root,text="""Choose a programming language:""", justify = LEFT,padx = 20).pack()
#Radiobutton(root, text="Python", padx = 20, variable=v, value=1).pack(anchor=W)
#Radiobutton(root, text="Perl", padx = 20, variable=v, value=2).pack(anchor=W)
v.set(1)    # initializing the choice, i.e. Python
languages = [("Python",1),("Perl",2), ("Java",3), ("C++",4), ("C",5)] 
def ShowChoice():
    print (v.get())
Label(root,text="""Choose your favourite programming language:""", justify = LEFT, padx = 20).pack()
for txt, val in languages:
    #Radiobutton(root, text=txt, padx = 20, variable=v, command=ShowChoice, value=val).pack(anchor=W)
    Radiobutton(root, text=txt, indicatoron = 0, width = 40, padx = 5, variable=v, command=ShowChoice, value=val).pack(anchor=W)
mainloop()