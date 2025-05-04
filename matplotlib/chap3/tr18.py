import matplotlib.pyplot as plt

# Data
x = [0,1,2,3,4,5,6,7,8,9]
y1 = [10,20,40,55,58,55,50,40,20,10]
y2 = [20,30,50,77,82,77,75,68,65,60]

# Shade the area between y1 and y2
plt.fill_between(x, y1, y2, 
                #facecolor='red', # The fill color
                color='orange', # The outline color
                alpha=0.2) # Transparency of the fill

# Show the plot
plt.show()