import time
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def run_matrix_multiplication(size):
    A = np.random.rand(size, size).astype(np.float32)
    B = np.random.rand(size, size).astype(np.float32)

    start = time.time()
    C = np.dot(A, B)
    end = time.time()

    print(f"Matrix multiplication ({size}x{size}) took {end - start:.4f} seconds")
    return end - start

sizes = [128, 256, 512, 1024]
times = []

for size in sizes:
    t = run_matrix_multiplication(size)
    times.append(t)

plt.plot(sizes, times, marker='o')
plt.xlabel("Matrix Size (N x N)")
plt.ylabel("Time (s)")
plt.title("Matrix Multiplication Performance")
plt.grid(True)
plt.tight_layout()
plt.show()



