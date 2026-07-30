from qiskit import QuantumCircuit,QuantumRegister,ClassicalRegister
from qiskit_aer import AerSimulator

qr = QuantumRegister(2)
cr = ClassicalRegister(2)

qc = QuantumCircuit(qr,cr)

qc.x([0,1])
qc.cz(0,1)
qc.cx(0,1)
qc.swap(0,1)
qc.h(qr)
qc.h(qr)


qc.measure(qr, cr)  # ya da qc.measure([0, 1], [0, 1])

simulator = AerSimulator()
run = simulator.run(qc, shots=1000)
print(run.result().get_counts())