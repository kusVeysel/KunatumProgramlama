#  ⊕ = bit düzeyinde XOR işlemidir.

#! H^(⊗2)∣00⟩ = 1/2 ( ∣00⟩ + ∣01⟩ + ∣10⟩ + ∣11⟩ )
#! H^(⊗2)∣01⟩ = 1/2 ( ∣00⟩ − ∣01⟩ + ∣10⟩ − ∣11⟩ )
#! H^(⊗2)∣10⟩ = 1/2 ( ∣00⟩ + ∣01⟩ − ∣10⟩ − ∣11⟩ ) 
#! H^(⊗2)∣11⟩ = 1/2 ( ∣00⟩ − ∣01⟩ − ∣10⟩ + ∣11⟩ )

#? s = "s0s1" & s = ab için:
#* İşlevi: Sadece y * ab ≡ 0 (mod2) şartını sağlayan durumlar kalır
#* Hesap: ölçülen ab durumu için a*s0 + b*s1 = 0 durumu sağlanır
#! 00 için hiçbir durum yok olmaz her ihtimal(1/2∣00⟩ 1/2∣01⟩ 1/2∣10⟩ 1/2∣11⟩) çıkar (birebir)

#* Simon Algoritması, Kuantum Fourier Dönüşümü (QFT) ve Shor Algoritması'nın temelini oluşturan ilk üstel (exponential) kuantum hızlanmasını sağlayan algoritmadır.

#? Amaç ve Tanım
#* Elimizde birebir (one-to-one) veya ikiyebir (two-to-one) çalışan bir fonksiyon var: f:{0,1}^n -> {0,1}^n. Bu fonksiyon için şu kural geçerlidir:
#* f(x) = f(y) ⟺ x ∈ {0^n, s} , Buradaki s, fonksiyonun gizli periyodudur (string). Amaç bu s değerini bulmaktır:
#* Eğer s = 00...0 ise fonksiyon birebirdir (her girdinin çıktısı farklıdır)
#* Eğer s != 00...0 ise fonksiyon ikiyebirdir (farklı iki girdi aynı çıktıyı verir)

#* Ölçüm Aşamasında Hedef Kübitler: 4. ve 5. adım arasında hedef (ikinci sicil) kübitlerin de ölçülebileceği (veya ölçülmeden bırakılabileceği) ancak algoritmanın çalışmasını etkilemediği

#? Klasik vs Kuantum Farkı
#* Klasik Bilgisayar: s gizli periyodunu bulmak için rastgele girdiler deneyip aynı çıktıyı veren iki girdi (f(x) = f(y)) çakışması arar. En kötü senaryoda O(2^(n/2)) adım sürer (Üstel zaman)
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

#* Elde edilen her y vektörü şu diklik koşulunu sağlar: s * y = 0 (mod 2)
#* n−1 adet bağımsız y vektörü toplandığında, lineer denklem sistemi (Gauss Eleme yöntemi) klasik olarak çözülerek s kesin olarak bulunur


# 2-bitlik bir girdi için gizli periyodun s = 11 olduğu Simon devresi kurgusu

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

s = "11"
n = len(s)

qr_input = QuantumRegister(n)
qr_target = QuantumRegister(n)
cr = ClassicalRegister(n)

#? 1.Adım
qc = QuantumCircuit(qr_input, qr_target, cr)

#? 2.Adım
qc.h(qr_input)

#? 3.Adım Oracle (s = 11 için 2-to-1 fonksiyon tasarımı)
# f(x) = x veya f(x) = x XOR 11
#* 11 durumunu cx kapısında her durumda çalışır yani 0.index içinde 1.index içinde , mesela s = 10 olsaydı sağdaki bit durumu için çalışmayacaktı yani oracle tasarımımız şöyle olurdu:
#* qc.cx(qr_input[1], qr_target[1])
#* qc.cx(qr_input[1], qr_target[0])

qc.cx(qr_input[0], qr_target[0])
qc.cx(qr_input[0], qr_target[1])
qc.cx(qr_input[1], qr_target[0])
qc.cx(qr_input[1], qr_target[1])

#? 4.Adım
qc.h(qr_input)

#? 5.Adım
qc.measure(qr_input, cr)

simulator = AerSimulator()
counts = simulator.run(qc, shots=1000).result().get_counts()

print("Ölçülen Y Vektörleri:", counts)
