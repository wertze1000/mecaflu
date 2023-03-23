import numpy as np
#getcoeff()#4 noeuds (gauche droite haut bas), renvoie une matrice de coefficients a dans un éq Ax = b
#laplace()#3 matrices DOM, NUM, CL, retourne une matrice psy

def getCoeff(num_left, num_right, num_down, num_up, num_cent, type_cent, cl_cent):
     #cefficients
    j = np.array() #phi
    b = np.array() #b
    
    if(cl_cent == 1) {
        A = np.array([[1],[1],[1],[1],[-4]])
        print(A)
        
    }
    return A, j, b