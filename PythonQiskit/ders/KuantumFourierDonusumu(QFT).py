
#? Temel Amacı ve Avantajı
#* Ne İşe Yarar? Periyodik yapıları ortaya çıkarmak için kullanılır. Shor Algoritması ve Kuantum Faz Kestirimi (QPE) gibi kritik algoritmaların temelini oluşturur.
#* Klasik Üstünlük: Klasik Hızlı Fourier Dönüşümü (FFT) N=2^n eleman için O(n2^n) işlem yaparken, QFT bunu sadece O(n^2) kuantum kapısıyla gerçekleştirir

#? Devre Mimarisi ve Kullanılan Kapılar
#* Hadamard Kapısı (h): Kübitleri süperpozisyona sokar ve ilk faz ilişkisini kurar.
#* Kontrollü Faz Kapıları (Rk): Komşu kübitler arasındaki açısal faz farklarını ekler. Matris formu:
#* Rk = ( 1 0 0 e^(2πi/2^k))

#? Not: Devrenin sonunda kübit sıralaması ters döndüğü için çıkışta SWAP kapıları uygulanarak sıra düzeltilir.

import numpy as np
from qiskit import QuantumCircuit

n = 3
qc = QuantumCircuit(n)

# 1. Kübit (q2)
qc.h(2)
qc.cp(np.pi / 2, 1, 2)  # R2 kapısı
qc.cp(np.pi / 4, 0, 2)  # R3 kapısı

# 2. Kübit (q1)
qc.h(1)
qc.cp(np.pi / 2, 0, 1)  # R2 kapısı

# 3. Kübit (q0)
qc.h(0)

# Bit sıralamasını düzeltmek için SWAP
qc.swap(0, 2)

print(qc.draw())