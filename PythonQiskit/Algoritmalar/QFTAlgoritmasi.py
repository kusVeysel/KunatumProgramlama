# cp faz kapısı
#* iki kübit arasında çalışan ve sadece her iki kübit de |1⟩ durumundayken hedefe belirli bir açısal faz (dönme) ekleyen mantıksal bir kuantum kapısıdır
#* 1.parametre uygulanacak faz açısı, 2.parametre kontrol kübiti, 3.parametre hedef kübiti

#? Tanım
#* Kuantum Fourier Dönüşümü (QFT), klasik Ayrık Fourier Dönüşümü'nün (DFT) kuantum durumları üzerindeki karşılığıdır. N=2^n boyutlu bir durum uzayında O(NlogN) karmaşıklığa sahip klasik FFT yerine O(n²) kuantum kapısı karmaşıklığı ile çalışır

#? Temel Amacı ve Avantajı
#* Ne İşe Yarar? Periyodik yapıları ortaya çıkarmak için kullanılır. Shor Algoritması ve Kuantum Faz Kestirimi (QPE) gibi kritik algoritmaların temelini oluşturur
#* Klasik Üstünlük: Klasik Hızlı Fourier Dönüşümü (FFT) N=2^n eleman için O(n2^n) işlem yaparken, QFT bunu sadece O(n²) kuantum kapısıyla gerçekleştirir

#? Devre Mimarisi ve Kullanılan Kapılar
#* Hadamard Kapısı (h): Kübitleri süperpozisyona sokar ve ilk faz ilişkisini kurar.
#* Kontrollü Faz Kapıları (Rk): Komşu kübitler arasındaki açısal faz farklarını ekler. Matris formu:
#* Rk = ( 1 0 0 e^(2πi/2^k))

#? Faz ekleme mantığı
#* İlgili(target) kübit control kübitiyse(q0-q0) π(180derece) faz ekler
#* İlgili(target) kübit control kübitinin yanındaysa(q0-q1) π/2(90derece) faz ekler
#* İlgili(target) kübit control kübitinin 2 yanındaysa(q0-q2) π/4(45derece) faz ekler
#* ...

#! Devrenin sonunda kübit sıralaması ters döndüğü için çıkışta SWAP kapıları uygulanarak sıra düzeltilir.

import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def qft(n):
    circuit = QuantumCircuit(n)
    
    #* 1. Hadamard ve Kontrollü Faz Kapıları (R_k)
    for target in range(n):
        circuit.h(target)
        for control in range(target + 1, n):
            k = control - target + 1
            angle = 2 * np.pi / (2**k)
            circuit.cp(angle, control, target)
            
    #* İşlem Mantığı: İlk işlenen qubit, kendisinden sonra gelen TÜM qubit'lerden faz bilgisi toplamak zorundadır. Bu yüzden en çok faz açısını (en detaylı bilgisi olan ikilik kesiri) ilk işlenen qubit alır.
    for i in range(n // 2):
        circuit.swap(i, n - i - 1)
         
    return circuit

n_qubits = 3
qft_circuit = qft(n_qubits)

print(qft_circuit)

qft_circuit.measure_all()
simulator = AerSimulator()
run = simulator.run(qft_circuit,shots=1000)
print(run.result().get_counts())
