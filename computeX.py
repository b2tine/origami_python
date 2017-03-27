import numpy as np

def computeX(edge, theta) :
    edge1 = edge.astype(float) / np.linalg.norm(edge, 2)
    u = edge1[0]
    v = edge1[1]
    w = edge1[2]
    X = np.array([[u**2 + (1-u**2)*np.cos(theta), u*v*(1-np.cos(theta)) - w*np.sin(theta), u*w*(1-np.cos(theta)) + v*np.sin(theta)], [u*v*(1-np.cos(theta)) + w*np.sin(theta), v**2 + (1-v**2)*np.cos(theta), v*w*(1-np.cos(theta)) - u*np.sin(theta)], [u*w*(1-np.cos(theta)) - v*np.sin(theta), v*w*(1-np.cos(theta)) + u*np.sin(theta), w**2 + (1 - w**2)*np.cos(theta)]])
    return X
     
