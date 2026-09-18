 #? Tek Kübitli Kapılar(Pauli Kapılar)

from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
#! Diğer kapıların durumlarını görmek için Statevector ile doğrudan yazdırmamız gerekir

qc = QuantumCircuit(1)


#? 1. BAŞLANGIÇ DURUMU (|0⟩)
#* Kuantum bilgisayarlarda varsayılan durum |0⟩ durumudur.
#* Vektör Gösterimi: [1, 0]^T
#* Olasılıklar: |0⟩ olma olasılığı %100, |1⟩ olma olasılığı %0.
state = Statevector.from_instruction(qc)
print("Başlangıç (|0⟩):", state.data)  # Çıktı: [1.+0.j, 0.+0.j]



# 2. X (NOT / Pauli-X) KAPISI
# Klasik bilgisayarlardaki NOT kapısının kuantum karşılığıdır (Bit-Flip).
# Matris Gösterimi: [[0, 1], [1, 0]]
# İşlem: X * |0⟩ = |1⟩
# Vektör Değişimi: [1, 0]^T → [0, 1]^T
# Olasılıklar: |0⟩ olma olasılığı %0, |1⟩ olma olasılığı %100.
qc.x(0)
state = Statevector.from_instruction(qc)
print("X sonrası (|1⟩):", state.data)  # Çıktı: [0.+0.j, 1.+0.j]



# 3. Z (Pauli-Z / Phase-Flip) KAPISI
# Durumun ölçüm olasılıklarını (genliğin karesini) değiştirmez, sadece FAZINI ters çevirir.
# Matris Gösterimi: [[1, 0], [0, -1]]
# İşlem: Z * |1⟩ = -|1⟩  (Eğer durum |0⟩ olsaydı etkisiz kalırdı: Z * |0⟩ = |0⟩)
# Vektör Değişimi: [0, 1]^T → [0, -1]^T
# Olasılıklar: |-1|^2 = 1 olduğu için |1⟩ gelme olasılığı hala %100'dür, fakat fazı -1 olmuştur.
qc.z(0)
state = Statevector.from_instruction(qc)
print("Z sonrası (-|1⟩):", state.data)  # Çıktı: [0.+0.j, -1.+0.j]



# 4. Y (Pauli-Y) KAPISI
# Hem Bit-Flip (X) hem Phase-Flip (Z) işlemini birlikte uygular (Y = iXZ).
# Matris Gösterimi: [[0, -i], [i, 0]]
# İşlem: Y * (-|1⟩) = i|0⟩
#   - Matris çarpımı: [[0, -i], [i, 0]] * [0, -1]^T = [i, 0]^T
# Vektör Değişimi: [0, -1]^T → [i, 0]^T (Karmaşık düzlemde +i genliği)
# Olasılıklar: |i|^2 = 1 olduğu için durum tekrar |0⟩ konumuna döner ve gelme olasılığı %100 olur.
qc.y(0)
state = Statevector.from_instruction(qc)
print("Y sonrası (i|0⟩):", state.data)  # Çıktı: [0.+1.j, 0.+0.j]