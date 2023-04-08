import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse import linalg
import matplotlib.pyplot as plt
import GETCOEF
from GETCOEF import getCoeff


def Laplace(dom, num, cl_d):

    b_vec   = np.array([], dtype = float) #float!
    n_vec   = np.array([], dtype = int)
    
    A_full = np.array([], dtype = int) #[] pour pas avoir "built in function" et dtype pour avoir des int car sparse prend que int.
    k_full = np.array([],dtype = int)
    line_full = np.array([], dtype = int)

    laplacian = np.zeros(shape = num.shape, dtype = float)

    for i in range(len(dom)): #iteration sur les lignes

        for j in range(len(dom[0])):   #iteration sur les colonnes
             
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

