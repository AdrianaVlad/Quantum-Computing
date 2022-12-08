import cmath
import numpy as np
a=[complex(1,1),complex(2,0)]
b=[complex(3,-1),complex(-1,0)]
c=[complex(0,-2),complex(4,-2)]
def inmultire(a,b,c):
    A=[[a[0]*b[0]],[a[0]*b[1]],[a[1]*b[0]],[a[1]*b[1]]] #|ab>
    B=[np.conj(c[0]*a[0]),np.conj(c[0]*a[1]),np.conj(c[1]*a[0]),np.conj(c[1]*a[1])] #<ca|
    rezultat=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for i in range(len(A)):
        for j in range(len(B)):
            rezultat[i][j]=A[i][0]*B[j]
    return rezultat 
print(inmultire(a,b,c))