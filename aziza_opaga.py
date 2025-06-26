from math import *
import numpy as np
import matplotlib.pyplot as plt

sigma=float(2.0)
T0=float(1.0)
h_x=float(0.2)
h_t=float(0.1)
eps=0.0001
L_s=2*pi*sqrt(sigma+1)/sigma

x=[]
x.append(-L_s/2)
while x[-1]<L_s/2:
    x[-1]=round(x[-1],2)
    x.append(x[-1]+h_x)
x.remove(x[-1])
t=[]
t.append(0)
while t[-1]<T0:
    t.append(t[-1]+h_t)
    t[-1]=round(t[-1],1)
U=np.zeros((len(x),len(t)),dtype=float)

for i in range(len(x)):
    for j in range(len(t)):
        U[i][j]=sqrt(3)/2*cos(x[i]/sqrt(3))*sqrt(1/(2-t[j]))
n,m=U.shape
shart=False
S=-1
while(not shart):
    Y_0=U[:,0]
    S=S+1
    shart=True
    for j in range(1,m):
        # print("J=",j)
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
                a_i[i-1]=(Y_0[i-1]**2+Y_0[i]**2)/2
                a_i_1[i-1]=(Y_0[i+1]**2+Y_0[i]**2)/2
                A_i[i]=h_t/(h_x)**2*a_i[i-1]
                B_i[i]=h_t/(h_x)**2*a_i_1[i-1]
                C_i[i]=1+A_i[i]+B_i[i]
                F_i[i]=-(Y_0[i]+h_t*(Y_0[i]**3))
                alfa[i]=B_i[i]/(C_i[i]-alfa[i-1]*A_i[i])
            if i==0:
                beta[i]=-F_i[i]/C_i[i]
            elif i!=(n-1):
                beta[i]=(beta[i-1]*A_i[i]-F_i[i])/(C_i[i]-alfa[i-1]*A_i[i])
        for i in range(len(Y)-2,0,-1):
            Y[i]=Y[i+1]*alfa[i]+beta[i]
        for i in range(n):
            # print(abs(aniq[i]-Y[i]))
            if abs(aniq[i]-Y[i])>eps:
                shart=False
        Y_0=Y
        U[:,j]=Y

x = np.linspace(0, 28, 28)
y_values = np.arange(1, len(U[0])+1)
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
for i, y in enumerate(y_values):
    ax.plot(x, np.full_like(x, y), U[:,i], label=f'Ряд{i+1}')

ax.set_ylabel('Ряд')
ax.set_zlabel('U')
ax.set_xticks(np.arange(0,29,2))  
ax.set_yticks(y_values)                        
ax.set_zticks(np.linspace(0, 1, 11))
ax.tick_params(axis='x', labelsize=6)
ax.tick_params(axis='y', labelsize=6)
ax.tick_params(axis='z', labelsize=6)
plt.figtext(0.5, 0.95, f' ', ha='center', fontsize=15)
ax.legend()
plt.show()