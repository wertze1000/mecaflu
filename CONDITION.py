import numpy as np
def cl(DOM,débit):
    CL=np.zeros(shape= DOM.shape, dtype= float)
    size_line=len(DOM[0])
    size_column=len(DOM)
    #condition horizontale
    for i in range(size_line-1):
        if(i>0 and i<size_line-1):
            CL[1][i]=débit
            CL[size_column-1][i]=0
            
    #condition verticale
    pas=débit/(size_column-3)
    for i in range(size_column-1):
        if(i>=1 and i<size_column-1):
            transform= (size_column - 1) - i - 1
            CL[i][1]=transform*pas
            CL[i][size_line-2]=transform*pas
    #condtion ilo
    for i in range(size_column):
        for j in range(size_line):
            if(j<size_line-2 and i>1 and j>1 and i<size_column-2):
                if(DOM[i][j]==2):
                   CL[i][j]=débit/2                         
    return CL

def cl4(DOM,débit):
    CL=np.zeros(shape= DOM.shape, dtype= float)
    size_line=len(DOM[0])
    size_column=len(DOM)
    #condition horizontale
    for i in range(size_line-1):
        if(i>0 and i<size_line-1):
            CL[1][i]=débit
            CL[size_column-1][i]=0
            
    #condition verticale
    pas=débit/(size_column-3)
    for i in range(size_column-1):
        if(i>=1 and i<size_column-1):
            transform= (size_column - 1) - i - 1
            CL[i][1]=transform*pas
            CL[i][size_line-2]=transform*pas
    #condtion ilo
    for i in range(size_column):
        for j in range(size_line):
            if(j<size_line-2 and i>1 and j>1 and i<size_column-2):
                if(DOM[i][j]==2):
                   CL[i][j]=débit/4                       
    return CL