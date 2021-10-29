#_____________-HISTOGRAM PLOT-______________

import matplotlib.pyplot as plt

edges=[15,16,17,18,20,21,22,23,26,29,30,33,35]
bins=[15,20,26,30,35]

plt.hist(edges,bins,edgecolor='black')

plt.show()
