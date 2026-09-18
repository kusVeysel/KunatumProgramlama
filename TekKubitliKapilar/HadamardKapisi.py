 #? Hadamard (H) Kapısı
#! Hadamard kapısı bir kübitin süperpozisyon durumuna geçmesini sağlar. Çok önemli bir kapıdır

#* |0⟩ → (|0⟩ + |1⟩) / √2
#* |1⟩ → (|0⟩ - |1⟩) / √2

#! Yani başlangıçta |0⟩ durumundaki kübite H kapısı uygulanırsa, kübit %50 |0⟩ ve %50 |1⟩ olasılığıyla süperpozisyon durumuna geçer.


from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 1 kübit ve 1 klasik bit içeren devre oluşturulur
devre = QuantumCircuit(1, 1)

# Başlangıç durumu: |0⟩

# Hadamard kapısı uygulanır
devre.h(0)

# Kübit ölçülür
devre.measure(0, 0)

#? Simülasyon
simulator = AerSimulator()
job = simulator.run(devre, shots=1000)  
counts = job.result().get_counts() 
print(counts)

# Devreyi yazdır
print(devre)