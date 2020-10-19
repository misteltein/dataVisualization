import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("dataA.csv",delimiter=',',skiprows=1)

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_xlim(-30,30)
ax.set_ylim(-30,30)
ax.scatter(data[:,0],data[:,1],alpha=0.05,s=1)
#plt.show()
fig.savefig('dataA2D_a_b.png')
