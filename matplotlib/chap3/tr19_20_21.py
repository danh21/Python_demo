import matplotlib.pyplot as plt
import numpy as np

# Data
x = [14,23,23,25,34,43,55,56,63,64,65,67,76,82,85,87,87,95]
y = [34,45,34,23,43,76,26,18,24,74,23,56,23,23,34,56,32,23]

# Create the plot
plt.plot(x, y, 'r-')
# r- is a style code meaning red solid line
 #Show the plot
plt.show()

#--------------------------------------------------------------
plt.plot(x, y, 'b^')
# Create blue up-facing triangles
plt.show()

#--------------------------------------------------------------
plt.plot(x, y, 'go--')
# green circles and dashed line
plt.show()

#--------------------------------------------------------------
# shuffle the elements in x
np.random.shuffle(x)
plt.plot(x, y, 'r-')
plt.show()

