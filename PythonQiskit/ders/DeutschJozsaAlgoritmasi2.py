from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator

def run_normal_measurement(oracle_type="constant"):
    input_qr = QuantumRegister(2, name="x")
    target_qr = QuantumRegister(1, name="f(x)")
    
    cr_input = ClassicalRegister(2, name="meas_x")
    cr_target = ClassicalRegister(1, name="meas_f")
    
    qc = QuantumCircuit(input_qr, target_qr, cr_input, cr_target)

    # 1. Girdileri esit superpozisyona sokuyoruz (|00>, |01>, |10>, |11>)
    qc.h(input_qr)

    # 2. Oracle Mantigi
    if oracle_type == "constant":
        # Sabit Fonksiyon: Girdi ne olursa olsun f(x) = 1 uretir
        qc.x(target_qr[0])
        
    elif oracle_type == "balanced":
        # Dengeli Fonksiyon: CNOT ile f(x) = x0 XOR x1 uretir
        qc.cx(input_qr[0], target_qr[0])
        qc.cx(input_qr[1], target_qr[0])

    # 3. Hicbir girisim yapmadan direkt olcum
    qc.measure(input_qr, cr_input)
    qc.measure(target_qr, cr_target)

    simulator = AerSimulator()
    counts = simulator.run(qc, shots=10000).result().get_counts()
    
    return counts

def print_table(title, counts):
    print(f"\n--- {title} ---")
    print("Girdi (x)  -->  Çıktı f(x)   (Olasılık)")
    print("-" * 40)
    # Qiskit cıktı yapısını sıralı basmak icin sıralıyoruz
    for state in sorted(counts.keys()):
        f_x, x = state.split()
        prob = (counts[state] / 10000) * 100
        print(f"   {x}     -->      {f_x}        (%{prob:.1f})")

# Testleri çalıştır
constant_counts = run_normal_measurement("constant")
balanced_counts = run_normal_measurement("balanced")

print_table("SABİT FONKSİYON (f(x) = 1)", constant_counts)
print_table("DENGELİ FONKSİYON (f(x) = x0 XOR x1)", balanced_counts)