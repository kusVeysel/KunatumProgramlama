from qiskit import QuantumCircuit , QuantumRegister, ClassicalRegister
from qiskit.quantum_info import Statevector

q = QuantumRegister(2)
qc = QuantumCircuit(q) #* kübit oluşturuldu |00>

qc.x(1) #* 1.kübiti(kotrol kübiti) durumu |1> yapıldı
qc.h(0) #* 0.kübit(hedef kübit) süperpozisyon durumuna sokuldu
qc.cx(1,0) #* 1.kübiti(kotrol kübiti) 1 olduğu için , 2.kübite cnot uygulanır ve 1 durumuna gelir, hedef kübitimiz süperpozisyon durumunda olduğundan |01> ya da |11> olur

result = Statevector.from_instruction(qc)
print(result.data)
print(result.probabilities())

# 1. Eleman (0.): 00 gelme olasılığı %0
# 2. Eleman (0.): 01 gelme olasılığı %0
# 3. Eleman (0.5): 10 gelme olasılığı %50
# 4. Eleman (0.5): 11 gelme olasılığı %50