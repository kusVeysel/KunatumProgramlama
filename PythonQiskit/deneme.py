from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr,cr)

#? 1.Adım
qc.h([0,1])

#? 2.Adım
qc.cz(1,0) 

#? 3.Adım
qc.h([0, 1])  #* ilk duruma çeker (süperpozisyon öncesi yani |00>) 
#! 2.adımda(oracle) yaptığımız için yani aradığımız kübitin genliğini eksi yaptık bu yüzden hadamard kapısnın yapısını bozarız ve yapıcı yıkıcı dengesi bozulur yani , hadamard kapısı unitierdir(I) 2.defa uygulandığında ilk durumuna geri döner(süperpozisyon olmamış gibi) ancak biz bunu yaptığmız için yıkıcı ve yapıcı dengesi bozuldu ve süperpozisyon olarak kalmaya devam etti 
qc.x([0, 1])  #* durumu |11>e çektik
qc.cz(1, 0)    #* durumumuza - attık
qc.x([0, 1])  #* durmu |00>a çektik
qc.h([0, 1])  
#! 2eksi olduğu içni ilkteki gibi yıkıcı yapıcı etksi bozulmadı , yıkııc yapıcı etkinin bozulmsıd için , eksi sayısının 1 ya da 3 olması lazım , değilse(0,2,4) bozulmaz

#? 4.Adım
qc.measure([0,1],[0,1])

simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print(counts)
