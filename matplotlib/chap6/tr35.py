# import matplotlib.pyplot as plt
# plt.plot([0, 1], [0, 1])
# plt.close()

# --------------------------------

import matplotlib.pyplot as plt
fig1 = plt.figure(1) # create first figure
plt.plot([0, 1], [0, 1])
fig2 = plt.figure(2) # create second figure
plt.plot([0, 1], [0, 1])
plt.close(fig1) # close first figure although second one is active
plt.show()