
#* Simon Algoritması, Kuantum Fourier Dönüşümü (QFT) ve Shor Algoritması'nın temelini oluşturan ilk üstel (exponential) kuantum hızlanmasını sağlayan algoritmadır.

#? Amaç ve Tanım
#* Elimizde birebir (one-to-one) veya ikiyebir (two-to-one) çalışan bir fonksiyon var: f:{0,1}^n -> {0,1}^n. Bu fonksiyon için şu kural geçerlidir:
#* f(x) = f(y) ⟺ x ⊕ ∈ {0^n, s} , Buradaki s, fonksiyonun gizli periyodudur (string). Amaç bu s değerini bulmaktır:
#* Eğer s = 00...0 ise fonksiyon birebirdir (her girdinin çıktısı farklıdır)
#* Eğer s != 00...0 ise fonksiyon ikiyebirdir (farklı iki girdi aynı çıktıyı verir)

#? Klasik vs Kuantum Farkı
#* Klasik Bilgisayar: s gizli periyodunu bulmak için rastgele girdiler deneyip aynı çıktıyı veren iki girdi (f(x)=f(y)) çakışması arar. En kötü senaryoda O(2^(n/2)) adım sürer (Üstel zaman)
#* Kuantum Bilgisayar: Yaklaşık O(n) ölçüm ve klasik lineer denklem çözümü ile s değerini bulur (Polinomiyal zaman)

#todo 1.Adım Hazırlık
#? n adet girdi kübiti (∣0⟩) ve n adet hedef kübiti (∣0⟩) hazırlanır.

#todo 2.Adım Süperpozisyon
#? Sadece girdi kübitlerine Hadamard (h) uygulanır

#todo 3.Adım Oracle
#? Uf oracle'ı uygulanır: ∣x⟩∣0⟩ → ∣x⟩∣f(x)⟩

#todo 4.Adım Son Hadamard
#? Girdi kübitlerine tekrar Hadamard (h) uygulanır

#todo 5.Adım Girdi Ölçümleri
#? Girdi kübitleri ölçülür ve bir y sonucu elde edilir

#* Elde edilen her $y$ vektörü şu diklik koşulunu sağlar: s * y = 0 (mod 2)
#* n−1 adet bağımsız y vektörü toplandığında, lineer denklem sistemi (Gauss Eleme yöntemi) klasik olarak çözülerek s kesin olarak bulunur


# 2-bitlik bir girdi için gizli periyodun s = 11 olduğu Simon devresi kurgusu

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

s = "11"
n = len(s)

qr_input = QuantumRegister(n, name="input")
qr_target = QuantumRegister(n, name="target")
cr = ClassicalRegister(n, name="meas")

qc = QuantumCircuit(qr_input, qr_target, cr)

# 1. Girdileri süperpozisyona sok
qc.h(qr_input)
qc.barrier()

# 2. Oracle (s = 11 için 2-to-1 fonksiyon tasarımı)
# f(x) = x veya f(x) = x XOR 11
qc.cx(qr_input[0], qr_target[0])
qc.cx(qr_input[1], qr_target[1])
qc.cx(qr_input[0], qr_target[1])
qc.cx(qr_input[1], qr_target[0])
qc.barrier()

# 3. Girdi kübitlerine Hadamard
qc.h(qr_input)
qc.barrier()

# 4. Girdi kübitlerini ölç
qc.measure(qr_input, cr)

# Simülasyon
simulator = AerSimulator()
counts = simulator.run(qc, shots=1000).result().get_counts()

print("Ölçülen Y Vektörleri:", counts)