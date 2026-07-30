from qiskit.quantum_info import SparsePauliOp
from qiskit.circuit.library import TwoLocal
from qiskit_algorithms.optimizers import COBYLA
from qiskit_algorithms import VQE
from qiskit.primitives import StatevectorEstimator

# 1. Hamiltoniyen (Gözlemlenebilir - Observable) Tanımlama
# Örnek basit bir 2 kübitlik sistem: H = 1.0*(Z⊗I) - 0.5*(I⊗X)
observable = SparsePauliOp.from_list([("ZI", 1.0), ("IX", -0.5)])

# 2. Ansatz (Parametrik Kuantum Devresi) Hazırlama
# 'ry' kapıları ile dönüş, 'cz' kapıları ile dolanıklık (entanglement) yaratıyoruz
ansatz = TwoLocal(num_qubits=2, rotation_blocks='ry', entanglement_blocks='cz')

# 3. Klasik Optimizer ve Ölçümcü (Estimator) Tanımlama
optimizer = COBYLA(maxiter=100)
estimator = StatevectorEstimator()

# 4. VQE Algoritmasını Kurma ve Çalıştırma
vqe = VQE(estimator=estimator, ansatz=ansatz, optimizer=optimizer)

# Minimum özdeğeri (taban enerjisini) hesaplama
result = vqe.compute_minimum_eigenvalue(observable)

# 5. Sonuçları Yazdırma
print("En Düşük Enerji (Minimum Eigenvalue):", result.eigenvalue.real)
print("Optimum Parametreler:", result.optimal_point)