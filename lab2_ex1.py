import qiskit
import qiskit_aer
from qiskit import QuantumCircuit, execute
from qiskit_aer import qasm_simulator, Aer
circuit = QuantumCircuit(3)
circuit.measure_all()
circuit.x(0)
print(circuit)
circuit.measure_all()
backend=Aer.get_backend('qasm_simulator')
job=backend.run(circuit,shots=1024)
results=job.result()
counts=results.get_counts()
print(counts)