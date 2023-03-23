import numpy as np
#laplace()#3 matrices DOM, NUM, CL, retourne une matrice psy

def getCoeff(num_left, num_right, num_down, num_up, num_cent, type_cent, cl_cent):
     #cefficients
    

    if(cl_cent == 1):
        A = np.array([[1],[1],[1],[1],[-4]], dtype = int)
        j = np.array([[num_left], [num_right], [num_down], [num_up], [num_cent]], dtype = int)
        b = 0
        #print("Bonsoir 1")
        #print(type(A))
        #print(A)
        #print(j)
        
        
    elif(cl_cent == 2):
        A = np.array([[1]], dtype = int)
        j = np.array([[num_cent]], dtype = int)
        b = cl_cent
        #print("Bonsoir 2")
        #print(type(A))

    elif(cl_cent == 0):
        A, j = np.zeros(1)
        b = 0
        #print("Bonsoir 3")
        
    
    return A, j, b

#getCoeff(0,0,0,0,0,0,1)