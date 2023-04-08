def circu(u,v,x,y):
    n = len(x) #nombre d'éléments
    c = 0.0
    for i in range(n-1):
        #je fais 2 cas représentant les 2 cas de parcours d'une circulation rectangulaire:
        #déplacement horizontal
        if(y[i] == y[i + 1]):
            c = c + ((x[i + 1] - x[i])/2)*(u[i + 1] + u[i] )

        #déplacement vertical
        elif(x[i] == x[i + 1]):
            c = c + ((y[i + 1] - y[i])/2)*(v[i + 1] + v[i] )
        else:
            c = c + 0.0
    return c
