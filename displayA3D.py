import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data = np.loadtxt("dataA.csv",delimiter=',',skiprows=1,\
        dtype={'names':('a','b','c'),'formats':(np.float64,np.float64,np.float64)})

fig = plt.figure()
ax = fig.add_subplot( projection = '3d' )
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')
ax.set_xlim(-30,30)
ax.set_ylim(-30,30)
ax.set_zlim(-30,30)
ax.scatter(data['a'],data['b'],data['c'],alpha=0.05,s=1)
plt.show()
