import numpy as np
from DERIV import deriv
def velocity(laplacian, psi, dom, num, h):
    u = np.zeros(len(psi))
    v = np.zeros(len(psi))

    for i in range(len(laplacian)):
        for j in range(len(laplacian[0])):
                if(num[i, j] == 0.0):
                    continue
                else:
                    v[num[i, j] - 1] = -deriv(laplacian[i - 1, j], laplacian[i, j], laplacian[i + 1, j], dom[i - 1, j], dom[i, j], dom[i + 1, j], h)
                    u[num[i, j] - 1] = deriv(laplacian[i, j - 1], laplacian[i, j], laplacian[i, j + 1], dom[i, j - 1], dom[i, j], dom[i, j + 1], h)

    return u, v

def velocity_field(u,v,num):
    U = np.zeros(shape = num.shape, dtype = float)
    V = np.zeros(shape = num.shape, dtype = float)
    for i in range(len(num)):

        for j in range(len(num[0])):

            if(num[i,j] == 0):
                continue
            else:
                U[i,j] = u[num[i, j] - 1]
                V[i,j] = v[num[i, j] - 1]
    return U, V