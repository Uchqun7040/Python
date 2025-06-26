import numpy as np
from math import *
from sympy import symbols, Eq, linsolve, simplify
import tkinter as tk
from tkinter import messagebox

def simpson(quyi,yuqori,soni,f_func,k_func):
    m=int(soni/2)
    h=(yuqori-quyi)/soni
    u=[]
    eq=[]
    A=[]
    x=[]
    x.append(quyi)
    for i in range(2*m+1):
        A.append(h/3 if i%2==0 else 4*h/3)

    for i in range(soni):
        x.append(x[-1]+h)

    simvollar=''
    for i in range(soni+1):
        simvollar+=('u'+str(i)+' ')
    simvollar=simvollar.rstrip()
    u=symbols(simvollar)
    for i in range(len(u)):
        q=0
        for j in range(len(u)):
            q+=A[j]*eval(k_func)*u[j]
        eq.append(Eq(simplify(eval(f_func)-(q)-u[i]),0))

    solutions = linsolve(eq,u)
    yechim=list(solutions)[0]
    satr=''
    for i in range(len(yechim)):
        satr+='U['+str(i)+']='+str(yechim[i])+';\n'
    return satr

def submit():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        n = int(n_entry.get())
    except ValueError:
        messagebox.showwarning("Xatolik", "a, b, n lar uchun faqat son kiriting!")
    f = f_entry.get()
    k = k_entry.get()
    f=f.replace('x','x[i]')
    f=f.replace('ex[i]p','exp')
    k=k.replace('x','x[i]')
    k=k.replace('w','x[j]')
    k=k.replace('ex[i]p','exp')
    f=f.replace('^','**')
    k=k.replace('^','**')
    k=k.replace('ln','log')
    f=f.replace('ln','log')
    k=k.strip()
    f=f.strip()
    if a or not b or not n or not f or not k:
        messagebox.showwarning("Xatolik", "Barcha maydonlarni to'ldiring!")
        return
    
    result.config(text=simpson(a,b,n,f,k))
    result.update_idletasks()
    new_height = result.winfo_reqheight() // 20
    result.config(height=new_height,pady=20)
   
root = tk.Tk()
root.title("Simpson kvadratur")
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

tk.Label(root, text="f(x) funksiya:").pack(pady=[10,5])
f_entry = tk.Entry(root,width=35,font=28)
f_entry.pack()

tk.Label(root, text="K(x) yadro funksiya(s ni w qilib kiriting!):").pack(pady=[10,5])
k_entry = tk.Entry(root,width=35,font=28)
k_entry.pack()

tk.Button(root, text="Hisoblash", command=submit).pack(pady=10)

tk.Label(root, text="Natija:").pack(pady=[10,5])
result = tk.Label(root,font=15,bg="#ffffff",borderwidth=0, relief="solid", width=40, wraplength=250, justify="left",height=3)
result.pack()


root.mainloop()



