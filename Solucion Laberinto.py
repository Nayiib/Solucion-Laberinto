# Nayib Moreno - 20152020401

import numpy as np
from io import StringIO

# apertura del archivo "laberinto"
pfile=open('laberinto','r')
# lectura del archivo 
data=pfile.read()
# cierre de archivo 
pfile.close()
# lectura de espacios en archivo 
data=np.genfromtxt(StringIO(data), delimiter  = ' ' )

dim= list(data.shape)
fil=dim[0]
col=dim[1]
sup=0
izq=0
der=col
inf=fil
recorrido=[]
 
print(data)
print(fil)
print(col) 

while sup < inf or izq < der :
    i=inf-1
    j=der-1
    
    while j>izq:
        recorrido.append(data[i][j])
        j=j-1
    
    while i>sup:
        recorrido.append(data[i][j])
        i=i-1
        
    while j<der-1:
        recorrido.append(data[i][j])
        j=j+1   
    
    while i<inf-1:
        recorrido.append(data[i][j])
        i=i+1
    
    izq=izq+1
    sup=sup+1
    der=der-1
    inf=inf-1


print(recorrido)      