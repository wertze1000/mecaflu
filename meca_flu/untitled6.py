import numpy as np
import matplotlib.pyplot as plt
from LAPLACE import Laplace
from CIRCU import circu
from PRESSURE import pressure
from VELOCITY import velocity
from VELOCITY import velocity_field

NUM = np.loadtxt('./data/1-num.txt', dtype = int)
DOM = np.loadtxt('./data/1-dom.txt', dtype = int)
CL_D = np.loadtxt('./data/1-cl.txt', dtype = float)
print(CL_D)

rho= 1000

### --TEST-- ###
lap, psi = Laplace(DOM, NUM, CL_D) #(psi = lap)
print(lap)
u, v = velocity(lap, psi, DOM, NUM, 0.5)
print("U =", u,"V =", v)
print(pressure(u,v,rho))
vx, vy=velocity_field(u, v, NUM)

### --COLORIAGE-- ###
fig, ax0 = plt.subplots(1, 1)
c = ax0.pcolor(vx, cmap = plt.cm.plasma)
fig.colorbar(c, ax = ax0)
plt.show()