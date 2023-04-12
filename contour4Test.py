import numpy as np

CONTOUR = np.loadtxt('./data/4-contourObj.txt', dtype = int)
num4 = np.rot90(np.loadtxt('./data/4-num.txt', dtype = int))
#num2 = np.rot90(np.loadtxt('./data/2-num.txt', dtype = int))

def contourCas4(contour, num):

    nbLines = len(contour)
    nbColumns = len(contour[0])
    noeudsContour = np.zeros(shape = (1,nbLines))
    coordNoeudX = np.zeros(shape = (1,nbLines))
    coordNoeudY = np.zeros(shape = (1,nbLines))
    xDim = len(num[0]) #x axis
    yDim = len(num) #y axis

    for i in range(nbLines):
        coordNoeudX[0,i] = contour[i,0]
        coordNoeudY[0,i] = yDim - contour[i,1]
        noeudsContour[0,i] = num[contour[i,1], contour[i,0]]
        #print("x,y = [", coordNoeudX[0, i], ", ", coordNoeudY[0, i], "]")

    coordNoeudX = np.flip(coordNoeudX)
    coordNoeudY = np.flip(coordNoeudY)
    noeudsContour = np.flip(noeudsContour)

    #print("Lines", nbLines,"Columns", nbColumns, noeudsContour, "nbNoeuds:", np.shape(noeudsContour))
    #print("XCOORD flipped:", coordNoeudX, "YCOORD flipped", coordNoeudY)
    return noeudsContour, coordNoeudX, coordNoeudY

contourCas4(CONTOUR, num4)