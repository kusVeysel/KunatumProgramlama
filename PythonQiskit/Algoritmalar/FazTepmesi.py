# Phase Kickback

#! cx kapısı için geçerlidir
#? en iyi gözlenme yöntemi hedef kübiti |-> kontrol kübiti süperpozisyon ( |+> ya da |-> ) halidir
#? hedef kübiti |-> durumunda ise ve kontrol kübiti |1> , ya da süperpozisyon ( |+> ya da |-> ) halinde ise faz geri tepmesi olur
#* kontrol kübitin |0>'dan farklı olmasının gerekmesinin sebebi, kontrol kapılarında kontrol kübiti 0 ise kapının çalışmaması

#! cz kapısı için geçerlidir
#? en iyi gözlenme yöntemi hedef kübiti |1> ve konrol kübiti süperpozisyon ( |+> ya da |-> ) halidir
#? hedef kübit |1> ya da |-> durumunda ise ve kontrol kübiti |1> ya da süperpozisyon ( |+> ya da |-> ) halinde ise faz geri tepmesi olur, hedef kübit |+> ise dolanıklık oluşturur

#! 2.yorum(#?) olarak yazılan diğer yöntemlerde faz değişimini gözlemleyemeyiz çünkü faz tepmesi global olur, gözlemlemek istiyorsan 1.yorumu(#?) yap

from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Statevector
# from qiskit_aer import AerSimulator

qr = QuantumRegister(2)

qc = QuantumCircuit(qr)

qc.x(0)
qc.h([0,1])
qc.cx(1,0)

print(Statevector.from_instruction(qc).data)

# qc.measure_all()
# s = AerSimulator()
# run = s.run(qc,shots=100)
# print(run.result().get_counts())