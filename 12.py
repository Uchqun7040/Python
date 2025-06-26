import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Solver:
    def __init__(self, nmax=10, a=200):
        self.nmax = nmax
        self.a = a  # Parametr 'a'
        self.b = None
        self.t = None
        self.m = None
        self.k = None
        self.n = None
        self.q = None
        self.gamma1 = None
        self.gamma2 = None
        self.tau = None
        self.h = None

    def uxy(self, xx, tt):
        """
        Ushbu funksiya u(x, t) hisoblaydi.
        """
        res = (self.t + tt) ** -self.gamma1
        a1 = xx * (self.t + tt) ** -self.gamma2
        a1 = self.a - self.b * a1**2
        if a1 < 0:
            a1 = 0
        res *= a1 ** (1.0 / (self.m - 1.0))
        return res

    def solve(self, t, m, k, n, q):
        """
        Asosiy yechim funksiyasi.
        """
        self.t = t
        self.m = m
        self.k = k
        self.n = n
        self.q = q
        self.gamma1 = (self.n + 1) / (self.q - 1)
        self.gamma2 = ((self.q - 1) * (self.k + 1) - (self.m - 1) * (self.n + 1)) / (self.q - 1) / 2

        # self.b qiymatini nol bo'lishdan himoyalash
        if self.gamma2 == 0 or (self.m - 1.0) == 0:
            raise ValueError("self.b uchun nolga bo'lishdan saqlanish kerak. Parametrlarni qayta tekshiring.")

        self.b = self.gamma2 * (self.m - 1.0) / 2.0
        if self.b == 0:
            raise ValueError("self.b qiymati nolga teng, parametrlarni to'g'ri kiriting.")

        self.tau = self.t / self.nmax
        self.h = np.sqrt(self.a / self.b) * (2 * self.t) ** self.gamma2 / self.nmax

        # U matritsasini hisoblash
        u = np.zeros((self.nmax + 1, self.nmax + 1))
        for i in range(self.nmax + 1):
            u[0, i] = self.uxy(i * self.h, 0)
            u[i, 0] = self.uxy(0, i * self.tau)
            u[i, self.nmax] = self.uxy(self.nmax * self.h, i * self.tau)

        for i in range(1, self.nmax + 1):
            y = np.array([self.uxy(j * self.h, i * self.tau) for j in range(self.nmax + 1)])
            y2 = y.copy()
            tr = True

            while tr:
                tr = False
                alf = np.zeros(self.nmax + 1)
                bet = np.zeros(self.nmax + 1)
                alf[0] = 0
                bet[0] = y[0]

                for j in range(self.nmax):
                    aij = self._ai(j, i)
                    bij = self._bi(j, i)
                    cij = aij + bij + 1
                    alf[j + 1] = bij / (cij - aij * alf[j])
                    bet[j + 1] = (aij * bet[j] + self._fi(j, i)) / (cij - aij * alf[j])

                for j in range(self.nmax - 1, -1, -1):
                    y2[j] = alf[j + 1] * y2[j + 1] + bet[j + 1]

                if np.max(np.abs(y2 - y)) >= 0.001:
                    tr = True
                y = y2.copy()

            for j in range(1, self.nmax):
                u[i, j] = y2[j]

        return u

    def _ai(self, ii, i):
        return (self.h**2) * (self.m - 1) * ((i * self.tau + self.t)**self.k) * self.tau

    def _bi(self, ii, i):
        return (self.h**2) * (self.m - 1) * ((i * self.tau + self.t)**self.k) * self.tau

    def _fi(self, ii, i):
        return ((i * self.tau + self.t)**self.n) * self.tau * (ii**self.q) + ii

# Grafik hosil qilish
def plot_3d(u, h, tau):
    x = np.arange(0, u.shape[0]) * h
    y = np.arange(0, u.shape[1]) * tau
    X, Y = np.meshgrid(x, y)
    Z = u.T

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('T')
    ax.set_zlabel('U(x,t)')
    plt.show()

# Parametrlar
solver = Solver(nmax=50)
t = 10000
m = 1.2
k = 2.12
n = 1.1
q = 1.5

u = solver.solve(t, m, k, n, q)
plot_3d(u, solver.h, solver.tau)
