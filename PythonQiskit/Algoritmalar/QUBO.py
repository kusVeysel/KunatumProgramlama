import numpy as np

# Q Matrisinin Oluşturulması
# f(x1, x2) = -2*x1 - 3*x2 + 4*x1*x2
# Q[0,0] = -2  (x1'in katsayısı)
# Q[1,1] = -3  (x2'nin katsayısı)
# Q[0,1] = 4   (x1 * x2 etkileşimi)

Q = np.array([
    [-2,  4],
    [ 0, -3]
])

def evaluate_qubo(x, Q):
    """f(x) = x^T * Q * x değerini hesaplar."""
    return np.dot(x.T, np.dot(Q, x))

# Tüm olasılıkların (Brute-Force) taranması
best_score = float('inf')
best_x = None

for x1 in [0, 1]:
    for x2 in [0, 1]:
        x = np.array([x1, x2])
        score = evaluate_qubo(x, Q)
        print(f"x: {x} -> Maliyet: {score}")
        
        if score < best_score:
            best_score = score
            best_x = x

print(f"\nMinimum Maliyet: {best_score}, En İyi x: {best_x}")