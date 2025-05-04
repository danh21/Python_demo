import matplotlib.pyplot as plt
import numpy as np
# generate 1000 data points with normal distribution
data = np.random.randn(1000)
plt.hist(data)
plt.show()