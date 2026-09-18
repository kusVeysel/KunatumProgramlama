from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector

q = QuantumRegister(3)
qc = QuantumCircuit(q)  # Durum: |000⟩ (Qiskit sıralaması: |q2 q1 q0⟩)

qc.x([1, 2])  # 1. ve 2. kübitler |1⟩ yapıldı. Durum: |110⟩
qc.h(0)  # 0. kübit (hedef) süperpozisyona sokuldu. Durum: 1/√2 (|110⟩ + |111⟩)
qc.ccx(1, 2, 0)  # Kontrol kübitleri (q1, q2) |1| olduğu için CCX tetiklenir ve q0 üzerindeki |0⟩ ile |1⟩ bileşenlerini takas eder.

result = Statevector.from_instruction(qc)
print("Genlikler:", result.data)
print("Olasılıklar:", result.probabilities())


#* 0 , ∣000⟩ , 0. , %0
#* 1 , ∣001⟩ , 0. , %0
#* 2 , ∣010⟩ , 0. , %0
#* 3 , ∣011⟩ , 0. , %0
#* 4 , ∣100⟩ , 0. , %0
#* 5 , ∣101⟩ , 0. , %0
#* 6 , ∣110⟩ , 0.5 , %50
#* 7 , ∣111⟩ , 0.5 , %50