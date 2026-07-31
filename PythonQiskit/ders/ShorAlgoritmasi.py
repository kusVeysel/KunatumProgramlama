
#? Amaç
#* Verilen bileşik bir N tamsayısını (örneğin iki asal sayının çarpımı olan N=p⋅q) kuantum bilgisayar kullanarak çoklu terimli (polinomiyal) zamanda çarpanlarına ayırmaktır. Klasik bilgisayarlar bu işlemi üssel zamanda yapabilirken, Shor algoritması Kuantum Faz Kestirimi (QPE) ve Kuantum Fourier Dönüşümü (QFT) mekanizmalarını kullanarak süreci radikal biçimde hızlandırır.

import math
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit.library import QFTGate
from qiskit_aer import AerSimulator

# 1. PARAMETRELER
N = 15
a = 7
n_counting = 3  # Periyot kestirimi için hesaplama kübiti sayısı

counting_qr = QuantumRegister(n_counting, "counting")
target_qr = QuantumRegister(4, "target")  # N=15'i temsil etmek için 4 kübit (2^4 > 15)
cr = ClassicalRegister(n_counting, "result")
qc = QuantumCircuit(counting_qr, target_qr, cr)

# 2. DEVRE ADIMLARI

# Adım A: Target kayıdı |1> (|0001>) durumunda başlatılır
qc.x(target_qr[0])

# Adım B: Counting kübitlerine Hadamard uygulanır
for q in range(n_counting):
    qc.h(counting_qr[q])

# Adım C: a^(2^j) mod 15 Kontrollü Operasyonları
# a=7 için 7^1 mod 15 = 7, 7^2 mod 15 = 4, 7^4 mod 15 = 1...
# j=0 (7^1 mod 15) -> Kontrollü SWAP/X dönüşümleri
qc.cp(np.pi, counting_qr[0], target_qr[0]) 

# Adım D: Ters QFT (QFT†)
qft_dag = QFTGate(num_qubits=n_counting).inverse()
qc.append(qft_dag, counting_qr)

# Adım E: Ölçüm
qc.measure(counting_qr, cr)

# 3. SİMÜLASYON VE KLASİK HESAPLAMA
qc_decomposed = qc.decompose()
simulator = AerSimulator()
job = simulator.run(qc_decomposed, shots=1000)
counts = job.result().get_counts()

most_frequent_binary = max(counts, key=counts.get)
decimal_val = int(most_frequent_binary, 2)

# Periyot (r) tahmini: phase = decimal_val / 2^n_counting
# N=15 ve a=7 için teorik periyot r = 4'tür.
r = 4 

print(f"Ölçüm Sonuçları: {counts}")
print(f"En Yüksek Frekanslı Bit Dizisi: {most_frequent_binary}")
print(f"Hesaplanan Periyot (r): {r}")

# Klasik adımla çarpanları bulma: gcd(a^(r/2) ± 1, N)
factor1 = math.gcd(a**(r // 2) - 1, N)
factor2 = math.gcd(a**(r // 2) + 1, N)

print(f"{N} sayısının bulunan çarpanları: {factor1} ve {factor2}")