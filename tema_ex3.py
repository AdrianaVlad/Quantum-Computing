import qiskit
import qiskit_aer
from qiskit import QuantumCircuit, execute
from qiskit_aer import qasm_simulator, Aer
from qiskit.visualization import plot_histogram
import numpy as np
from numpy import linalg
    #a)
circ1=QuantumCircuit(2)
circ1.cnot(0,1) #circ.cx(1)
circ1.h(0)
print(circ1)
    #b)
backend=Aer.get_backend('unitary_simulator')
job=backend.run(circ1)
results=job.result()
U=results.get_unitary(circ1,decimals=4)
U=np.matrix(U)
print("Matricea U =",U)
Uc=np.matrix(np.conj(np.transpose(U)))
t1=(round(np.linalg.norm(U*Uc-Uc*U),4))
print("||U*Uc-Uc*U|| = ", t1, " (if=0, U*Uc=Uc*U)")
I=np.identity(4)
t2=(round(np.linalg.norm(Uc*U-I),4))
print("||Uc*U-I4|| = ", t2, " (if=0, Uc*U=I4)")
if t1==0 and t2==0:
    print("U este unitara")
else:
    print("Error: U nu e unitara")
    #c)
circ2=circ1
circ2.measure_all()
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circ2,shots=1000)
results=job.result()
counts=results.get_counts()
print("Masurare qasmsimulator: ")
print(counts)
plot_histogram(counts).savefig('histograma.png')
    #d)
def pr_bell(circ):
    circ.h(0)
    circ.cnot(0,1) # am general starea bell corespunzatoare
    circ+=circ2 # adaugam circuitul de masurare
    backend=Aer.get_backend('qasm_simulator')
    job=backend.run(circ,shots=1000)
    results=job.result()
    counts=results.get_counts()
    probs = {string:count/1000 for string,count in counts.items()}
    print(probs)
print("Pentru input 00 avem:")
bell=QuantumCircuit(2)
pr_bell(bell)
print("Pentru input 01 avem:")
bell=QuantumCircuit(2)
bell.x(0)
pr_bell(bell)
print("Pentru input 10 avem:")
bell=QuantumCircuit(2)
bell.x(1)
pr_bell(bell)
print("Pentru input 11 avem:")
bell=QuantumCircuit(2)
bell.x(0)
bell.x(1)
pr_bell(bell) 
