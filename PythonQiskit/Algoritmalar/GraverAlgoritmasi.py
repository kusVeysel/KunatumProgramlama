
#! h => YeniGenlik = (2 * OrtalamaGenlik - KendiGenliği)

#! H^(⊗2)∣00⟩ = 1/2 ( ∣00⟩ + ∣01⟩ + ∣10⟩ + ∣11⟩ )
#! H^(⊗2)∣01⟩ = 1/2 ( ∣00⟩ − ∣01⟩ + ∣10⟩ − ∣11⟩ )
#! H^(⊗2)∣10⟩ = 1/2 ( ∣00⟩ + ∣01⟩ − ∣10⟩ − ∣11⟩ ) 
#! H^(⊗2)∣11⟩ = 1/2 ( ∣00⟩ − ∣01⟩ − ∣10⟩ + ∣11⟩ )


#? Amaç
#* Aranan elemana faz uygulayıp(-1) belirlemek ve daha sonra diffuser ile genliklerle oynayıp hadamard kapısının yapıcı-yıkıcı gücüyle genlikleri kırdırıp aranan durumun kalmasını sağlamak

#? Klasik vs Kuantum Farkı
#* N = 2^n elemanlı bir listede aranan tek bir ∣w⟩ elemanını bulmak için:
#* Klasik Bilgisayar: Ortalama N/2, en kötü senaryoda N sorgu yapar (O(N)).
#* Kuantum Bilgisayar: Yaklaşık π/4 √N sorguda bulur (O(√N))

#todo 1.Adım: Hadamard Kapısı(h)
#? Tüm kübitlere hadamard(h) kapısı uygula hepsini eşit olasılığa getir(tüm durumlar olabilir, her durum %25)

#todo 2.Adım: kahin(oracle/cz)
#? Arama kriterine uyan aranan doğru cevabın genliğinin işaretini negatif yapar (fazını 180derece çevirir). Aranan cevabın olasılığını henüz değiştirmez, sadece işaretini işaretler. örneğin |11⟩ olsun aranan

#todo Adım 3: Yayılım Operatörü / Genlik Büyütme(Diffuser) 
#? Tüm durumların genliklerini ortalamaya göre tersine çevirir (yansıtır). İşareti negatifleşen aranan eleman bu işlem sonucunda büyük bir pozitif genlik kazanırken, diğer elemanların genlikleri küçülür.

#* 1.aşama
#? Mantık: Tüm durumları Süperpozisyon bazından çıkartıp Klasik baz'a (00⟩,|01⟩,vb.) geri dönüştürür. Kod kısmında belirtilen durumundan dolayı sistem 100% |00⟩ olmaz, süperpozisyon durumunda kalmaya devam eder ama yoğunluk |00⟩'dadır
#? Ne Sağlar?: Ortalamaya göre yansıma yapabilmek için önce durumu orijine (00⟩ noktasına) göre hizalamamız gerekir

#* 2.aşama
#? Mantık: Bütün kübitlerdeki 0'ları 1, 1'leri 0 yapar
#? Ne Sağlar? Bir sonraki adımda kullanacağımız CZ kapısı sadece |11⟩ durumunu yakalar. Amacımız |00⟩ durumuna işlem yapmak olduğu için, X kapıları uygulayarak |00⟩ durumunu geçici olarak |11⟩ kılığına sokarız.

#* 3.aşama
#? Mantık: Sistemdeki tek durum olan |11⟩ durumunun önüne bir negatif(-) işareti koyar
#? Ne Sağlar? Aslında 2. aşamada |00⟩'ı |11⟩'a dönüştürdüğümüz için, bu kapı doğrudan orijin olan |00⟩ durumunun fazını çevirmiş olur. (2|00⟩<00| - I matematiği burada gerçekleşir) 

#* 4.aşama
#? Mantık: 2. aşamada uyguladığımız X kapılarının tam tersini (simetriğini) yapar
#? Ne Sağlar? Geçici olarak |11⟩ kılığına soktuğumuz |00⟩ durumunu tekrar eski orijinal haline (|00⟩) çeviririz

#* 5.aşama
#? Mantık: 1. aşamada bozduğumuz süperpozisyon bazına geri döner
#? Ne Sağlar? Orijinde (|00⟩) yaptığımız bu faz çevrimini tekrar tüm arama uzayına yayar

#todo Adım 4: Ölçüm
#? Süperpozisyon halindeki kübitler ölçülerek klasik ortama aktarılır. Genliği en yüksek olan (yani büyütülen) durum, yüksek bir olasılıkla ekranda görünür.

# 100% |11⟩ çıkartan graver algoritması kodu:

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

qr = QuantumRegister(2)
cr = ClassicalRegister(2)

qc = QuantumCircuit(qr,cr)

#? 1.Adım
qc.h([0,1])

#? 2.Adım
qc.cz(1,0) #* ya da qc.cz(0,1), cz kapısı simetrik olduğu için farketmez 

#? 3.Adım
qc.h([0, 1])  # 1. Aşama
#* Hadamard kapısı uniter kapıdır HH†=I yani 2 defa uygulanırsa eski haline döner, süperpozisyon öncesi kübit |00⟩ durumundaydı , yani |00⟩ durumuna döner ama...
#! ...ilk başta aradığımız kübiti eksi ile işaretledik sistemde 1 eksi var, bu durum hadamard kapısının yıkıcı-yapıcı durumunu bozar, sistem 100% olarak |00⟩ durumuna çökmez ,uniter kapı olmasına (2 defa uygulanınca eski haline denmesi gerekmesine) rağmen halen süperpozisyon durumunda kalır ancak sistem(genlikler) |00⟩ durumuna yoğunlaşır

#! sistemde 1 ya da 3 eksi varsa hadamard kapısının yapıcı-yıkıcı durumu bozulur; 0,2 ya da 4 tane eksi varsa yapıcı-yıkıcı durumunu korur

qc.x([0, 1])  # 2. Aşama
qc.cz(1, 0)   # 3. Aşama   #* ya da qc.cz(0,1), cz kapısı simetrik olduğu için farketmez 
qc.x([0, 1])  # 4. Aşama
qc.h([0, 1])  # 5. Aşama
#* daha net anlamak için en yukardaki 4satırlık(#!) kısımdaki 2kübitlik hadamard kapısı formülü ile yapabilirsiniz
#? anlamanız için: 3.kez hadamard kapısı uygulanmadan önce durum şudur = -1/2|00⟩ 1/2|01⟩ 1/2|10⟩ -1/2|11⟩

#* H^(⊗2)∣00⟩ = 1/2 ( ∣00⟩ + ∣01⟩ + ∣10⟩ + ∣11⟩ ) için:
#* -1/2|00⟩ => -1/4 ( |00⟩ + |01⟩ + |10⟩ + |11⟩ ) 

#* H^(⊗2)∣01⟩ = 1/2 ( ∣00⟩ − ∣01⟩ + ∣10⟩ − ∣11⟩ ) için:
#* 1/2|01⟩ => 1/4 ( |00⟩ - |01⟩ + |10⟩ - |11⟩ ) 

#* H^(⊗2)∣10⟩ = 1/2 ( ∣00⟩ + ∣01⟩ − ∣10⟩ − ∣11⟩ ) için:
#* 1/2|10⟩ => 1/4 ( |00⟩ + |01⟩ - |10⟩ - |11⟩ ) 

#* H^(⊗2)∣11⟩ = 1/2 ( ∣00⟩ − ∣01⟩ − ∣10⟩ + ∣11⟩ ) için:
#* -1/2|11⟩ => -1/4 ( |00⟩ - |01⟩ - |10⟩ + |11⟩ ) 

#* tüm durumlar toplanınca = -1|11⟩ olur, olasılık =⟩ (-1)² = 1, yani 100% |11⟩ gelir  

#? 4.Adım
qc.measure(qr,cr) #* ya da qc.measure([0,1],[0,1]) farketmez

simulator = AerSimulator()
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts()

print(counts)