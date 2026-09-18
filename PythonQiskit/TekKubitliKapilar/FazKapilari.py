 #? Faz Kapıları

#* Faz kapıları kübitin fazını değiştirir
#* Kübitin olasılıklarını doğrudan değiştirmek yerine kuantum durumundaki faz bilgisini değiştirir


# Temel faz kapıları:

#? S Kapısı
#* |0⟩ → |0⟩
#* |1⟩ → i|1⟩

#? T Kapısı
#* |0⟩ → |0⟩
#* |1⟩ → e^(iπ/4)|1⟩

#? P(θ) Faz Kapısı
#* |0⟩ → |0⟩
#* |1⟩ → e^(iθ)|1⟩


from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

#? 1 kübitlik devre
devre = QuantumCircuit(1,1)
# Başlangıç durumu: |0⟩

# Önce Hadamard uygulanarak kübit süperpozisyona alınır
devre.h(0)

# S Faz Kapısı
# Fazı π/2 kadar değiştirir
devre.s(0)

result = Statevector.from_instruction(devre)
print("Genlikler:", result.data)
print("Olasılıklar:", result.probabilities())

print("S Kapısı:")
print(devre.draw())


#? Yeni bir devre
devre = QuantumCircuit(1,1)
# Başlangıç durumu: |0⟩

# Kübiti süperpozisyona al
devre.h(0)

# T Faz Kapısı
# Fazı π/4 kadar değiştirir
devre.t(0)

result = Statevector.from_instruction(devre)
print("Genlikler:", result.data)
print("Olasılıklar:", result.probabilities())

print("\nT Kapısı:")
print(devre.draw())


#? Yeni bir devre
devre = QuantumCircuit(1,1)
# Başlangıç durumu: |0⟩

# Kübiti süperpozisyona al
devre.h(0)

# P(θ) genel faz kapısı
# Burada θ = π/3
from numpy import pi

devre.p(pi / 3, 0)

result = Statevector.from_instruction(devre)
print("Genlikler:", result.data)
print("Olasılıklar:", result.probabilities())

print("\nP(θ) Faz Kapısı:")
print(devre.draw())