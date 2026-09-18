
#! H^(⊗2)∣00⟩ = 1/2 ( ∣00⟩ + ∣01⟩ + ∣10⟩ + ∣11⟩ )
#! H^(⊗2)∣01⟩ = 1/2 ( ∣00⟩ − ∣01⟩ + ∣10⟩ − ∣11⟩ )
#! H^(⊗2)∣10⟩ = 1/2 ( ∣00⟩ + ∣01⟩ − ∣10⟩ − ∣11⟩ ) 
#! H^(⊗2)∣11⟩ = 1/2 ( ∣00⟩ − ∣01⟩ − ∣10⟩ + ∣11⟩ )

#? Amaç
#* Bir fonksiyonun sabit (constant) mi yoksa dengeli (balanced) mi olduğunu tek bir sorguda belirlemek

#?
#* Klasik bilgisayarlar en kötü senaryoda sonucu kesin bilmek için 2^(n-1)+1 sorgu yapmak zorundadır. Deutsch-Jozsa algoritması ise bunu tek bir kuantum sorgusu (1 adım) ile çözer

#todo 1.Adım Hazırlık
#? n adet kontrol kübiti |0⟩, 1 adet hedef kübit |1⟩ olarak başlatılır

#todo 2.Adım Süperpozisyon
#? Tüm kübitlere Hadamard (h) uygulanır
#* Kontrol kübitleri eşit süperpozisyona (|+⟩) girer
#* Hedef kübit |-⟩ durumuna geçer

#todo 3.Adım Oracle(Fonksiyon) Çağrısı
#? Kontrollü kapı uygulanır. Hedef |-⟩ olduğu için Phase Kickback gerçekleşir! Fonksiyonun çıktısı f(x), faz olarak kontrol kübitlerinin önüne gelir
#? 1/√2^n ∑(aşşağısı x) (-1)^f(x)|x⟩

#todo 4.Adım Girişim(Interference)
#? Kontrol kübitlerine tekrar Hadamard (h) uygulanır. Fazlardaki eksi ve artı işaretleri birbirini sönümler veya güçlendirir

#todo 5.Adım Ölçüm
#? Kontrol kübitleri ölçülür
#* Sonuç tamamen |00...0⟩ çıkarsa Fonksiyon SABİTtir
#* Sonuç |00...0⟩'dan farklı herhangi bir şey çıkarsa Fonksiyon DENGELİdir.


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

def deutchjozsa(oracle_type="constant"):
    input_qr = QuantumRegister(2)
    target_qr = QuantumRegister(1)
    
    cr_input = ClassicalRegister(2)

    #? 1.Adım
    qc = QuantumCircuit(input_qr, target_qr, cr_input)

    #? 2.Adım
    qc.x(target_qr)
    qc.h(input_qr)
    qc.h(target_qr)

    #? 3.Adım
    if oracle_type == "constant":
        pass  # f(x) = 0
    elif oracle_type == "balanced":
        qc.cx(input_qr[0], target_qr[0])
        qc.cx(input_qr[1], target_qr[0])

    #? 4.Adım
    qc.h(input_qr)

    #? 5.Adım
    qc.measure(input_qr, cr_input)

    simulator = AerSimulator()
    counts = simulator.run(qc, shots=1000).result().get_counts()
    
    return counts


print("Sabit Fonksiyon Sonucu :", deutchjozsa("constant"))
print("Dengeli Fonksiyon Sonucu:", deutchjozsa("balanced"))