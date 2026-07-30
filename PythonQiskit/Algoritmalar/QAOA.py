from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import StatevectorSampler
from qiskit_optimization.translators import from_docplex_mp
from docplex.mp.model import Model

# 1. Problemi Tanımlama (QUBO / Docplex)
mdl = Model(name='QUBO_Example')
x1 = mdl.binary_var('x1')
x2 = mdl.binary_var('x2')

# f(x1, x2) = -2*x1 - 3*x2 + 4*x1*x2
mdl.minimize(-2*x1 - 3*x2 + 4*x1*x2)

# Docplex modelini Qiskit Optimization problemine dönüştürme
qp = from_docplex_mp(mdl)

# 2. QAOA Bileşenlerini Hazırlama
optimizer = COBYLA(maxiter=100) # Klasik optimizasyon algoritması
sampler = StatevectorSampler()             # Ölçüm alıcı

# QAOA Algoritmasını Tanımlama (p=1 katmanlı)
qaoa = QAOA(sampler=sampler, optimizer=optimizer, reps=1)

# 3. Çözücü Algoritmayı Çalıştırma
from qiskit_optimization.algorithms import MinimumEigenOptimizer
qaoa_optimizer = MinimumEigenOptimizer(qaoa)

result = qaoa_optimizer.solve(qp)

# 4. Sonucu Yazdırma
print("En iyi çözüm x1, x2:", result.x)
print("Minimum Maliyet (Minimum Energy):", result.fval)