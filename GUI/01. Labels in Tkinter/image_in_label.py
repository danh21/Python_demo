from tkinter import *
root = Tk()
logo = PhotoImage(file='assets\chelsea.png')
#w1 = Label (root,image=logo).pack(side="left")
chuoi = "Vo dich C1"
#w2 = Label (root,padx=10,text=chuoi).pack(side="right")
#w3 = Label (root,compound=CENTER,padx=10,text=chuoi,image=logo).pack()
w4 = Label(root,compound=TOP,padx=3,text=chuoi,image=logo).pack()
root.mainloop()