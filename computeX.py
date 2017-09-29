import numpy as np


def computeX(edge, theta, vertex):
    edge1 = edge.astype(float) / np.linalg.norm(edge, 2)
    u = edge1[0]
    v = edge1[1]
    w = edge1[2]
    a = vertex[0]
    b = vertex[1]
    c = vertex[2]
    X = np.array([[u**2+(1-u**2)*np.cos(theta),
                 u*v*(1-np.cos(theta))-w*np.sin(theta),
                 u*w*(1-np.cos(theta))+v*np.sin(theta),
                 (a*(v**2+w**2)-u*(b*v+c*w))*(1-np.cos(theta)) +
                 (b*w-c*v)*np.sin(theta)],
                 [u*v*(1-np.cos(theta))+w*np.sin(theta),
                 v**2+(1-v**2)*np.cos(theta),
                 v*w*(1-np.cos(theta))-u*np.sin(theta),
                 (b*(u**2+w**2)-v*(a*u+c*w)) *
                 (1-np.cos(theta))+(c*u-a*w)*np.sin(theta)],
                 [u*w*(1-np.cos(theta))-v*np.sin(theta),
                 v*w*(1-np.cos(theta))+u*np.sin(theta),
                 w**2+(1-w**2)*np.cos(theta),
                 (c*(u**2+v**2)-w*(a*u+b*v)) *
                 (1-np.cos(theta))+(a*v-b*u)*np.sin(theta)],
                 [0, 0, 0, 1]])
    return X
