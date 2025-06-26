import numpy as np
from math import *
import sympy as sp
import tkinter as tk
from tkinter import messagebox

def kellog(a,b,K,w):
    n=4
    w0=''
    
    x=sp.symbols('x')
    t=sp.symbols('t')
    for i in range(n):
        w0=w
        w=w.replace('x','t')
        w=str(sp.integrate('('+K+')'+'*'+'('+w+')',(t,a,b)))
    w0=sqrt(sp.integrate('('+w0+')**2',(x,a,b)))
    w=sqrt(sp.integrate('('+w+')**2',(x,a,b)))
    
    res=w0/w
    return res   
# print(kellog(-pi,pi,'sin(x)*sin(t)','sin(x)'))
def submit():
    try:
        a = a_entry.get()
        b = b_entry.get()
    except ValueError:
        messagebox.showwarning("Xatolik", "a, b, n lar uchun faqat son kiriting!")
    w = w_entry.get()
    k = k_entry.get()
    w=w.replace('^','**')
    k=k.replace('^','**')
    k=k.replace('ln','log')
    w=w.replace('ln','log')
    k=k.strip()
    w=w.strip()
    if a is None or b is None or not w or not k:
        messagebox.showwarning("Xatolik", "Barcha maydonlarni to'ldiring!")
        return
    
    result.config(text=kellog(a,b,k,w))
    result.update_idletasks()
    new_height = result.winfo_reqheight() // 20
    result.config(height=new_height,pady=20)
   
root = tk.Tk()
root.title("Kolleg usuli")
root.geometry("600x700")    

tk.Label(root, text="a(quyi chegara):").pack(pady=[10,5])
a_entry = tk.Entry(root,width=35,font=28)
a_entry.pack()

tk.Label(root, text="b(yuqori chegara):").pack(pady=[10,5])
b_entry = tk.Entry(root,width=35,font=28)
b_entry.pack()

tk.Label(root, text="w(x) funksiya:").pack(pady=[10,5])
w_entry = tk.Entry(root,width=35,font=28)
w_entry.pack()

tk.Label(root, text="K(x) yadro funksiya:").pack(pady=[10,5])
k_entry = tk.Entry(root,width=35,font=28)
k_entry.pack()

tk.Button(root, text="Hisoblash", command=submit).pack(pady=10)

tk.Label(root, text="Natija:").pack(pady=[10,5])
result = tk.Label(root,font=13,bg="#ffffff",borderwidth=0, relief="solid", width=40, wraplength=250, justify="left",height=3)
result.pack()


root.mainloop()