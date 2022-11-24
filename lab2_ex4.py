import qiskit
import qiskit_aer
import numpy as np
from qiskit import QuantumCircuit, execute
from qiskit_aer import qasm_simulator, Aer
n=3
circuit=QuantumCircuit(n+1,n)
for qubit in range(n):
    circuit.h(qubit)
circuit.x(n)
circuit.h(n)
#poarta speciala
const_oracle = QuantumCircuit(n+1)
output = np.random.randint(2)
if output==1:
    const_oracle.x(n)
balanced_oracle = QuantumCircuit(n+1)
b_str = "101"
# Place X-gates
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        balanced_oracle.x(qubit)
# Use barrier as divider
balanced_oracle.barrier()
# Controlled-NOT gates
for qubit in range(n):
    balanced_oracle.cx(qubit, n)
balanced_oracle.barrier()
# Place X-gates
for qubit in range(len(b_str)):
    if b_str[qubit] == '1':
        balanced_oracle.x(qubit)
#poarta speciala
circuit+=balanced_oracle
for qubit in range(n):
    circuit.h(qubit)
circuit.barrier()
for i in range(n):
    circuit.measure(i, i)
print(circuit)
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circuit,shots=1024)
results=job.result()
counts=results.get_counts()
print(counts)
