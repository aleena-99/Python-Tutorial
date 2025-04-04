import numpy as np

A = np.random.randint(0, 20, (3, 3))
B = np.random.randint(0, 20, (3, 3))
C = A + B
D = A * B
transpose_D = D.T

print(C)
print(D)
print(transpose_D)
