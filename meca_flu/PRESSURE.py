import numpy as np
def norm(x,y):
    return np.sqrt(x*x + y*y)

def pressure(u,v,rho):
    p=np.zeros(len(u), dtype=float)
    for i in range(len(p)):
        p[i]=rho*0.5*(norm(u[i],v[i]))*(norm(u[i],v[i]))
    return p