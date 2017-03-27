import numpy as np
from folding_opt import folding_opt
import matplotlib.pyplot as plt

points = np.loadtxt("points.txt")
creases = np.loadtxt("creases.txt", dtype=int)
edges = np.loadtxt("edges.txt", dtype=int)
rho_T = np.loadtxt("configs.txt")
rho_T *= np.pi

faces = []
infile = open("faces.txt", "r")
for line in infile : 
    face = map(int, line.split())
    faces.append(face)

fig = plt.figure()
rho_series = folding_opt(fig, points, edges, creases, faces, rho_T, 500, "test")



