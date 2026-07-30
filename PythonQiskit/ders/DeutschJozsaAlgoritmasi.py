
#todo 1.Adım Hazırlık
#? n adet kontrol kübiti |0>, 1 adet hedef kübit |1> olarak başlatılır

#todo 2.Adım Süperpozisyon
#? Tüm kübitlere Hadamard (h) uygulanır
#* Kontrol kübitleri eşit süperpozisyona (|+>) girer
#* edef kübit |-> durumuna geçer

#todo 3.Adım Oracle(Fonksiyon) Çağrısı
#? Kontrollü kapı uygulanır. Hedef |-> olduğu için Phase Kickback gerçekleşir! Fonksiyonun çıktısı f(x), faz olarak kontrol kübitlerinin önüne gelir
#? 1/√2^n ∑(aşşağısı x) (-1)^f(x)|x>

#todo 4.Adım Girişim(Interference)
#? Kontrol kübitlerine tekrar Hadamard (h) uygulanır. Fazlardaki eksi ve artı işaretleri birbirini sönümler veya güçlendirir

#todo 5.Adım Ölçüm
#? Kontrol kübitleri ölçülür
#* Sonuç tamamen |00...0> çıkarsa Fonksiyon SABİTtir
#* Sonuç $|00...0>'dan farklı herhangi bir şey çıkarsa Fonksiyon DENGELİdir.


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

def get_deutsch_jozsa_circuit(oracle_type="constant"):
    # 2 kontrol (girdi) kübiti + 1 hedef (oracle) kübiti
    n = 2
    qr_input = QuantumRegister(n, name="input")
    qr_target = QuantumRegister(1, name="target")
    cr = ClassicalRegister(n, name="meas")
    
    qc = QuantumCircuit(qr_input, qr_target, cr)

    # 1. ADIM: Başlangıç Durumu Hazırlığı
    # Hedef kübiti |1> durumuna getiriyoruz
    qc.x(qr_target)
    qc.barrier()

    # 2. ADIM: Süperpozisyon Oluşturma
    # Tüm kübitlere Hadamard uyguluyoruz. 
    # Girdiler |+>, Hedef ise |-> durumuna geçer.
    qc.h(qr_input)
    qc.h(qr_target)
    qc.barrier()

    # 3. ADIM: Oracle (Kara Kutu) Uygulaması
    if oracle_type == "constant":
        # Sabit Fonksiyon: f(x) = 1 (Girdi ne olursa olsun hedefi değiştirir/değiştirmez)
        # Hiçbir kapı koymayabiliriz (f(x)=0) ya da sadece Hedefe X koyabiliriz (f(x)=1).
        qc.x(qr_target)
        
    elif oracle_type == "balanced":
        # Dengeli Fonksiyon: CNOT kullanarak girdilerin yarısında 0, yarısında 1 çıktısı üretiyoruz.
        # Phase Kickback burada devreye girer!
        qc.cx(qr_input[0], qr_target)
        qc.cx(qr_input[1], qr_target)
        
    qc.barrier()

    # 4. ADIM: Girişim (Interference)
    # Phase Kickback ile oluşan faz bilgisini ölçülebilir genliklere çevirmek için 
    # kontrol kübitlerine tekrar Hadamard uyguluyoruz.
    qc.h(qr_input)
    qc.barrier()

    # 5. ADIM: Ölçüm
    # Sadece kontrol kübitlerini ölçüyoruz
    qc.measure(qr_input, cr)
    
    return qc

# --- TEST ETME ---
simulator = AerSimulator()

# 1. Sabit Oracle Testi
circuit_constant = get_deutsch_jozsa_circuit("constant")
result_constant = simulator.run(circuit_constant, shots=1).result().get_counts()

# 2. Dengeli Oracle Testi
circuit_balanced = get_deutsch_jozsa_circuit("balanced")
result_balanced = simulator.run(circuit_balanced, shots=1).result().get_counts()

print("Sabit Oracle Ölçüm Sonucu :", result_constant)
print("Dengeli Oracle Ölçüm Sonucu:", result_balanced)
