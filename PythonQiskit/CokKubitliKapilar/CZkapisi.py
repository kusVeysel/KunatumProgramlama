from qiskit import QuantumCircuit , QuantumRegister
from qiskit.quantum_info import Statevector

q = QuantumRegister(2)
qc = QuantumCircuit(q) #* kübit oluşturuldu |00>

qc.x(1) #* 1.kübiti(kotrol kübiti) durumu |1> yapıldı ve cz kapısı uygulayacağımız için hedef kübitindeki değişimi görmek için |1> yapıldı, kübit durumu= |10>
qc.h(0) #* 0.kübit(hedef kübit) süperpozisyon durumuna sokuldu
qc.cz(1,0) #* 1.kübiti(kontrol kübit) durumu |1> olduğu için , 2.kübite(hedef kübit) cz kapısı uygulanır ve durumu -|1> haline getirilir

result = Statevector.from_instruction(qc)
print(result.data)
print(result.probabilities())


# 1. Eleman (0.): 00 gelme olasılığı %0
# 2. Eleman (0.): 01 gelme olasılığı %0
# 3. Eleman (0.): 10 gelme olasılığı %50
# 4. Eleman (0.5): 11 gelme olasılığı %50