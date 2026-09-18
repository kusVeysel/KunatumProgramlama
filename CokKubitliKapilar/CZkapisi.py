from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector

q = QuantumRegister(2)
qc = QuantumCircuit(q)  # Durum: |00⟩ (Qiskit sıralaması: |q1 q0⟩)

qc.x(1)  # 1. kübit |1⟩ yapıldı. Durum: |10⟩
qc.h(0)  # 0. kübit (hedef) süperpozisyona sokuldu. Durum: 1/√2 (|10⟩ + |11⟩)
qc.cz(1, 0)  # Kontrol (q1) ve hedef (q0) ikisi de |1⟩ olduğunda |11⟩ durumunun genliğine -1 evresi (phase) eklenir: 1/√2 (|10⟩ - |11⟩)

result = Statevector.from_instruction(qc)
print("Genlikler:", result.data)
print("Olasılıklar:", result.probabilities())

#* 1. Eleman (0.0): 00 gelme olasılığı %0
#* 2. Eleman (0.0): 01 gelme olasılığı %0
#* 3. Eleman (0.5): 10 gelme olasılığı %50  (İndeks 2: |10⟩)
#* 4. Eleman (0.5): 11 gelme olasılığı %50  (İndeks 3: |11⟩)