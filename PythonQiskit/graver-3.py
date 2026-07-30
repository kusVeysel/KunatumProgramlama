from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit_aer import AerSimulator

# 2 kübitlik kuantum ve klasik yazmaçlar
qr = QuantumRegister(2, name="q")
cr = ClassicalRegister(2, name="c")
qc = QuantumCircuit(qr, cr)

# 1. ADIM: Süperpozisyon (Hadamard)
qc.h([0, 1])

# 2. ADIM: Oracle (|10> durumunu işaretleme)
# q0 = 0, q1 = 1 olduğunda faz çevirmek için önce q0'a X atılır
qc.x([0,1])
qc.cz(0, 1)
qc.x([0,1])


# 3. ADIM: Diffuser (Yayılım Operatörü - Sabit 5 Aşama)
qc.h([0, 1])   # 1. Aşama: Baz Değişimi
qc.x([0, 1])   # 2. Aşama: Maskeleme
qc.cz(0, 1)    # 3. Aşama: Orijinde Faz Çevirme
qc.x([0, 1])   # 4. Aşama: Maskeyi Çıkarma
qc.h([0, 1])   # 5. Aşama: Dalga Yayılımı

# 4. ADIM: Ölçüm
qc.measure(qr, cr)

# Simülasyonu Çalıştırma
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print(counts)