import numpy as np
def norm(x,y):
    return np.sqrt(x*x + y*y)

def pressure(u,v,rho):
    p=np.zeros(len(u), dtype=float)
    for i in range(len(p)):
        p[i]=rho * 0.5 * (-norm(u[i], v[i]))*(norm(u[i], v[i]))
    return p

def pressure_field(p,NUM):
    pf = np.zeros(shape = NUM.shape, dtype = float)
    for i in range(len(NUM)):
        for j in range(len(NUM[0])):
            if(NUM[i,j]==0):
                continue
            else:
                pf[i,j]=p[NUM[i,j]-1]
    return pf