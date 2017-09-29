import numpy as np
import time
from scipy.optimize import fmin
from computeX import computeX
from draw import draw
from movePoints import movePoints
import matplotlib.pyplot as plt


def folding_opt(fig, points, edges, creases, faces, rhoT, maxIter, outfile):
    size_crease = len(creases)
    w0 = 0.8
    w1 = 0.2
    w2 = 0.01
    w = w0
    D = 0.015

    rho_series = np.zeros((maxIter, size_crease))
    rho_delta = np.zeros((1, size_crease))
    rho_delta = np.reshape(rho_delta, size_crease)
    points0 = points
    crease_vect = points[creases[:, 1]]-points[creases[:, 0]]
    print(crease_vect)
    count = [1]
    draw(fig, points, edges, creases, outfile, count)
    for i in range(500):
        if np.linalg.norm(rho_delta - rhoT, 1) < 1e-2:
            print("convergence reached: err = 1e-2")
            break
        rho_rand = np.random.uniform(-np.pi, np.pi, (1, size_crease))
        rho_rand = np.reshape(rho_rand, size_crease)
        mapd = map(lambda x: -1 if x < 0 else 1, rhoT)
        rho_rand = np.array([val*rho_rand[j] for j, val in enumerate(mapd)])
        direc = (1-w)*rho_rand + w*rhoT
        rho_tau = rho_delta + D * direc
        rho = findFoldable(rho_tau, points0, creases)
        condi1 = isValid(rho)
        condi2 = (np.linalg.norm((rhoT-rho), 1) <
                  np.linalg.norm((rhoT-rho_delta), 1))
        if condi1 and condi2:
            rho_delta = rho
            w = w + w1
            rho_series[i] = rho
            points = movePoints(points0, crease_vect, faces, rho)
            draw(fig, points, edges, creases, outfile, count)
        else:
            w = w - w2
        w = max(min(w, 1), 0)
    points = movePoints(points0, crease_vect, faces, rho)
    print(rho)
    draw(fig, points, edges, creases, outfile, count)
    return rho_series


def isValid(rho):
    if True in (np.absolute(rho) > np.pi):
        return False
    else:
        return True


def findFoldable(rho_tau, points, creases):
    rho_opt = fmin(targetFunc, rho_tau, args=(points, creases), ftol=1.0e-3)
    return rho_opt


def targetFunc(rho, points, creases):
    vertices = np.unique(creases[:, 0])
    F = 0
    for i in range(vertices.size):
        X = np.identity(4)
        for j in range(len(creases)):
            if creases[j][0] == vertices[i]:
                creases_vect = points[creases[j][1]] - points[creases[j][0]]
                X = np.dot(X, computeX(creases_vect, rho[j],
                           points[vertices[i]]))
        F += np.linalg.norm((X-np.identity(4)), 1)
    return F
