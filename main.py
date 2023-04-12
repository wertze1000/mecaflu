import numpy as np
import matplotlib.pyplot as plt
from LAPLACE import Laplace
from CIRCU import circu
from PRESSURE import pressure
from VELOCITY import velocity
from VELOCITY import velocity_field
from CONDITION import cl
from CONDITION import cl4
from CONTOUR import contour
from CONTOUR import contour_vitesse
from FORCE import force
from PRESSURE import pressure_field
from CONTOUR import contourCas4

#importation des matrices
NUM = np.rot90(np.loadtxt('./data/4-num.txt', dtype = int))
DOM = np.rot90(np.loadtxt('./data/4-dom.txt', dtype = int))
#CL_D = np.rot90(np.loadtxt('./data/1-cl.txt', dtype = float))
CONTOUR=np.loadtxt('./data/4-contourObj.txt', dtype = int)


#paramètres
débit = (10 * 7 + 5 * 5) * 0.1
rho = 1000
       
### --TEST-- ###
CL_D = cl4(DOM, débit)
lap, psi = Laplace(DOM, NUM, CL_D) #(psi = lap)
u, v = velocity(lap, psi, DOM, NUM, 2)
#print("U =", u,"V =", v)
#print(pressure(u,v,rho))
vx, vy, vn=velocity_field(u, v, NUM)
p = pressure(v,u,rho)
pfield = pressure_field(p,NUM)


n, x, y = contourCas4(CONTOUR,NUM)
print(n, "of shape", n.shape, "first elem", n[0])
uf, vf = contour_vitesse(n,v,u)
pf = pressure(uf, vf, rho)
fx, fy = force(pf, x, y)
print(fx, fy)


### --COLORIAGE-- ###
fig, ax0 = plt.subplots(1, 1)
c = ax0.matshow(vn, cmap = plt.cm.plasma)
ax0.set_aspect('equal','box')

### --STREAMPLOT-- ###
'''
x_grid = CL = np.zeros(shape= DOM.shape, dtype= int)
y_grid = CL = np.zeros(shape= DOM.shape, dtype= int)

for i in range(len(DOM)):
    for j in range(len(DOM[0])):
        x_grid[i, j]=i
        y_grid[i, j]=j
ax0.streamplot(y_grid, x_grid, vy, vx, color='white',density=1)
'''
fig.colorbar(c, ax = ax0)
plt.show()

