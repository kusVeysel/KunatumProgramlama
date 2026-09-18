from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector

q = QuantumRegister(2)
qc = QuantumCircuit(q)  # Durum: |00> (Qiskit sıralaması: |q1 q0>)

qc.x(1)  # 1. kübit |1> yapıldı. Durum: |10>
qc.h(1)  # 1. kübit süperpozisyona sokuldu. Durum: 1/√2 (|00> - |10>)
qc.swap(0, 1)  # q0 ile q1'in durumları takas edildi. Durum: 1/√2 (|00> - |01>)

result = Statevector.from_instruction(qc)
print("Genlikler:", result.data)
print("Olasılıklar:", result.probabilities())


#* 2. Eleman (0.5): 01 gelme olasılığı %50  (İndeks 1: |01>)
#* 1. Eleman (0.5): 00 gelme olasılığı %50  (İndeks 0: |00>)
#* 3. Eleman (0.0): 10 gelme olasılığı %0   (İndeks 2: |10>)
#* 4. Eleman (0.0): 11 gelme olasılığı %0   (İndeks 3: |11>)