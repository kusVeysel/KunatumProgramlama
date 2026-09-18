
#? Amaç
#* Uniter bir U operatörünün ve onun ∣ψ⟩ özvektörünün verildiği durumda, U∣ψ⟩=e^(2πiθ)∣ψ⟩ denklemindeki bilinmeyen θ ∈ [0,1) faz değerini bulmaktır.

#todo 1.Adım Hazırlık
#? Hesaplama Kayıdı (Counting Register): n adet kübit ∣0⟩^⊗n durumunda başlatılır. (Kübit sayısı n, hassasiyeti belirler).
#? Hedef Kayıt (Target Register): Özvektör olan ∣ψ⟩ durumunda başlatılır

#todo 2.Adım Süperpozisyon
#? Hesaplama kayıdındaki tüm kübitlere Hadamard (H) kapısı uygulanır
#* 1/√2^n ∑(yukarısında 2^n-1, aşşağısında k=0) |k>∣ψ⟩

#todo 3.Adım Kontrollü-U Operasyonları (Phase Kickback)
#? Hesaplama kayıdındaki her j. kübit kontrol edilerek hedef kayıda U^2^j kapısı uygulanır. Phase kickback sayesinde faz bilgisi hesaplama kayıdına aktarılır
#* 1/√2^n ∑(yukarısında 2^n-1, aşşağısında k=0) e^(2πiθk) |k>∣ψ⟩

#todo 4.Adım Ters Kuantum Fourier Dönüşümü (QFT^†)
#?Fazdaki bilgiyi durum genliklerine dönüştürmek için hesaplama kayıdına QFT^† uygulanır:

#todo 5.Adım Ölçüm
#? Hesaplama kayıdı ölçülür. Elde edilen ikili (binary) tamsayı değeri y olsun
#? Tahmini faz: θ ≈ y/2^n

# Bu örnekte θ = 1/3 faz değeri hedeflenmiştir (U∣1⟩=e^(2πi(1/3)) ∣1⟩ 

import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import QFTGate
from qiskit_aer import AerSimulator

# 1. PARAMETRELER VE KAYITLAR
n_counting = 3 
theta = 1 / 3   

counting_qr = QuantumRegister(n_counting, "counting")
target_qr = QuantumRegister(1, "target")
cr = ClassicalRegister(n_counting, "result")
qc = QuantumCircuit(counting_qr, target_qr, cr)

# 2. DEVRE ADIMLARI
# Adım A: Target kübitini |1> yapma
qc.x(target_qr)

# Adım B: Counting kübitlerine Hadamard
for qubit in range(n_counting):
    qc.h(counting_qr[qubit])

# Adım C: Kontrollü-U^(2^j) kapıları
angle = 2 * np.pi * theta
for j in range(n_counting):
    power_angle = angle * (2**j)
    qc.cp(power_angle, counting_qr[j], target_qr[0])

# Adım D: Ters QFT (Yeni QFTGate ve inverse() kullanımı)
qft_gate = QFTGate(num_qubits=n_counting).inverse()
qc.append(qft_gate, counting_qr)

# Adım E: Ölçüm
qc.measure(counting_qr, cr)

# 3. SİMÜLASYON
# IQFT kapısını temel kuantum kapılarına (H, CP, SWAP vs.) ayırıyoruz
qc_decomposed = qc.decompose()

simulator = AerSimulator()
job = simulator.run(qc_decomposed, shots=1000)
counts = job.result().get_counts()

# Sonuçları okuma
most_frequent_binary = max(counts, key=counts.get)
decimal_value = int(most_frequent_binary, 2)
estimated_theta = decimal_value / (2**n_counting)

print(f"Ölçüm Sonuçları (Counts): {counts}")
print(f"Ölçülen Binary Değer: {most_frequent_binary}")
print(f"Hesaplanan Faz (Theta): {estimated_theta:.4f}")
print(f"Gerçek Faz (Theta): {theta:.4f}")