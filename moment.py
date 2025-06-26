import numpy as np
from math import *
import sympy as sp
import tkinter as tk
from tkinter import messagebox

def moment(a,b,f,K,lamda,fi_1):
    n=2
    fi=['']*n
    fi[0]=fi_1
    fi_0_s=fi[0].replace('x','s')
    x=sp.symbols('x')
    s=sp.symbols('s')
    fi[1]=str(sp.integrate('('+K+')'+'*'+'('+fi_0_s+')',(s,a,b)))
    alfa=[
        [0, 0],
        [0, 0]]
    beta=[
        [0, 0],
        [0, 0]]
    gamma=[0]*n
    
    for i in range(n):
        for j in range(n):
            alfa[i][j]=sp.integrate('('+fi[i]+')'+'*'+'('+fi[j]+')',(x,a,b))
            fi_s=fi[j].replace('x','s')
            beta[i][j]=sp.integrate('('+fi[i]+')'+'*'+'('+str(sp.integrate('('+K+')'+'*'+'('+fi_s+')',(s,a,b)))+')',(x,a,b))
        f_s=f.replace('x','s')
        gamma[i]=sp.integrate('('+fi[i]+')'+'*'+'('+str(sp.integrate('('+K+')'+'*'+'('+f_s+')',(s,a,b)))+')',(x,a,b))

    c_x=''
    for i in range(n):
        c_x+=('c'+str(i+1)+' ')
    c_x=c_x.rstrip()
    c_x=sp.symbols(c_x)
    eq=[]
    for i in range(n):
        q=0
        for j in range(n):
            q+=c_x[j]*(alfa[i][j]-lamda*beta[i][j])
        eq.append(sp.Eq(q,lamda*gamma[i]))
    c_i = sp.linsolve(eq,c_x)
    c_i=list(c_i)[0]
    sum=f
    for i in range(n):
        sum+='+'+str(c_i[i])+'*'+'('+fi[i]+')'
    y=sp.simplify(sum)
    print(alfa)
    print(beta)
    print(gamma)
    print(c_i)
    return y    

def submit():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        lamda = float(lamda_entry.get())
    except ValueError:
        messagebox.showwarning("Xatolik", "a, b, n lar uchun faqat son kiriting!")
    f = f_entry.get()
    fi = fi_entry.get()
    k = k_entry.get()
    f=f.replace('^','**')
    fi=fi.replace('^','**')
    k=k.replace('^','**')
    k=k.replace('ln','log')
    f=f.replace('ln','log')
    fi=fi.replace('ln','log')
    k=k.strip()
    f=f.strip()
    fi=fi.strip()
    if a or not b or not lamda or not f or not fi or not k:
        messagebox.showwarning("Xatolik", "Barcha maydonlarni to'ldiring!")
        return
    
    result.config(text=moment(a,b,f,k,lamda,fi))
    result.update_idletasks()
    new_height = result.winfo_reqheight() // 20
    result.config(height=new_height,pady=20)
   
root = tk.Tk()
root.title("Moment usuli")
root.geometry("600x700")    

tk.Label(root, text="a(quyi chegara):").pack(pady=[10,5])
a_entry = tk.Entry(root,width=35,font=28)
a_entry.pack()

tk.Label(root, text="b(yuqori chegara):").pack(pady=[10,5])
b_entry = tk.Entry(root,width=35,font=28)
b_entry.pack()

tk.Label(root, text="lyamda:").pack(pady=[10,5])
lamda_entry = tk.Entry(root,width=35,font=28)
lamda_entry.pack()

tk.Label(root, text="f(x) funksiya:").pack(pady=[10,5])
f_entry = tk.Entry(root,width=35,font=28)
f_entry.pack()

tk.Label(root, text="fi_1 funksiya:").pack(pady=[10,5])
fi_entry = tk.Entry(root,width=35,font=28)
fi_entry.pack()

tk.Label(root, text="K(x) yadro funksiya:").pack(pady=[10,5])
k_entry = tk.Entry(root,width=35,font=28)
k_entry.pack()

tk.Button(root, text="Hisoblash", command=submit).pack(pady=10)

tk.Label(root, text="Natija:").pack(pady=[10,5])
result = tk.Label(root,font=13,bg="#ffffff",borderwidth=0, relief="solid", width=40, wraplength=250, justify="left",height=3)
result.pack()


root.mainloop()