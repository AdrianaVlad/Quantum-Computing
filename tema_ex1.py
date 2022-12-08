import cmath
import numpy as np
A=[[complex(1,0),complex(1,-1),complex(3,0)],[complex(-1,1),complex(0,2),complex(2,3)],[complex(7,0),complex(5,-3),complex(9,0)]]
def dagger(A):
    Ad=A
    for i in range(len(A)):
        for j in range(len(A)):
            #Ad[j][i]=complex(A[i][j].real,-A[i][j].imag)
            Ad[i][j]=np.conj(A[i][j])
    print(Ad)
    for i in range(len(A)):
        for j in range(len(A)): 
            if(i<j):
                aux=Ad[i][j]
                Ad[i][j]=Ad[j][i]
                Ad[j][i]=aux
    return (Ad)
print(A)
print(dagger(A))