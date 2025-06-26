import numpy as np
from math import *
import sympy as sp
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import messagebox


def gal_pet(n,a,b,lamda,K,f):
    if b-int(b)==0:
        b=int(b)
    fi=['']*n
    psi=['']*n
    for i in range(n):
        fi[i]='x^'+str(i+1)
        psi[i]='x^'+str(i)

    a_i_j = [[0] * n for _ in range(n)]
    b_i=[0]*n
    x=sp.symbols('x')
    s=sp.symbols('s')
    for i in range(n):
        for j in range(n):
            l_fi=fi[j].replace('x','s')
            a_i_j[i][j]=sp.integrate('('+fi[j]+')'+'*'+'('+psi[i]+')',(x,a,b))-lamda*sp.integrate('('+psi[i]+')'+'*'+'('+str(sp.integrate('('+K+')'+'*'+'('+l_fi+')',(s,a,b)))+')',(x,a,b))
        l_f=f.replace('x','s')
        b_i[i]=lamda*sp.integrate('('+psi[i]+')'+'*'+'('+str(sp.integrate('('+K+')'+'*'+'('+l_f+')',(s,a,b)))+')',(x,a,b))
    
    c_x=''
    for i in range(n):
        c_x+=('c'+str(i+1)+' ')
    c_x=c_x.rstrip()
    c_x=sp.symbols(c_x)
    eq=[]
    for i in range(n):
        q=0
        for j in range(n):
            q+=a_i_j[i][j]*c_x[j]
        eq.append(sp.Eq(q,b_i[i]))
    c_i = sp.linsolve(eq,c_x)
    c_i=list(c_i)[0]
    sum=''
    for i in range(n):
        sum+='+'+str(c_i[i])+'*'+fi[i]
    y=sp.simplify(f+sum)    
    f_y = sp.lambdify(x, y, "numpy")
    x_vals = np.linspace(0, 1, 100)
    y_vals = f_y(x_vals)  
    plt.plot(x_vals, y_vals, label='y funksiyasi')
    plt.title('y='+str(y)+' funksiyasining grafigi')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

    return 'y='+str(y)
def submit():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        n = int(n_entry.get())
        lamda = float(lamda_entry.get())

    except ValueError:
        messagebox.showwarning("Xatolik", "a, b, n, lyamdalar uchun faqat son kiriting!")
    f = f_entry.get()
    k = k_entry.get()
    f=f.replace('^','**')
    k=k.replace('^','**')
    k=k.replace('ln','log')
    f=f.replace('ln','log')
    k=k.strip()
    f=f.strip()
    if a is None or b is None or not lamda or not n or not f or not k:
        messagebox.showwarning("Xatolik", "Barcha maydonlarni to'ldiring!")
        return
    
    result.config(text=gal_pet(n,a,b,lamda,k,f))
    result.update_idletasks()
    new_height = result.winfo_reqheight() // 20
    result.config(height=new_height,pady=20)
   
root = tk.Tk()
root.title("Galyorkin Petrov")
root.geometry("600x700")    

tk.Label(root, text="a(quyi chegara):").pack(pady=[10,5])
a_entry = tk.Entry(root,width=35,font=28)
a_entry.pack()

tk.Label(root, text="b(yuqori chegara):").pack(pady=[10,5])
b_entry = tk.Entry(root,width=35,font=28)
b_entry.pack()

tk.Label(root, text="n:").pack(pady=[10,5])
n_entry = tk.Entry(root,width=35,font=28)
n_entry.pack()

tk.Label(root, text="lyamda:").pack(pady=[10,5])
lamda_entry = tk.Entry(root,width=35,font=28)
lamda_entry.pack()

tk.Label(root, text="f(x) funksiya:").pack(pady=[10,5])
f_entry = tk.Entry(root,width=35,font=28)
f_entry.pack()

tk.Label(root, text="K(x) yadro funksiya:").pack(pady=[10,5])
k_entry = tk.Entry(root,width=35,font=28)
k_entry.pack()

tk.Button(root, text="Hisoblash", command=submit).pack(pady=10)

tk.Label(root, text="Natija:").pack(pady=[10,5])
result = tk.Label(root,font=15,bg="#ffffff",borderwidth=0, relief="solid", width=40, wraplength=250, justify="left",height=3)
result.pack()

root.mainloop()



