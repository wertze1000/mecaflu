def force(p,x,y):
    fx = 0.0
    fy = 0.0
    for i in range(len(x) - 1):
        fx = fx + ((x[i+1] - x[i])/2)*(p[i+1] + p[i] )
        fy = fy - ((y[i+1] - y[i])/2)*(p[i+1] + p[i] )
    return fx, fy