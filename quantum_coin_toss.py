from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

q = QuantumRegister(1)
c = ClassicalRegister(1)
circ = QuantumCircuit(q, c)
circ.h(q)
circ.measure(q, c)
from qiskit import BasicAer, execute

backend = BasicAer.get_backend('qasm_simulator')
job = execute(circ, backend, shots=10, memory=True)
data = job.result().get_memory()
print(data)
