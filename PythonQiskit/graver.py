
#! (2 * OrtalamaGenlik - KendiGenliği)

#? Amaç ve Karmaşıklık
#* N=2^n elemanlı bir listede aranan tek bir ∣w⟩ elemanını bulmak için:
#* Klasik Bilgisayar: Ortalama N/2, en kötü senaryoda N sorgu yapar (O(N)).
#* Kuantum Bilgisayar: Yaklaşık π/4 √N sorguda bulur (O(√N))

#todo 1.Adım: Hadamard Kapısı(h)
#? Tüm kübitlere hadamard(h) kapısı uygula hepsini eşit olasılığa getir(tüm durumlar olabilir, her durum %25)

#todo 2.Adım: kahin(oracle/zf)
#? Arama kriterine uyan aranan doğru cevabın genliğinin işaretini negatif yapar (fazını 180derece çevirir). Aranan cevabın olasılığını henüz değiştirmez, sadece işaretini işaretler. örneğin |11> olsun aranan

#todo Adım 3: Yayılım Operatörü / Genlik Büyütme(Diffuser) 
#? Tüm durumların genliklerini ortalamaya göre tersine çevirir (yansıtır). İşareti negatifleşen aranan eleman bu işlem sonucunda büyük bir pozitif genlik kazanırken, diğer elemanların genlikleri küçülür.

#* 1.aşama
#? Mantık: Tüm durumları "Süperpozisyon bazı"ndan çıkartıp "Klasik baz"a (00>,|01>,vb.) geri dönüştürür
#? Ne Sağlar?: Ortalamaya göre yansıma yapabilmek için önce durumu orijine (00> noktasına) göre hizalamamız gerekir

#* 2.aşama
#? Mantık: Bütün kübitlerdeki 0'ları 1, 1'leri 0 yapar
#? Ne Sağlar? Bir sonraki adımda kullanacağımız CZ kapısı sadece |11> durumunu yakalar. Amacımız |00> durumuna işlem yapmak olduğu için, X kapıları uygulayarak |00> durumunu geçici olarak |11> kılığına sokarız.

#* 3.aşama
#? Mantık: Sistemdeki tek durum olan |11> durumunun önüne bir negatif(-) işareti koyar
#? Ne Sağlar? Aslında 2. aşamada |00>'ı |11>'a dönüştürdüğümüz için, bu kapı doğrudan orijin olan |00> durumunun fazını çevirmiş olur. (2|00><00| - I matematiği burada gerçekleşir) 

#* 4.aşama
#? Mantık: 2. aşamada uyguladığımız X kapılarının tam tersini (simetriğini) yapar
#? Ne Sağlar? Geçici olarak |11> kılığına soktuğumuz |00> durumunu tekrar eski orijinal haline (|00>) çeviri

#* 5.aşama
#? Mantık: 1. aşamada bozduğumuz süperpozisyon bazına geri döner
#? Ne Sağlar? Orijinde (|00>) yaptığımız bu faz çevrimini tekrar tüm arama uzayına yayar

#todo Adım 4: Ölçüm
#? Süperpozisyon halindeki kübitler ölçülerek klasik ortama aktarılır. Genliği en yüksek olan (yani büyütülen) durum, yüksek bir olasılıkla ekranda görünür.


from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
# from qiskit.quantum_info import Statevector
from qiskit_aer import AerSimulator

qr = QuantumRegister(2)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr,cr)

#? 1.Adım
qc.h([0,1])

#? 2.Adım
qc.cz(1,0) #* ya da qc.cz(0,1) farketmez

#? 3.Adım
# qc.h([0, 1])  # 1. Aşama
qc.x([0, 1])  # 2. Aşama
qc.cz(1, 0)   # 3. Aşama   #* ya da qc.cz(0,1) farketmez
qc.x([0, 1])  # 4. Aşama
qc.h([0, 1])  # 5. Aşama


#? 4.Adım
qc.measure([0,1],[0,1]) #* ya da qc.measure(qr,cr)


# Devreyi simülatörde 1000 kez çalıştır
simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print(counts)

# print(qc.draw())


# print(Statevector.from_instruction(qc).data)
# print(Statevector.from_instruction(qc).probabilities())