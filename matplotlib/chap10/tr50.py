import matplotlib.pyplot as plt
fig = plt.figure('image')
#fig = plt.figure()
ax = plt.subplot(3, 2, 1) # 3 rows, 2 columns, the first subplot
fig, (ax1, ax2) = plt.subplots(ncols=2, nrows=1) # 1 row, 2 columns
plt.show()