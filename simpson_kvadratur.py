import numpy as np
from math import *
from sympy import symbols, Eq, linsolve, simplify, sympify,lambdify
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

A=[]
x=[]

def simpson(quyi,yuqori,soni,f_func,k_func):
    m=int(soni/2)
    h=(yuqori-quyi)/soni
    u=[]
    eq=[]
    x.clear()
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
        eq.append(Eq(simplify(eval(f_func)-q-u[i]),0))

    solutions = linsolve(eq,u)
    yechim=list(solutions)[0]
    
    return yechim
    
def submit():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        n = int(n_entry.get())
    except ValueError:
        messagebox.showwarning("Xatolik", "a, b, n lar uchun faqat son kiriting!")
    f = f_entry.get()
    k = k_entry.get()
    r = r_entry.get()
    f=f.replace('x','x[i]')
    f=f.replace('ex[i]p','exp')
    f=f.replace('^','**')
    f=f.replace('ln','log')
    f=f.strip()

    k=k.replace('x','x[i]')
    k=k.replace('w','x[j]')
    k=k.replace('ex[i]p','exp')
    k=k.replace('^','**')
    k=k.replace('ln','log')
    k=k.strip()
    
    r=r.replace('^','**')
    r=r.replace('ln','log')
    r=r.strip()
    if a or not b or not n or not f or not k:
        messagebox.showwarning("Xatolik", "Barcha maydonlarni to'ldiring!")
        return
    yechim=simpson(a,b,n,f,k)
    satr=''
    for i in range(len(yechim)):
        satr+='U['+str(i)+']='+str(yechim[i])+';\n'
    result.config(text=satr)
    result.update_idletasks()
    new_height = result.winfo_reqheight() // 20
    result.config(height=new_height,pady=20)

    
    l=0
    k=k.replace('x[i]','x')
    f=f.replace('x[i]','x')    
    print('k:',k)
    for i in range(len(yechim)):
        k1=k.replace('x[j]',str(x[i]))
        print('k1:',k1)
        l+=A[i]*eval(k1)*yechim[i]
   
    
    print('l:',l)
    grafik(str(simplify(eval(f)-l)),r)

def grafik(f1,f2):
    x = np.linspace(-10, 10, 400)
    
    x_sym = symbols('x')  
    func1 = sympify(f1)
    func2 = sympify(f2)
    func_lambda1 = lambdify(x_sym, func1, 'numpy')
    func_lambda2 = lambdify(x_sym, func2, 'numpy')
    y1 = func_lambda1(x)
    y2 = func_lambda2(x)

    fig, ax = plt.subplots()
    ax.plot(x, y1, label='sin(x)', color='blue')  
    ax.plot(x, y2, label='cos(x)', color='red')   

    ax.set_title('Grafiklar')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.axhline(0, color='black',linewidth=0.5) 
    ax.axvline(0, color='black',linewidth=0.5) 
    ax.grid(True)  
    ax.legend()  

    canvas = FigureCanvasTkAgg(fig, master=frame)  
    canvas.draw()  
    canvas.get_tk_widget().pack() 
   
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

tk.Label(root, text="Asl funksiya:").pack(pady=[10,5])
r_entry = tk.Entry(root,width=35,font=28)
r_entry.pack()

tk.Button(root, text="Hisoblash", command=submit).pack(pady=10)

tk.Label(root, text="Natija:").pack(pady=[10,5])
result = tk.Label(root,font=15,bg="#ffffff",borderwidth=0, relief="solid", width=40, wraplength=250, justify="left",height=3)
result.pack()

frame = tk.Frame(root)
frame.pack()

root.mainloop()
