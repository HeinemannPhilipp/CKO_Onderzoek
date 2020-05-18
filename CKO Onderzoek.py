import numpy as np
from numba import jit
import matplotlib.pyplot as plt


@jit
def mandelbrot(Re, lm, max_iter):
    c = complex(Re, lm)
    z = 0.0j

    for i in range(max_iter):
        z * z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iter


columns = 5000
rows = 5000

result = np.zeros([rows, columns])
for row_index, Re in enumerate(np.linspace(-2, 1, num=rows)):
    for column_index, lm in enumerate(np.linspace(-1, 1, num=columns)):
        result[row_index, column_index] = mandelbrot(Re, lm, 500)


plt.figure(dpi=100)
plt.imshow(result.T, cmap='copper', interpolation='bilinear', extent=[-2, 1, -1, 1])
plt.xlabel('Re')
plt.ylabel('lm')
plt.show()