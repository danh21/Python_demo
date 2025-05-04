import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([2.], [3.], 'bo')
plt.text( # position text relative to data
    2., 3., 'important point', # x, y, text,
    ha='center', va='bottom', # text alignment,
    transform=ax.transData # coordinate system transformation
)
plt.text( # position text relative to Axes
    1.0, 1.0, 'axes corner',
    ha='right', va='top',
    transform=ax.transAxes
)
plt.text( # position text relative to Figure
    0.0, 1.0, 'figure corner',
    ha='left', va='top',
    transform=fig.transFigure
)
plt.text( # position text absolutely at specific pixel on image
    200, 300, 'pixel (200, 300)',
    ha='center', va='center',
    transform=None
)
plt.show()