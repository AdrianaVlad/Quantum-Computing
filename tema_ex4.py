import qiskit
import qiskit_aer
from qiskit import QuantumCircuit, execute
from qiskit_aer import qasm_simulator, Aer
def circC(): # in conditiile in care starile sunt |q1q0>, nu |q0q1>, cum obisnuiam pe foaie
    circC=QuantumCircuit(2)
    circC.h(1)
    circC.x(1)
    circC.cnot(1,0)
    circC.h(0)
    return circC
circ=circC()
print(circ)
print("Matricea generata este:")
backend=Aer.get_backend('unitary_simulator')
job=backend.run(circ)
results=job.result()
U=results.get_unitary(circ,decimals=4)
print(U)