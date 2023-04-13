#Sur base des formules fournies, on calule la force grâce 
#à la pression en un point et les coordonés de celui-ci
def force(p,x,y):
    fx = 0.0
    fy = 0.0
    for i in range(len(x) - 1):
        fx = fx + ((y[i + 1] - y[i])/2) * (p[i + 1] + p[i] )
        fy = fy - ((x[i + 1] - x[i])/2) * (p[i + 1] + p[i] )
    return fx,fy
