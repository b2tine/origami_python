import numpy as np
from computeX import computeX

def movePoints(points0, crease_vects, faces, theta) :
    (a, b) = points0.shape
    points = np.zeros((a, b))
    np.copyto(points, points0)
    old_points = np.zeros((a, b+1))
    old_points[:, 0:3] = points0
    old_points[:,3] = 1 
    for i in range(len(faces)) :
        R = np.identity(4)
	for j in range(i+1) : 
	    X = computeX(crease_vects[j], theta[j], points[faces[i][0]])
	    R = np.dot(R, X)
	for j in range(len(faces[i])) : 
	    pindex = faces[i][j]
	    points[pindex] = np.dot(R, old_points[pindex])[0:3]
    return points
