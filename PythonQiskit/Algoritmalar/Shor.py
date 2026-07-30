# from qiskit_algorithms import Shor
# from qiskit.primitives import StatevectorSampler

# # 1. Çarpanlarına ayrılacak sayı
# N = 15
# a = 2  # a^x mod N fonksiyonu için taban

# # 2. Sampler (Ölçüm birimi) tanımlama
# sampler = StatevectorSampler()

# # 3. Shor Algoritmasını Kurma
# shor = Shor(sampler=sampler)

# # 4. Çalıştırma
# result = shor.factor(N, a=a)

# # 5. Sonucu Yazdırma
# print(f"{N} sayısının asal çarpanları:", result.factors)



import math
from fractions import Fraction
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFTGate
from qiskit.primitives import StatevectorSampler

def c_amod15(a, power):
    """a^power mod 15 işlemini gerçekleştiren kontrollü kapı devresi."""
    if a not in [2, 4, 7, 8, 11, 13]:
        raise ValueError("'a' değeri 2, 4, 7, 8, 11 veya 13 olmalıdır.")
    
    U = QuantumCircuit(4)
    for _ in range(power):
        if a in [2, 13]:
            U.swap(2, 3)
            U.swap(1, 2)
            U.swap(0, 1)
            if a == 13:
                U.x(0); U.x(1); U.x(2); U.x(3)
        elif a in [7, 8]:
            U.swap(0, 1)
            U.swap(1, 2)
            U.swap(2, 3)
            if a == 7:
                U.x(0); U.x(1); U.x(2); U.x(3)
        elif a in [4, 11]:
            U.swap(1, 3)
            U.swap(0, 2)
            if a == 11:
                U.x(0); U.x(1); U.x(2); U.x(3)
                
    U = U.to_gate()
    U.name = f"{a}^{power} mod 15"
    return U.control(1)

# 1. Shor Devresinin Kurulması
N = 15
a = 2
n_count = 8  # Hassasiyet kübit sayısı

qc = QuantumCircuit(n_count + 4, n_count)

# Ölçüm kübitlerine Hadamard kapısı
for q in range(n_count):
    qc.h(q)

# Yardımcı son kübiti |1> durumuna getirme
qc.x(n_count)

# Modüler Üst Alma Kapılarının Eklenmesi
for q in range(n_count):
    qc.append(c_amod15(a, 2**q), [q] + [i + n_count for i in range(4)])

# Ters Kuantum Fourier Dönüşümü (Inverse QFT)
qc.append(QFTGate(n_count).inverse(), range(n_count))

# Ölçüm
qc.measure(range(n_count), range(n_count))

# 2. Çalıştırma
sampler = StatevectorSampler()
job = sampler.run([qc])
result = job.result()[0]

# Güncel Qiskit 2.x Veri Yapısından Counts Alma
counts = result.data.c.get_counts()

# En çok tekrar eden ölçümü (faz bilgisini) alma
measured_phase = max(counts, key=counts.get)
phase_int = int(measured_phase, 2)
phase = phase_int / (2**n_count)

# 3. Klasik Kısım: Periyodun (r) ve Çarpanların Hesapanması
frac = Fraction(phase).limit_denominator(N)
r = frac.denominator

print(f"Ölçülen Faz: {phase}")
print(f"Hesaplanan Periyot (r): {r}")

if r % 2 == 0:
    guess1 = math.gcd(a**(r//2) - 1, N)
    guess2 = math.gcd(a**(r//2) + 1, N)
    print(f"{N} sayısının bulunan asal çarpanları: {guess1} ve {guess2}")
else:
    print("Periyot çift bulunamadı, tekrar çalıştırın.")