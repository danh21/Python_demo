import matplotlib.pyplot as plt
# Data
x = [0,1,2,3,4,5,6,7,8,9]
y1 = [10,20,40,55,58,55,50,40,20,10]

# Shade the area between y1 and line y=0
plt.fill_between(x, y1, 0,
                #facecolor="blue", 
                color="orange", 
                alpha=0.2) # Transparency of the fill

# Show the plot
plt.show()