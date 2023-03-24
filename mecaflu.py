import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse import linalg

NUM = np.loadtxt('./data/1-num.txt', dtype = int)
DOM = np.loadtxt('./data/1-dom.txt', dtype = int)
CL_D = np.loadtxt('./data/1-cl.txt', dtype = float)

def getCoeff(num_left, num_right, num_down, num_up, num_cent, type_cent, cl_cent):

    if(type_cent == 1):
        A = np.array([[1], [1], [1], [1], [-4]], dtype = int)
        j = np.array([[num_left], [num_right], [num_down], [num_up], [num_cent]], dtype = int)
        b = 0
        
    elif(type_cent == 2):
        A = np.array([[1]], dtype = int)
        j = np.array([[num_cent]], dtype = int)
        b = cl_cent

    elif(type_cent == 0):
        A, j = np.zeros(2)
        b = 0
    else:
        A, j = np.zeros(2)
        b = 0
    
    return j, A, b

def Laplace(dom, num, cl_d):

    b_vec   = np.array([], dtype = float) #float!
    n_vec   = np.array([], dtype = int)
    
    A_full = np.array([], dtype = int) #[] pour pas avoir "built in function" et dtype pour avoir des int car sparse prend que int.
    k_full = np.array([],dtype = int)
    line_full = np.array([], dtype = int)
    
    for i in range(len(dom[0])): #iteration sur les lignes

        for j in range(len(dom)):   #iteration sur les colonnes
             
             if(dom[i,j] == 0): #si on arrive à un zéro on skip
                continue
             
             else: #(si c'est pas un zéro)
                k, A, b = getCoeff(num[i - 1, j], num[i + 1, j], num[i, j - 1], num[i, j + 1], num[i, j], dom[i, j], cl_d[i, j])
                
                A_full = np.append(A_full, A)
                k_full = np.append(k_full, k)
                b_vec = np.append(b_vec, b)
                n_vec = np.append(n_vec, num[i,j] - 1)

                line = A #On a besoin de la taille de A
                for l in range(len(A)):
                    line[l] = num[i,j]
                
                line_full = np.append(line_full, line)

    #On organise les valeurs de b pour avoir un vecteur
    b_final = np.zeros(len(b_vec), dtype = float)
    for p in range(len(b_vec)):
        b_final[n_vec[p]] = b_vec[p]

    #On reset les indices pour que ce soit bien en matriciel
    k_full -= 1
    line_full -= 1

    A_sparse = csc_matrix((A_full, (line_full, k_full)))
    
    return linalg.spsolve(A_sparse, b_final)


lp = Laplace(DOM, NUM, CL_D)
print(lp)

def deriv(f_left, f_c, f_right, type_left, type_c, type_right, h):
    v=0.0
    if(type_c == 1): #derivée centré
        v=(f_right - f_left)/(2*h)
    
    elif(type_c == 2):
        if(type_right == 0): #décentrée arrière(bord droit par exemple)
            v=(f_c - f_left)/h
        else:               #décentrée avant
            v=(f_right - f_c)/h
    elif(type_c == 0):
        v=0.0
    else:
        v=0.0
    return v

def circu(u,v,x,y):
    n=len(x) #nombre d'éléments
    c=0.0
    for i in range(n-1):
#je fais 4 cas représentant les 4 cas de parcours d'une circulation rectangulaire
        #(0,0) -> (1,0)  vers là droite
        if(x[i] < x[i+1] and y[i] == y[i+1]):
            c = c + ((x[i+1] - x[i])/2)*(u[i+1] + u[i] )
        #(1,1) -> (0,1) vers la gauche
        elif(x[i] > x[i+1] and y[i] == y[i+1]):
            c = c - ((x[i] - x[i+1])/2)*(u[i+1] + u[i] )
        #(0,1) -> (0,0) vers le bas 
        elif(x[i] == x[i+1] and y[i] > y[i+1]):
            c = c - ((y[i] - y[i+1])/2)*(v[i+1] + v[i] )
        #(1,0) -> (1,1) vers le haut
        elif(x[i] == x[i+1] and y[i] < y[i+1]):
            c = c + ((y[i+1] - y[i])/2)*(v[i+1] + v[i] )
        else:
            c= c +0.0
    return c

