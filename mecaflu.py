import numpy as np
from scipy.sparse import csc_matrix
#laplace()#3 matrices DOM, NUM, CL, retourne une matrice psy

NUM = np.loadtxt('./data/1-num.txt', dtype = int)
DOM = np.loadtxt('./data/1-dom.txt', dtype = int)
CL_D = np.loadtxt('./data/1-cl.txt', dtype = int)

def getCoeff(num_left, num_right, num_down, num_up, num_cent, type_cent, cl_cent):
     #cefficients


    if(type_cent == 1):
        A = np.array([[1],[1],[1],[1],[-4]], dtype = int)
        j = np.array([[num_left], [num_right], [num_down], [num_up], [num_cent]], dtype = int)
        b = 0
        print(A)
        print(j)


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
    length_b = (len(dom) - 2)*(len(dom[0]) - 2)
    b_vec = np.zeros(length_b + 1)

    for i in range(len(dom[0])):
        for j in range(len(dom)):
            if(dom[i,j] == 0):
                continue
            else:
                A_full = []
                k_full = []
                line_full = []

                k, A, b = getCoeff(num[i - 1, j], num[i + 1, j], num[i, j - 1], num[i, j + 1], num[i, j], dom[i, j], cl_d[i, j])
                A_full.append(A)
                k_full.append(k)
                line = A

                b_vec[num[i,j]] = cl_d[i,j]
                for l in range(len(A[0])):
                    line[l] = num[i,j]

                line_full.append(line)

    print(A_full, k_full, line_full)
    A_sparse = csc_matrix((A_full, (line_full, k_full)))
    print(A_sparse)
    return A_sparse

Sparse = Laplace(DOM, NUM, CL_D)