import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("dataA.csv",delimiter=',',skiprows=1,\
        dtype={'names':('a','b','c'),'formats':(np.float64,np.float64,np.float64)})

fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_xlim(-30,30)
ax.set_ylim(-30,30)
ax.scatter(data['a'],data['b'],alpha=0.05,s=1)
#plt.show()
plt.savefig('dataA_a_b.png')
