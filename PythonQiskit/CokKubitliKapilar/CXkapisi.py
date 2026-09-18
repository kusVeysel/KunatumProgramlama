from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector

q = QuantumRegister(2)
qc = QuantumCircuit(q)  # Durum: |00⟩ (Qiskit sıralaması: |q1 q0⟩)

qc.x(1)  # 1. kübit (kontrol) |1⟩ yapıldı. Durum: |10⟩
qc.h(0)  # 0. kübit (hedef) süperpozisyona sokuldu. Durum: 1/√2 (|10⟩ + |11⟩)
qc.cx(1, 0)  # Kontrol kübiti (q1) |1⟩ olduğu için CNOT tetiklenir ve q0 üzerindeki |0⟩ ile |1⟩ bileşenlerini takas eder.

result = Statevector.from_instruction(qc)
print("Genlikler:", result.data)
print("Olasılıklar:", result.probabilities())

#* 1. Eleman (0.0): 00 gelme olasılığı %0
#* 2. Eleman (0.5): 01 gelme olasılığı %50  (|q1 q0⟩ = |10⟩ -⟩ indeks 2)
#* 3. Eleman (0.0): 10 gelme olasılığı %0   (|q1 q0⟩ = |01⟩ -⟩ indeks 1)
#* 4. Eleman (0.5): 11 gelme olasılığı %50  (|q1 q0⟩ = |11⟩ -⟩ indeks 3)