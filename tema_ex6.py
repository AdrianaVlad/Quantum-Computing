import qiskit
import qiskit_aer
import math
from math import pi,sqrt,acos
from qiskit import QuantumCircuit, transpile, execute
from qiskit_aer import qasm_simulator, Aer
import numpy as np
circ=QuantumCircuit(3)
circ.ry(2*(acos(1/sqrt(3))),0)
circ.ch(0,1)
circ.cx(1,2)
circ.cx(0,1)
circ.x(0)
#circ.p(4*pi/3,1) circ.p(2*pi/3,0) pt cealalta stare (0)
#aici: starea 1
circ.p(2*pi/3,1)
circ.p(4*pi/3,0)
print(circ)
#circ.barrier()
#am terminat de construit qbitul
backend = Aer.get_backend('statevector_simulator')
job = execute(circ, backend=backend, shots=1, memory=True)
job_result = job.result()
stare=job_result.get_statevector(circ)
for i in range(len(stare)):
    if(stare[i].real<0.005 and stare[i].real>-0.005):
        print(0)
    else:
        print(round(stare[i],4))
#optional: masuram
circ.measure_all()
simulator=Aer.get_backend('qasm_simulator')
job=simulator.run(transpile(circ,backend=simulator),shots=1000)
results=job.result()
counts=results.get_counts()
print(counts)
#rezultatul final:
if(round(stare[1].imag,4)<0):
    print("Rezultatul final: stare 1")
else:
    print("Rezultatul final: stare 0")
