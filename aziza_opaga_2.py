from math import *
import numpy as np
import matplotlib.pyplot as plt


def solveInJs(U,p):
    n,m=U.shape
    shart=False
    S=-1
    while(not shart):
        Y_0=U[:,0]
        S=S+1
        shart=True
        for j in range(1,m):
            a_i=[0]*(n-2)
            a_i_1=[0]*(n-2)
            A_i=[0]*n
            B_i=[0]*n
            C_i=[0]*n
            C_i[0],C_i[-1]=[-1,-1]
            aniq=U[:,j]
            Y=[0]*n
            Y[0]=aniq[0]
            Y[-1]=aniq[-1]
            F_i=[0]*n
            F_i[0]=aniq[0]
            F_i[-1]=aniq[-1]
            alfa=[0]*(n-1)
            beta=[0]*(n-1)
            for i in range(n):
                if i!=0 and i!=(n-1):
                    # a_i[i-1]=(Y_0[i-1]**2+Y_0[i]**2)/2
                    # a_i_1[i-1]=(Y_0[i+1]**2+Y_0[i]**2)/2
                    a_i[i-1]=pow(abs(Y_0[i]-Y_0[i-1])/h_x,p-2)
                    a_i_1[i-1]=pow(abs(Y_0[i+1]-Y_0[i])/h_x,p-2)
                    A_i[i]=h_t/(h_x)**2*a_i[i-1]
                    B_i[i]=h_t/(h_x)**2*a_i_1[i-1]
                    C_i[i]=1+A_i[i]+B_i[i]
                    F_i[i]=-(Y_0[i])
                    alfa[i]=B_i[i]/(C_i[i]-alfa[i-1]*A_i[i])
                if i==0:
                    beta[i]=-F_i[i]/C_i[i]
                elif i!=(n-1):
                    beta[i]=(beta[i-1]*A_i[i]-F_i[i])/(C_i[i]-alfa[i-1]*A_i[i])
            for i in range(len(Y)-2,0,-1):
                Y[i]=Y[i+1]*alfa[i]+beta[i]
            for i in range(n):
                if abs(aniq[i]-Y[i])>eps:
                    shart=False
            Y_0=Y
            U[:,j]=Y
    return U

def graphics_3d(U_1,U_2):
    n,m=U_1.shape
    # x = np.linspace(0, x[-1], n)

    y = np.arange(1, m + 1)
    X, Y = np.meshgrid(x, y)
    Z1 = U_1.T
    Z2 = U_2.T

    fig = plt.figure(figsize=(14, 6))
    zmin1, zmax1 = Z1.min(), Z1.max()
    zmin2, zmax2 = Z2.min(), Z2.max()

    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    surf1 = ax1.plot_surface(X, Y, Z1, cmap='plasma')
    ax1.set_title("1-Grafik (U_1)")
    ax1.set_ylabel('t')
    ax1.set_zlabel('U')
    # ax1.set_xticks(np.arange(0, n + 1, 2))
    ax1.set_yticks(y)
    ax1.set_zticks(np.linspace(zmin1, zmax1, 5))
    ax1.tick_params(axis='x', labelsize=6)
    ax1.tick_params(axis='y', labelsize=6)
    ax1.tick_params(axis='z', labelsize=6)
    fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=10)

    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    surf2 = ax2.plot_surface(X, Y, Z2, cmap='plasma')
    ax2.set_title("2-Grafik (U2)")
    ax2.set_ylabel('t')
    ax2.set_zlabel('U')
    # ax2.set_xticks(np.arange(0, n + 1, 2))
    ax2.set_yticks(y)
    ax2.set_zticks(np.linspace(zmin2, zmax2, 5))
    ax2.tick_params(axis='x', labelsize=6)
    ax2.tick_params(axis='y', labelsize=6)
    ax2.tick_params(axis='z', labelsize=6)
    fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=10)

    plt.figtext(0.5, 0.95, f' ', ha='center', fontsize=15)
    plt.tight_layout()
    plt.show()

def graphics_2d(U_1,U_2):
    n, m = U_1.shape
    # x = np.linspace(0, x[-1], n)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    for i in range(m):
        ax1.plot(x, U_1[:, i], label=f't {i + 1}')
    ax1.set_title("1-Grafik (U_1)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("U")
    ax1.legend(fontsize=7)
    ax1.grid(True)

    for i in range(m):
        ax2.plot(x, U_2[:, i], label=f't {i + 1}')
    ax2.set_title("2-Grafik (U_2)")
    ax2.set_xlabel("x")
    ax2.set_ylabel("U")
    ax2.legend(fontsize=7)
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

q1=2.1
q2=2.2
p1=2.0108
p2=2.1119
b=4
a_1,a_2=[1,1]
z=300
o=15
T=float(1.0)   
h_x=float(b/z)
h_t=float(T/o)
eps=0.001

x=[]
x.append(0)
while x[-1]<b:
    # x[-1]=round(x[-1],2)
    x.append(x[-1]+h_x)
t=[]
t.append(0)
while t[-1]<T:
    t.append(t[-1]+h_t)
    # t[-1]=round(t[-1],1)

U1=np.zeros((len(x),len(t)),dtype=float)
U2=np.zeros((len(x),len(t)),dtype=float)

for i in range(len(x)):
    for j in range(len(t)):
        alfa_1=(2*(p2-1)*(p1-1)+(p2-1)*p1*q1)/(p1*p2*q1*q2-4*(p2-1)*(p1-1))
        lamda_1=(q1*q2*p2+2*q1*(p2-1)-2*(p2-1)*(p1-1)-(p2-1)*q1*p1)/(p1*p2*q1*q2-4*(p1-1)*(p2-1))
        ksi_1=x[i]*pow(T+t[j],-lamda_1)
        b_1=(p1-2)/p1*pow(lamda_1,1/(p1-1))
        fi_1=pow(a_1-b_1*pow(ksi_1,p1/(p1-1)),(p1-1)/(p1-2))
        U1[i,j]=pow(T+t[j],-alfa_1)*fi_1

for i in range(len(x)):
    for j in range(len(t)):
        alfa_2=(2*(p2-1)*(p1-1)+(p1-1)*p2*q2)/(p1*p2*q1*q2-4*(p2-1)*(p1-1))
        lamda_2=(q1*q2*p1+2*q2*(p1-1)-2*(p2-1)*(p1-1)-(p1-1)*q2*p2)/(p1*p2*q1*q2-4*(p1-1)*(p2-1))
        ksi_2=x[i]*pow(T+t[j],-lamda_2)
        b_2=(p2-2)/p2*pow(lamda_2,1/(p2-1))
        fi_2=pow(a_2-b_2*pow(ksi_2,p2/(p2-1)),(p2-1)/(p2-2))
        U2[i,j]=pow(T+t[j],-alfa_2)*fi_2


u1=solveInJs(U1,p1)
u2=solveInJs(U2,p2)
# u1=u1[5:,:]
# u2=u2[5:,:]
# x=x[:15]

graphics_2d(u1,u2)
graphics_3d(u1,u2)