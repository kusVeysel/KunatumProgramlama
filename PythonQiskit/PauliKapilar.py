from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
#! diğer kapıları görmek için doğrudan yazdırmamız gerekir

qc = QuantumCircuit(1)

state = Statevector.from_instruction(qc)
print(state.data)  # Kübit 0 olarak başlar

qc.x(0)  # Durumu |1> yap
state = Statevector.from_instruction(qc)
print(state.data) 

qc.z(0)  # Z kapısı uygula -> -|1> olur
state = Statevector.from_instruction(qc)
print(state.data) 

qc.y(0) # Y kapısı uygula -> j
state = Statevector.from_instruction(qc)
print(state.data) 
