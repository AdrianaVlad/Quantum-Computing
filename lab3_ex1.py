import qiskit
import qiskit_aer
import numpy as np
from qiskit import QuantumCircuit, execute
from qiskit_aer import qasm_simulator, Aer
n=3
s='011'
circuit=QuantumCircuit(n+1,n)
circuit.x(n)
for i in range(n):
    circuit.h(i)
circuit.h(n)
circuit.z(n)
circuit.barrier()
s=s[::-1]
for q in range(n):
    if s[q] == '0':
        circuit.i(q)
    else:
        circuit.cnot(q, n)
circuit.barrier()
for i in range(n):
    circuit.h(i)
for i in range(n):
    circuit.measure(i,i)
print(circuit)
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circuit,shots=1024)
results=job.result()
counts=results.get_counts()
print(counts)