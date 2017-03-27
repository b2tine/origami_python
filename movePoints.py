import numpy as np
from computeX import computeX

def movePoints(points0, crease_vects, faces, theta) :
    points = np.zeros((points0.shape))
    for i in range(len(faces)) :
	R = np.identity(3)
	for j in range(i+1) : 
	    X = computeX(crease_vects[j], theta[j])
	    R = np.dot(R, X)
	for j in range(len(faces[i])) : 
	    pindex = faces[i][j]
	    points[pindex] = np.dot(R, points0[pindex])
    return points
