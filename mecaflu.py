import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse import linalg
#laplace()#3 matrices DOM, NUM, CL, retourne une matrice psy

NUM = np.loadtxt('./data/1-num.txt', dtype = int)
DOM = np.loadtxt('./data/1-dom.txt', dtype = int)
CL_D = np.loadtxt('./data/1-cl.txt', dtype = float)

def getCoeff(num_left, num_right, num_down, num_up, num_cent, type_cent, cl_cent):
     #cefficients
    

    if(type_cent == 1):
        A = np.array([[1],[1],[1],[1],[-4]], dtype = int)
        j = np.array([[num_left], [num_right], [num_down], [num_up], [num_cent]], dtype = int)
        b = 0
        
        
    elif(type_cent == 2):
        A = np.array([[1]], dtype = int)
        j = np.array([[num_cent]], dtype = int)
        b = cl_cent
        #print(type(A))

    elif(type_cent == 0):
        A, j = np.zeros(2)
        b = 0
    else:
        A, j = np.zeros(2)
        b = 0
    
    return j, A, b

def Laplace(dom, num, cl_d):
    b_vec   = np.array([], dtype = float)
    b       = np.array([0.0], dtype = float)
    n_vec   = np.array([], dtype = int)
    n       = np.array([0], dtype = int)
    #[] pour pas avoir "built in function et dtype pour avoir des int car spare prend que Ã§a
    A_full = np.array([], dtype = int)
    k_full = np.array([],dtype = int)
    line_full = np.array([], dtype = int)
    for i in range(len(dom[0])):
        for j in range(len(dom)):
             if(dom[i,j] == 0):
                continue
             else:
                k, A, b = getCoeff(num[i - 1, j], num[i + 1, j], num[i, j - 1], num[i, j + 1], num[i, j], dom[i, j], cl_d[i, j])
                A_full = np.append(A_full, A)
                k_full = np.append(k_full, k)
                b = cl_d[i,j]
                b_vec = np.append(b_vec,b)
                n[0] = num[i,j] - 1
                n_vec = np.append(n_vec,n)
                line = A
                for l in range(len(A)):
                    line[l] = num[i,j]
                
                line_full = np.append(line_full, line)

    b_sparse = csc_matrix((b_vec, (n_vec, n_vec)))
    one = np.ones(len(b_vec))
    print(one)
    one_vert = one.reshape(len(b_vec),1)
    print(one_vert)
    b_final = csc_matrix.multiply(b_sparse, one_vert)
    print(b_final)
    k_full = k_full - 1
    line_full = line_full - 1
    A_sparse = csc_matrix((A_full, (line_full, k_full)))
    return linalg.spsolve(A_sparse, b_final)


lp=Laplace(DOM, NUM, CL_D)
print(lp)