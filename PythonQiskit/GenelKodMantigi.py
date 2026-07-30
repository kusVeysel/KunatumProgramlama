from qiskit import QuantumCircuit #* qiskit'i dahil eder
from qiskit_aer import AerSimulator #* simülatörü dahil et

#* QuantumCircuit(Kaç_Kübitli,Kübit_kaç_bit_içerecek)
qc = QuantumCircuit(1,1)

qc.x(0) #* 0(birinci).kübite x kapısı uygula
#* eğer QuantumCircuit(3,3)lük bi kübit oluşturulursa (ilk parametre önemli) x(0) dersek birinci kübite ,x(1) dersek ikinci kübite , x(2) dersek 3.kübite x kapısı uygular 

#* Ölçüm
qc.measure(0,0) #* kuantumla arada köprü görevi görür, dolayısıyla simülatörü görebilmek için gerek vardır
#// kübitlerin kuantum yapısı bozulur, klasik 0-1'e dönüşür
#* 1.parametre kaçıncı kübiti ölçeceği 
#* 2.parametre kübitin bilgisayardaki karşılığı nereye yazılacağı
#* QuantumCircuit(2,2) şuna karşılık q0,q1 ve c0,c1 oluşur ,c'ler q'lerin karşılığıdır bilgisayarın hangi kübiti tutacağıdır

#* Simülatör için
simulator = AerSimulator() #* simülatörü oluştur
job = simulator.run(qc, shots=1) #* simulatörü çalıştır ,1.parametre devre ,2.parametre kaç kez çalıştırılacağı
counts = job.result().get_counts() #* sonucu topla (kaç kez çalıştığını yazar)
print(counts)

print(qc)

#! diğer kapıları görmek için doğrudan yazdırmamız gerekir(PauliKapilar dosyasına bak)
