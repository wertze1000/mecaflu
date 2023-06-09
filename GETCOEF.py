import numpy as np
#getCoeff sert à lire le fichier cl fourni et à l'adapter dans le but d'assigner les conditions
#correspondantes à chaque noeud
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