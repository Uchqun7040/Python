import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tkinter import Tk, Label, Entry, Button

# Parametrlarni saqlash uchun global o'zgaruvchilar
params = {"beta": 2.1, "p": 2.65, "m": 1.2, "q": 2.5}

def get_params():
    """Parametrlarni foydalanuvchi kiritganidan so'ng o'qish."""
    global params
    params["beta"] = float(beta_entry.get())
    params["p"] = float(p_entry.get())
    params["m"] = float(m_entry.get())
    params["q"] = float(q_entry.get())
    root.destroy()  # Formani yopish va grafikni chizish

# Tkinter oynasini yaratish
root = Tk()
root.title("Parametrlarni kiritish")

# Beta
Label(root, text="beta:").grid(row=0, column=0)
beta_entry = Entry(root)
beta_entry.insert(0, str(params["beta"]))
beta_entry.grid(row=0, column=1)

# p
Label(root, text="p:").grid(row=1, column=0)
p_entry = Entry(root)
p_entry.insert(0, str(params["p"]))
p_entry.grid(row=1, column=1)

# m
Label(root, text="m:").grid(row=2, column=0)
m_entry = Entry(root)
m_entry.insert(0, str(params["m"]))
m_entry.grid(row=2, column=1)

# q
Label(root, text="q:").grid(row=3, column=0)
q_entry = Entry(root)
q_entry.insert(0, str(params["q"]))
q_entry.grid(row=3, column=1)

# OK tugmasi
Button(root, text="OK", command=get_params).grid(row=4, column=0, columnspan=2)

root.mainloop()

# Parametrlar o'qib olindi
beta = params["beta"]
p = params["p"]
m = params["m"]
q = params["q"]

# Boshqa parametrlar
L = 10  # Bo'shliq uzunligi
T = 10  # Vaqt oralig'i
Nx = 200  # Bo'shliq bo'yicha tugunlar soni
Nt = 200  # Vaqt bo'yicha tugunlar soni

# Masofalar va vaqt qadamlarini aniqlash
dx = L / Nx
dt = T / Nt

# Boshlang'ich shart
x = np.linspace(-5, 5, Nx + 1)
t = np.linspace(0, T, Nt + 1)
u = np.zeros((Nt + 1, Nx + 1))  # Vaqt va bo'shliq bo'yicha yechim
u[0, :] = np.exp(-x**2)  # Boshlang'ich qiymat (Gaussian)

# Sonli yechim uchun iteratsion jarayon
for n in range(0, Nt):
    for i in range(1, Nx):
        # Adiabatik differensial usulga asoslangan formulalar
        u[n + 1, i] = (
            u[n, i]
            + dt * ((u[n, i + 1] - 2 * u[n, i] + u[n, i - 1]) / dx**2)**(p - 2)
            + dt * u[n, i]**beta
        )
    # Chegara shartlari
    u[n + 1, 0] = u[n, 0]**q  # chap chegara
    u[n + 1, -1] = u[n, -1]  # o'ng chegara

# 3D grafikni qurish
X, T = np.meshgrid(x, t)  # Bo'shliq va vaqt matritsasi
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")

# Sirtni chizish
surf = ax.plot_surface(X, T, u, cmap="viridis")
ax.set_xlabel("x (Bo'shliq)")
ax.set_ylabel("t (Vaqt)")
ax.set_zlabel("u (Harorat)")
ax.set_title("Issiqlik tarqalishi")
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
