from drawingpanel import *
panel = DrawingPanel(400, 300)
panel.canvas.create_rectangle(100, 50, 200, 200, outline="red", fill="yellow")
panel.canvas.create_oval(20, 10, 180, 70, fill="blue", outline="red")
panel.mainloop()