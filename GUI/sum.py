from tkinter import *
root = Tk()
root.title("SUM")
SUM = StringVar()

def sum():
    a = float(A.get())
    b = float(B.get())
    sum = a + b
    SUM.set(str(sum))

A_text = Label(root, text="A = ")
A_text.grid(row=0, column=0)
A = Entry(root, width=30)
A.grid(row=0, column=1)
B_text = Label(root, text="B = ")
B_text.grid(row=1, column=0)
B = Entry(root, width=30)
B.grid(row=1, column=1)

Button(root, fg="white", width=10, bg="black", text="Calculate", command=lambda: sum()).grid(row=2, columnspan=2)

result_text = Label(root, text="Sum = ")
result_text.grid(row=3, column=0)
result = Entry(root, textvariable=SUM, width=30)
result.grid(row=3, column=1)

mainloop()