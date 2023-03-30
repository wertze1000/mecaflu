import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse import linalg
import matplotlib.pyplot as plt

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

    laplacian = np.zeros(shape = num.shape, dtype = float)

    for i in range(len(dom[0])): #iteration sur les lignes

        for j in range(len(dom)):   #iteration sur les colonnes
             
             if(dom[i,j] == 0): #si on arrive à un zéro on skip
                continue
             
             else: #(si c'est pas un zéro)
                k, A, b = getCoeff(num[i - 1, j], num[i + 1, j], num[i, j - 1], num[i, j + 1], num[i, j], dom[i, j], cl_d[i, j])
                
                A_full = np.append(A_full, A)
                k_full = np.append(k_full, k)
                b_vec = np.append(b_vec, b)
                n_vec = np.append(n_vec, num[i, j] - 1)

                line = A #On a besoin de la taille de A
                for l in range(len(A)):
                    line[l] = num[i, j]
                
                line_full = np.append(line_full, line)

    #On organise les valeurs de b pour avoir un vecteur
    b_final = np.zeros(len(b_vec), dtype = float)
    for p in range(len(b_vec)):
        b_final[n_vec[p]] = b_vec[p]

    #On reset les indices pour que ce soit bien en matriciel
    k_full -= 1
    line_full -= 1

    A_sparse = csc_matrix((A_full, (line_full, k_full)))
    
    psi = linalg.spsolve(A_sparse, b_final)

    for i in range(len(num)):

        for j in range(len(num[0])):

            if(num[i,j] == 0):
                continue
            else:
                laplacian[i,j] = psi[num[i, j] - 1]
    return laplacian, psi

def deriv(f_left, f_c, f_right, type_left, type_c, type_right, h):
    v = 0.0
    #Formules slide 33 /!\
    if(type_c == 1): #derivée centrée
        v = (f_right - f_left)/(2 * h)
    
    elif(type_c == 2):
        if(type_right == 0): #décentrée arrière(bord droit par exemple)
            v = (f_c - f_left)/h
        else:               #décentrée avant
            v = (f_right - f_c)/h
    elif(type_c == 0):
        v = 0.0
    else:
        v = 0.0
    return v

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

def force(p,x,y):
    fx = 0.0
    fy = 0.0
    for i in range(len(x) - 1):
        fx = fx + ((x[i+1] - x[i])/2)*(p[i+1] + p[i] )
        fy = fy - ((y[i+1] - y[i])/2)*(p[i+1] + p[i] )
    return fx, fy
        
#psi de Laplace !
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

### --TEST-- ###
lap, psi = Laplace(DOM, NUM, CL_D) #(psi = lap)
print(lap)
u, v = velocity(lap, psi, DOM, NUM, 0.5)
print("V =", u,"U =", v)

### --COLORIAGE-- ###
#fig, ax0 = plt.subplots(1, 1)
#c = ax0.pcolor(lap, cmap = plt.cm.plasma)
#fig.colorbar(c, ax = ax0)
#plt.show()
