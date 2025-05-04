import matplotlib.pyplot as plt
# Data
x = [43,76,34,63,56,82,87,55,64,87,95,23,14,65,67,25,23,85]
y = [34,45,34,23,43,76,26,18,24,74,23,56,23,23,34,56,32,23]
fig, ax = plt.subplots(1, figsize=(10, 6))
fig.suptitle('Example Of Scatterplot')

# Create the Scatter Plot
ax.scatter(x, y,
        color="blue", # Color of the dots
        s=100, # Size of the dots
        alpha=0.5, # Alpha/transparency of the dots (1 is opaque, 0 is transparent)
        linewidths=1) # Size of edge around the dots

# Show the plot
plt.show()