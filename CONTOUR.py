import numpy as np

"""--------------------------------------------------------
-------------------------VALIDE----------------------------
--------------------------------------------------------"""
def contour(DOM,NUM):
    x = np.array([], dtype = int)
    y = np.array([], dtype = int)
    n = np.array([], dtype = int)
    size_line = len(DOM[0]) #Nombre de lignes
    size_column = len(DOM)  #Nombre de colonnes
    i_bord = 0
    j_bord = 0
    bord = 0 #booléen pour voir si on a atteint le bord supp gauche
    
    for i in range(size_column):
        #print(len(DOM[0]), len(DOM))
        if(bord == 1): #Si on trouve un bord on sort
            break
        
        for j in range(size_line): #Si on trouve un bord on sort
            
            if(bord == 1):
                break
            
            if(j < size_line - 2 and i > 1 and j > 1 and i < size_column - 2):
                
                if(DOM[i, j] == 2):
                    bord = 1
                    i_bord = i
                    j_bord = j

    for i in range(size_line): #bord supp
        
        if(DOM[i_bord, j_bord + i] == 1):
            j_bord = j_bord - 1 + i
            break
        
        x = np.append(x, j_bord + i)
        y = np.append(y, i_bord)
        n = np.append(n, NUM[i_bord][j_bord + i])

    for i in range(size_column): #bord droit
        if(DOM[i_bord + i, j_bord] == 1):
            i_bord = i_bord - 1 + i
            break

        x = np.append(x, j_bord)
        y = np.append(y, i_bord + i)
        n = np.append(n, NUM[i_bord + i][j_bord])

    for i in range(size_line): #bord inf
        if(DOM[i_bord, j_bord - i] == 1):
            j_bord = j_bord + 1 - i
            break

        x=np.append(x, j_bord - i)
        y=np.append(y, i_bord)
        n=np.append(n, NUM[i_bord][j_bord - i])

    for i in range(size_column): #bord droit
        if(DOM[i_bord - i, j_bord] == 1):
            i_bord = i_bord + 1 - i
            break

        x=np.append(x, j_bord)
        y=np.append(y, i_bord - i)
        n=np.append(n, NUM[i_bord - i][j_bord])
    
    return x,y,n
    
def contour_vitesse(n, u, v):
    uf = np.zeros(shape = n.shape, dtype = float)
    vf = np.zeros(shape = n.shape, dtype = float)
    
    for i in range(len(uf)):
        
        uf[i]=u[n[i] - 1]
        vf[i]=v[n[i] - 1]
    
    return uf, vf

def contourCas4(contour, num): #Dans le sens aire à droite

    nbLines = len(contour)
    noeudsContour = np.zeros(shape = (1,nbLines), dtype = int)
    coordNoeudX = np.zeros(shape = (1,nbLines), dtype = int)
    coordNoeudY = np.zeros(shape = (1,nbLines), dtype = int)
    yDim = len(num) #y axis length

    for i in range(nbLines):
        coordNoeudX[0,i] = contour[i,0]
        coordNoeudY[0,i] = yDim - contour[i,1]
        noeudsContour[0,i] = num[contour[i,1], contour[i,0]] 
        #Recherche de la valeur du noeud dans NUM sur base des coordonnées trouvées

    return noeudsContour.flatten(), coordNoeudX.flatten(), coordNoeudY.flatten()
    
    
        
        
                    
                    
            

    
    