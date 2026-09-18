from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector


#? 1. PAULI-X (NOT / Bit-Flip) KAPISI
#* İşlevi: Kübitin durumunu tersine çevirir (0 -> 1, 1 -> 0).
#* Matris: [[0, 1], [1, 0]]


# X|0⟩ = |1⟩
qc = QuantumCircuit(1)
qc.x(0)
print("X|0> :", Statevector.from_instruction(qc).data)  # Çıktı: [0.+0.j, 1.+0.j]

# X|1⟩ = |0⟩
qc = QuantumCircuit(1)
qc.x(0)  # |1> durumuna getir
qc.x(0)  # Tekrar X uygula
print("X|1> :", Statevector.from_instruction(qc).data)  # Çıktı: [1.+0.j, 0.+0.j]



#? 2. PAULI-Z (Phase-Flip) KAPISI
#* İşlevi: Olasılıkları değiştirmeden sadece |1⟩ durumunun fazını ters çevirir.
#* Matris: [[1, 0], [0, -1]]


# Z|0⟩ = |0⟩
qc = QuantumCircuit(1)
qc.z(0)
print("Z|0> :", Statevector.from_instruction(qc).data)  # Çıktı: [1.+0.j, 0.+0.j]

# Z|1⟩ = -|1⟩
qc = QuantumCircuit(1)
qc.x(0)  # |1> durumuna getir
qc.z(0)
print("Z|1> :", Statevector.from_instruction(qc).data)  # Çıktı: [0.+0.j, -1.+0.j]



#? 3. PAULI-Y KAPISI
#* İşlevi: Hem bit değişimi (X) hem faz değişimi (Z) uygular.
#* Matris: [[0, -i], [i, 0]]


# Y|0⟩ = i|1⟩
qc = QuantumCircuit(1)
qc.y(0)
print("Y|0> :", Statevector.from_instruction(qc).data)  # Çıktı: [0.+0.j, 0.+1.j]

# Y|1⟩ = -i|0⟩
qc = QuantumCircuit(1)
qc.x(0)  # |1> durumuna getir
qc.y(0)
print("Y|1> :", Statevector.from_instruction(qc).data)  # Çıktı: [0.-1.j, 0.+0.j]