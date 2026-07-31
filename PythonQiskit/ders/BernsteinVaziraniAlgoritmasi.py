
#? Amaç
#* Elimizde bir fonksiyon var: f(x) = s * x  (mod 2)
#* Buradaki s, bulmak istediğimiz gizli bit dizisidir (örneğin s = 101). s * x ise s ve x bitlerinin iç çarpımıdır (bit bazlı XOR toplamı)

#? Klasik vs Kuantum Farkı
#* Klasik Bilgisayar: n-bitlik gizli s dizisini bulmak için her biti teker teker sorgulamalıdır (n adet sorgu)
#* Kuantum Bilgisayar: s kaç bit olursa olsun, fonksiyonu sadece 1 kez çağırarak s'in tamamını bulur

#todo 1.Adım Hazırlık
#? n kontrol kübiti |0⟩, 1 hedef kübit |1⟩ yapılır

#todo 2.Adım Süperpozisyon
#? Tüm kübitlere Hadamard(h) uygulanır (Kontroller |+⟩, hedef |-⟩)

#todo 3.Adım Oracle
#? s dizisinde hangi basamakta 1 varsa, o indeksteki kontrol kübitinden hedefe bir CNOT kapısı konur
#* Hedef |-⟩ olduğu için Phase Kickback gerçekleşir ve fazlar kontrol kübitlerine yansır

#todo 4.Adım Son Hadamard
#? Kontrol kübitlerine tekrar h uygulanır

#todo 5.Adım Ölçüm
#? Kontrol kübitleri ölçülür. Çıkan sonuç doğrudan gizli s dizisinin kendisidir

# Gizli dizinin s = 101 (s2=1, s1=0, s0=1) olduğu örnek:

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

secret_s = "101"
n = len(secret_s)

#? 1.Adım
qr_input = QuantumRegister(n)
qr_target = QuantumRegister(1)
cr = ClassicalRegister(n)

qc = QuantumCircuit(qr_input, qr_target, cr)
qc.x(qr_target)

#? 2.Adım
qc.h(qr_input)
qc.h(qr_target)

#? 3.Adım Oracle (s dizisinde '1' olan indekslere CNOT atılır)
#! s dizisi ters sırayla okunur (Qiskit kubit sıralaması nedeniyle)
for i, bit in enumerate(reversed(secret_s)):
    if bit == '1':
        qc.cx(i, n)

#? 4.Adım
qc.h(qr_input)

#? 5.Adım
qc.measure(qr_input, cr)

simulator = AerSimulator()
result = simulator.run(qc, shots=1).result().get_counts()

print("Gizli Dizi (s) :", secret_s)
print("Ölçüm Sonucu   :", result)

#* sadece 101 görmek için:
# print("Ölçüm Sonucu   :", list(result.keys())[0])
