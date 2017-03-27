import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def draw(fig, points, edges, creases, outFile, frameNum) :
    ax = fig.gca(projection='3d')
    ax.set_zlim3d(-2, 2)
    ax.set_xlim3d(-1.5, 1.5)
    ax.set_ylim3d(-1.5, 1.5)
    for i in range(len(edges)) : 
       	i1 = edges[i][0]
	i2 = edges[i][1]
	ax.plot(np.array([points[i1][0], points[i2][0]]), 
	 np.array([points[i1][1], points[i2][1]]),  
	np.array([points[i1][2], points[i2][2]]), "ro-", label="edge curve")
    
    for i in range(len(creases)) : 
	vindex = creases[i][0]
	pindex = creases[i][1]
	ax.plot(np.array([points[vindex][0], points[pindex][0]]), 
	np.array([points[vindex][1], points[pindex][1]]),  
	np.array([points[vindex][2], points[pindex][2]]), "g--", 
	label="crease curve")

    outFile = outFile + str(frameNum[0]) + ".png"
    fig.savefig(outFile)
    plt.clf()
    frameNum[0] += 1
    
    


