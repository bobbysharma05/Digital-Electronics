from tkinter import *
from tkinter import ttk, simpledialog
import tkinter.messagebox as tmg

rt2 = Tk()
rt2.title("JKLU\nVending Machine")
rt2.geometry("700x750")
rt2.configure(bg="light blue")

Label(rt2, text="JKLU\nVending Machine", bg="light blue", fg="black", font="Algerian 20 bold").place(x=250, y=20)
Label(rt2, text="Choose your item :", bg="light blue", fg="black", font="Algerian 20 ").place(x=50, y=118)

# IntVar for checkboxes
a_cb = IntVar(value=0)
b_cb = IntVar(value=0)
c_cb = IntVar(value=0)
d_cb = IntVar(value=0)
e_cb = IntVar(value=0)
f_cb = IntVar(value=0)
g_cb = IntVar(value=0)
h_cb = IntVar(value=0)
i_cb = IntVar(value=0)
j_cb = IntVar(value=0)
k_cb = IntVar(value=0)
l_cb = IntVar(value=0)
m_cb = IntVar(value=0)
n_cb = IntVar(value=0)

# IntVar for comboboxes
db_a = IntVar(value=10)
db_b = IntVar(value=10)
db_c = IntVar(value=10)
db_d = IntVar(value=10)
db_e = IntVar(value=10)
db_f = IntVar(value=10)
db_g = IntVar(value=10)
db_h = IntVar(value=10)
db_i = IntVar(value=10)
db_j = IntVar(value=10)
db_k = IntVar(value=10)
db_l = IntVar(value=10)
db_m = IntVar(value=10)
db_n = IntVar(value=10)

a = Checkbutton(rt2, text="French Fries = 80Rs", bg="light blue", variable=a_cb).place(x=60, y=150)
a_db = ttk.Combobox(rt2, width=5, textvariable=db_a)
a_db['values'] = tuple(range(1, db_a.get() + 1))
a_db.place(x=250, y=150)
a_db.current(0)

b = Checkbutton(rt2, text="Softy = 30Rs",bg = "light blue", variable=b_cb).place(x=60, y=200)
b_db = ttk.Combobox(rt2,width=5,textvariable=db_b)
b_db['values']=(1,2,3,4,5,6,7,8,9,10)
b_db.place(x =250 ,y =200)
b_db.current(0)

c = Checkbutton(rt2, text="Cup Cake = 20Rs",bg = "light blue", variable=c_cb).place(x=60, y=250)
c_db = ttk.Combobox(rt2,width=5,textvariable=db_c)
c_db['values']= (1,2,3,4,5,6,7,8,9,10)
c_db.place(x =250 ,y =250)
c_db.current(0)

d = Checkbutton(rt2, text="Dora Cake = 30Rs",bg = "light blue", variable=d_cb).place(x=60, y=300)
d_db = ttk.Combobox(rt2,width=5,textvariable=db_d)
d_db['values']= (1,2,3,4,5,6,7,8,9,10)
d_db.place(x =250 ,y =300)
d_db.current(0)

e = Checkbutton(rt2, text="Cold Coffee = 30Rs",bg = "light blue", variable=e_cb).place(x=60, y=350)
e_db = ttk.Combobox(rt2,width=5,textvariable=db_e)
e_db['values']= (1,2,3,4,5,6,7,8,9,10)
e_db.place(x =250 ,y =350)
e_db.current(0)

f = Checkbutton(rt2, text="Hot Coffee = 40Rs",bg = "light blue", variable=f_cb).place(x=60, y=400)
f_db = ttk.Combobox(rt2,width=5,textvariable=db_f)
f_db['values']= (1,2,3,4,5,6,7,8,9,10)
f_db.place(x =250 ,y =400)
f_db.current(0)

g = Checkbutton(rt2, text="Green Tea =30Rs",bg = "light blue", variable=g_cb).place(x=60, y=450)
g_db = ttk.Combobox(rt2,width=5,textvariable=db_g)
g_db['values']= (1,2,3,4,5,6,7,8,9,10)
g_db.place(x =250 ,y =450)
g_db.current(0)


h = Checkbutton(rt2, text="Tea = 20Rs",bg = "light blue", variable=h_cb).place(x=350, y=150)
h_db = ttk.Combobox(rt2,width=5,textvariable=db_h)
h_db['values']= (1,2,3,4,5,6,7,8,9,10)
h_db.place(x =500 ,y =150)
h_db.current(0)



i = Checkbutton(rt2, text="Ice Tea = 30Rs",bg = "light blue", variable=i_cb).place(x=350, y=200)
i_db = ttk.Combobox(rt2,width=5,textvariable=db_i)
i_db['values']= (1,2,3,4,5,6,7,8,9,10)
i_db.place(x =500 ,y =200)
i_db.current(0)



j = Checkbutton(rt2, text="Coca Cola = 40Rs",bg = "light blue", variable=j_cb).place(x=350, y=250)
j_db = ttk.Combobox(rt2,width=5,textvariable=db_j)
j_db['values']= (1,2,3,4,5,6,7,8,9,10)
j_db.place(x =500 ,y =250)
j_db.current(0)



k = Checkbutton(rt2, text="Pepsi = 40Rs",bg = "light blue", variable=k_cb).place(x=350, y=300)
k_db = ttk.Combobox(rt2,width=5,textvariable=db_k)
k_db['values']= (1,2,3,4,5,6,7,8,9,10)
k_db.place(x =500 ,y =300)
k_db.current(0)



l = Checkbutton(rt2, text="Mirinda = 40Rs",bg = "light blue", variable=l_cb).place(x=350, y=350)
l_db = ttk.Combobox(rt2,width=5,textvariable=db_l)
l_db['values']= (1,2,3,4,5,6,7,8,9,10)
l_db.place(x =500 ,y =350)
l_db.current(0)

m = Checkbutton(rt2, text="Lays = 20Rs", bg = "light blue", variable=m_cb).place(x=350, y=400)
m_db = ttk.Combobox(rt2,width=5,textvariable=db_m)
m_db['values']= (1,2,3,4,5,6,7,8,9,10)
m_db.place(x =500 ,y =400)
m_db.current(0)


n = Checkbutton(rt2, text="Kurkure = 20Rs",bg = "light blue", variable=n_cb).place(x=350, y=450)
n_db = ttk.Combobox(rt2,width=5,textvariable=db_n)
n_db['values']= (1,2,3,4,5,6,7,8,9,10)
n_db.place(x =500 ,y =450)
n_db.current(0)

Label(rt2, text="Enter Your Cash :", bg="light blue", fg="black", font=(20)).place(x=10, y=500)
Label(rt2, text="Total Bill :", bg="light blue", fg="black", font=(20)).place(x=10, y=550)
Label(rt2, text="Your Changes :", bg="light blue", fg="black", font=(20)).place(x=10, y=600)
s = IntVar()
o = Entry(rt2, font=(40), textvariable=s).place(x=200, y=500)

t = IntVar()
t1 = Entry(rt2, font=(40), textvariable=t).place(x=200, y=550)

s1 = IntVar()
p = Entry(rt2, font=(40), textvariable=s1).place(x=200, y=600)

def cancel1():
    rt2.destroy()

def clicked():
    # Get the amount entered by the user
    i = s.get()
    
    # Initialize the total bill
    total_bill = 0
    
    # Calculate the total bill based on selected items and their quantities
    if a_cb.get() == 1 and db_a.get() > 0:
        quantity = db_a.get()
        total_bill += quantity * 80

    if b_cb.get() == 1 and db_b.get() > 0:
        quantity = db_b.get()
        total_bill += quantity * 30

    if c_cb.get() == 1 and db_c.get() > 0:
        quantity = db_c.get()
        total_bill += quantity * 20
    
    if d_cb.get() == 1 and db_d.get() > 0:
        quantity = db_d.get()
        total_bill += quantity * 30

    if e_cb.get() == 1 and db_e.get() > 0:
        quantity = db_e.get()
        total_bill += quantity * 30

    if f_cb.get() == 1 and db_f.get() > 0:
        quantity = db_f.get()
        total_bill += quantity * 40

    if g_cb.get() == 1 and db_g.get() > 0:
        quantity = db_g.get()
        total_bill += quantity * 30

    if h_cb.get() == 1 and db_h.get() > 0:
        quantity = db_h.get()
        total_bill += quantity * 20

    if i_cb.get() == 1 and db_i.get() > 0:
        quantity = db_i.get()
        total_bill += quantity * 30

    if j_cb.get() == 1 and db_j.get() > 0:
        quantity = db_j.get()
        total_bill += quantity * 40

    if k_cb.get() == 1 and db_k.get() > 0:
        quantity = db_k.get()
        total_bill += quantity * 40
        
    if l_cb.get() == 1 and db_l.get() > 0:
        quantity = db_l.get()
        total_bill += quantity * 40

    if m_cb.get() == 1 and db_m.get() > 0:
        quantity = db_m.get()
        total_bill += quantity * 20

    if n_cb.get() == 1 and db_n.get() > 0:
        quantity = db_n.get()
        total_bill += quantity * 20

    # Set the total bill to the Entry widget
    t.set(total_bill)

    # Check if the entered amount is sufficient
    if i >= total_bill:
        # Calculate and set the change
        change = i - total_bill
        s1.set(change)
    else:
        # Show an error message if the amount is insufficient
        tmg.showerror('ERROR', "Insufficient amount")

def admin_access():
    password = simpledialog.askstring("Password", "Enter Admin Password:", show='*')
    if password == "admin":
        remaining_quantity = {
            "French Fries": db_a.get(),
            "Softy": db_b.get(),
            "Cup Cake": db_c.get(),
            "Dora Cake": db_d.get(),
            "Cold Coffee": db_e.get(),
            "Hot Coffee": db_f.get(),
            "Green Tea": db_g.get(),
            "Tea": db_h.get(),
            "Ice Tea": db_i.get(),
            "Coca Cola": db_j.get(),
            "Pepsi": db_k.get(),
            "Mirinda": db_l.get(),
            "Lays": db_m.get(),
            "Kurkure": db_n.get(),
        }
        remaining_text = "\n".join([f"{product}: {quantity}" for product, quantity in remaining_quantity.items()])
        tmg.showinfo("Remaining Quantity", f"Remaining Quantity:\n{remaining_text}")
    else:
        tmg.showerror("Admin Access", "Access Denied! Incorrect Password.")

Button(rt2, text="Submit", bg="white", font=(40), fg="black", command=clicked).place(x=300, y=650)
Button(rt2, text="Cancel", bg="white", font=(40), fg="black", command=cancel1).place(x=450, y=650)
Button(rt2, text="Admin", bg="white", font=(40), fg="black", command=admin_access).place(x=200, y=650)

try:
    rt2.iconbitmap("C:\\Users\\sharm.LENOVO\\Downloads\\jklu.ico")
except:
    raise

rt2.mainloop()
