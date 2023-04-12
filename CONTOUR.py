import numpy as np
DOM = np.rot90(np.loadtxt('./data/1-dom.txt', dtype = int))
#(1.1) (1.3) (3.3) (3.1)

"""--------------------------------------------------------
-------------------------VALIDE----------------------------
--------------------------------------------------------"""
def contour(DOM,NUM):
    x   = np.array([], dtype = int)
    y   = np.array([], dtype = int)
    n   = np.array([], dtype = int)
    size_line=len(DOM[0])
    size_column=len(DOM)
    i_bord=0
    j_bord=0
    bord=0 #booléen pour voir si on a atteint le bord supp gauche
    for i in range(len(DOM)):
        if(bord == 1):
            break
        for j in range(len(DOM[0])):
            if(bord == 1):
                break
            if(j<size_line-2 and i>1 and j>1 and i<size_column-2):
                if(DOM[i,j]== 2):
                    bord=1
                    i_bord=i
                    j_bord=j
#bord supp
    for i in range(len(DOM[0])):
        if(DOM[i_bord,j_bord + i] == 1):
            j_bord = j_bord -1 +i
            break
        x=np.append(x,j_bord + i)
        y=np.append(y,i_bord)
        n=np.append(n,NUM[i_bord][j_bord + i])
#bord droit
    for i in range(len(DOM)):
        if(DOM[i_bord + i,j_bord] == 1):
            i_bord = i_bord -1 +i
            break
        x=np.append(x,j_bord)
        y=np.append(y,i_bord + i)
        n=np.append(n,NUM[i_bord + i][j_bord])
#bord inf
    for i in range(len(DOM[0])):
        if(DOM[i_bord,j_bord - i] == 1):
            j_bord = j_bord +1 -i
            break
        x=np.append(x,j_bord - i)
        y=np.append(y,i_bord)
        n=np.append(n,NUM[i_bord][j_bord - i])
#bord droit
    for i in range(len(DOM)):
        if(DOM[i_bord - i,j_bord] == 1):
            i_bord = i_bord +1 -i
            break
        x=np.append(x,j_bord)
        y=np.append(y,i_bord - i)
        n=np.append(n,NUM[i_bord - i][j_bord])
    
    return x,y,n
    
def contour_vitesse(n,u,v):
    uf=np.zeros(shape = n.shape, dtype = float)
    vf=np.zeros(shape = n.shape, dtype = float)
    
    for i in range(len(uf)):
        uf[i]=u[n[i]-1]
        vf[i]=v[n[i]-1]
    return uf,vf
    
    
    
        
        
                    
                    
            

    
    