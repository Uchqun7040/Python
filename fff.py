import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Misol uchun matritsa (n=5, m=3)
U = [
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11],
    [4, 8, 12],
    [5, 9, 13],
]

U = np.array(U)  # NumPy arrayga aylantiramiz
n, m = U.shape

x = np.arange(n)  # x o‘qi uchun (0, 1, 2, ..., n-1)
x_new = np.linspace(x.min(), x.max(), 300)  # Ko'proq nuqtalar bilan silliq chiziq

# Har bir ustun (ya'ni har bir chiziq) uchun silliq chiziq chizamiz
for col in range(m):
    y = U[:, col]
    spline = make_interp_spline(x, y, k=3)  # Spline interpolatsiya (k=3 -> cubic)
    y_smooth = spline(x_new)
    plt.plot(x_new, y_smooth, label=f'Ustun {col+1}')

plt.xlabel('Qatorlar')
plt.ylabel('Qiymatlar')
plt.title('Har bir ustun uchun silliq chiziqli grafik')
plt.legend()
plt.grid(True)
plt.show()
