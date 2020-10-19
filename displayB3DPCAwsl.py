import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

data = np.loadtxt("dataA.csv",delimiter=',',skiprows=1)

pca = PCA(n_components=3)
pca.fit(data)

print('principal component:')
print(pca.components_)

print('mean:')
print(pca.mean_)

transformedData = pca.transform(data)

fig = plt.figure()
ax = fig.add_subplot( projection = '3d' )
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')
ax.set_xlim(-30,30)
ax.set_ylim(-30,30)
ax.set_zlim(-30,30)
ax.scatter(transformedData[:,0],transformedData[:,1],transformedData[:,2],alpha=0.05,s=1)
#plt.show()
fig.savefig('dataB_pc1_pc2_pc3.png')

