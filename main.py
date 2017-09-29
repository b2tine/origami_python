import numpy as np
from folding_opt import folding_opt
import matplotlib.pyplot as plt
import sys


dirname = sys.argv[1]

points = np.loadtxt(dirname + "/points.txt")
points += 0.5
creases = np.loadtxt(dirname + "/creases.txt", dtype=int)
edges = np.loadtxt(dirname + "/edges.txt", dtype=int)
rho_T = np.loadtxt(dirname + "/configs.txt")
rho_T *= np.pi

faces = []
with open(dirname+"/faces.txt") as f:
    faces = [list(map(int, line.split())) for line in f]
if dirname == "test3":
    theta = np.linspace(0, 2*np.pi-2*np.pi/16, num=16)
    x = np.cos(theta)
    y = np.sin(theta)
    z = np.zeros((16, 1))
    x = np.reshape(x, (x.size, 1))
    y = np.reshape(y, (y.size, 1))
    z = np.reshape(z, (z.size, 1))
    points = np.append(x, y, axis=1)
    points = np.append(points, z, axis=1)
    points *= 2
    points = np.append(points, np.array([[0, 0, 0]]), axis=0)

    x = np.arange(16)
    x = np.reshape(x, (x.size, 1))
    y = np.append(np.arange(1, 16), 1)
    y = np.reshape(y, (y.size, 1))
    edges = np.append(x, y, axis=1)

    x = np.ones(16, dtype=int) * 16
    x = np.reshape(x, (x.size, 1))
    y = np.arange(16)
    y = np.reshape(y, (y.size, 1))
    creases = np.append(x, y, axis=1)

fig = plt.figure()
rho_series = folding_opt(fig, points, edges, creases,
                         faces, rho_T, 2000, "test")
