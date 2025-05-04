import matplotlib.pyplot as plt
# Data
x = [21, 34, 44, 23]
y = [435, 334, 656, 1999]
labels = ["alice", "bob", "charlie", "diane"]

# Create the figure and axes objects
fig, ax = plt.subplots(1, figsize=(10, 6))
fig.suptitle('Example Of Labelled Scatterpoints')

# Plot the scatter points
ax.scatter(x, y,
        color="blue", # Color of the dots
        s=100, # Size of the dots
        alpha=0.5, # Alpha of the dots
        linewidths=1) # Size of edge around the dots

# Add the participant names as text labels for each point
for x_pos, y_pos, label in zip(x, y, labels):
    ax.annotate(label, # The label for this point
                xy=(x_pos, y_pos), # Position of the corresponding point
                xytext=(7, 0), # Offset text by 7 points to the right
                textcoords='offset points', # tell it to use offset points
                ha='left', # Horizontally aligned to the left
                va='center') # Vertical alignment is centered

# Show the plot
plt.show()