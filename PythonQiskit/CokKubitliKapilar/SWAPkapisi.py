from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector

q = QuantumRegister(2)
qc = QuantumCircuit(q) #* kübit oluşturuldu |00>

qc.x(1) #* durumu daha iyi görebilmek için kübit |10> durumuna getirildi
qc.h(1) #* q1'e hadamard kapısı uygulanarak süperpozisyon durumuna sokuldu böylelikle durumu net görebileceğiz
qc.swap(0, 1) #* değiştirme işlemi gerçekleşti |01> , hadamard kapısı uyguladığımız için durum: |00> ya da |01>

result = Statevector.from_instruction(qc)

print("Genlikler:", result.data)
print("Olasılıklar:", result.probabilities())

# 1. Eleman (0.5): 00 gelme olasılığı %50
# 2. Eleman (0.5): 01 gelme olasılığı %50
# 3. Eleman (0.): 10 gelme olasılığı %0
# 4. Eleman (0.): 11 gelme olasılığı %0