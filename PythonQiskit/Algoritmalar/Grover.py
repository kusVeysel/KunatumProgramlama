from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

# 2 Kübitlik Grover Devresi
qc = QuantumCircuit(2)

# 1. Adım: Tüm kübitleri süperpozisyona sokma
qc.h([0, 1])

# 2. Adım: Oracle (Hedef durum: '11' durumunu işaretleme)
# '11' durumuna CZ (Controlled-Z) kapısı uygulayarak fazını -1 yapıyoruz
qc.cz(0, 1)

# 3. Adım: Diffuser (Genlik Büyütme)
qc.h([0, 1])
qc.z([0, 1])
qc.cz(0, 1)
qc.h([0, 1])

# 4. Adım: Ölçüm
qc.measure_all()

# 5. Çalıştırma ve Ölçüm
sampler = StatevectorSampler()
job = sampler.run([qc])
result = job.result()[0]

# Güncel Qiskit Veri Yapısından Çıktı Alma
counts = result.data.meas.get_counts()

print("Ölçüm Sonuçları (Hedef '11'):", counts)