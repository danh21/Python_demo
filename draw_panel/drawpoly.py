from drawingpanel import *
panel = DrawingPanel(200, 200)
panel.canvas.create_polygon(100, 50, 150, 0, 150, 100, fill="green")
panel.canvas.create_line(10, 120, 20, 160, 30, 120, 40, 175)
panel.mainloop()