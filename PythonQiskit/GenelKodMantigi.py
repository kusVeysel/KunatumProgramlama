from qiskit import QuantumCircuit  #* Qiskit devre modülünü dahil eder
from qiskit_aer import AerSimulator  #* Simülatör modülünü dahil eder

#? QuantumCircuit(kübit_sayısı, klasik_bit_sayısı)
qc = QuantumCircuit(1, 1)

qc.x(0)  #* 0. (birinci) kübite X kapısı uygula
#! Not: Qiskit'te kübit sıralaması sağdan soladır.
#* Örneğin 4 kübitlik bir devrede durum gösterimi → |0000⟩ (Qiskit sıralaması: |q3 q2 q1 q0⟩)
# QuantumCircuit(3,3) oluşturulursa; qc.x(0) birinci, qc.x(1) ikinci, qc.x(2) üçüncü kübite X kapısı uygular.

#? Ölçüm
qc.measure(0, 0)
#* Ölçüm işlemi süperpozisyonu çökertir; kuantum durumu klasik 0 veya 1 bilgisine dönüşür.
#* 1. parametre: Ölçülecek kübit indeksi (q0)
#* 2. parametre: Sonucun aktarılacağı klasik bit indeksi (c0)
#* QuantumCircuit(2,2) oluşturulduğunda q0, q1 kübitleri ve c0, c1 klasik bitleri tanımlanır.

#? Simülasyon
simulator = AerSimulator()  #* Aer simülatör nesnesini oluşturur
job = simulator.run(qc, shots=1)  #* Devreyi çalıştırır (shots: deneyin kaç kez tekrarlanacağı)
counts = job.result().get_counts()  #* Ölçüm sonuçlarının frekansını (dağılımını) sözlük olarak alır
print(counts)

print(qc)