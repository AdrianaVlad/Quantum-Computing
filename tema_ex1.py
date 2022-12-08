import cmath
import numpy as np
A=[[complex(1,0),complex(1,-1),complex(3,0)],[complex(-1,1),complex(0,2),complex(2,3)],[complex(7,0),complex(5,-3),complex(9,0)]]
print(type(A))
def cross(A):
    Ac=A
    for i in range(len(A)):
        for j in range(len(A)):
            #Ac[j][i]=complex(A[i][j].real,-A[i][j].imag)
            Ac[j][i]=np.conj(A[i][j])
    return Ac
print(cross(A))