from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector

q = QuantumRegister(3)
qc = QuantumCircuit(q) #* kübit oluşturuldu |000>

qc.x([1,2]) #* 1.kübit ve 2.kübit(kotrol kübitleri) durumu |1> yapıldı , kübit durumu= |110>
qc.h(0) #* 0.kübit(hedef kübit) süperpozisyon durumuna sokuldu
qc.ccx(1,2,0) #* ccx kapısı uygulandı ,hedef kübit süperpozisyon durumunda olduğu için |110> ya da |111> olur

result = Statevector.from_instruction(qc)

print(result.data)
print(result.probabilities())

# 0 , ∣000⟩ , 0. , %0
# 1 , ∣001⟩ , 0. , %0
# 2 , ∣010⟩ , 0. , %0
# 3 , ∣011⟩ , 0. , %0
# 4 , ∣100⟩ , 0. , %0
# 5 , ∣101⟩ , 0. , %0
# 6 , ∣110⟩ , 0.5 ,%50
# 7 , ∣111⟩ , 0.5 ,%50