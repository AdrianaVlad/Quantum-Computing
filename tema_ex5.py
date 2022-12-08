import qiskit
import cmath
import math
from math import sqrt
from qiskit import QuantumCircuit
import numpy as np
a=[complex(1,0),complex(0,0),complex(0,0),complex(0,0)]
def entangled(x):
    #is entangled return "TRUE", else return "FALSE"
    #verificam probabilitatile
    a=round(abs(x[0])*abs(x[0]),2)
    b=round(abs(x[1])*abs(x[1]),2)
    c=round(abs(x[2])*abs(x[2]),2)
    d=round(abs(x[3])*abs(x[3]),2)
    p00=a+b
    p01=c+d
    p10=a+c
    p11=b+d
    print(a,b,c,d)
    if((p00*p10!=a)or(p00*p11!=b)or(p01*p10!=c)or(p01*p11!=d)):
        return "TRUE"
    return "FALSE"
print(entangled(a))
