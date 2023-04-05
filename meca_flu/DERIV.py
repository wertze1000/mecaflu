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