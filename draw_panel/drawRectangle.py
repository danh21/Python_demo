from drawingpanel import *
panel = DrawingPanel(400, 300)
panel.set_background("yellow")
panel.canvas.create_rectangle(100, 50, 200, 300)
panel.mainloop()