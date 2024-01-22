# import moduls
import sqlite3
import tkinter as tk
from tkinter import messagebox

con = sqlite3.connect("dr.db")

cur = con.cursor()

try:
    cur.execute("CREATE TABLE users(id integer PRIMARY KEY AUTOINCREMENT,fullname varchar(255),username varchar(255))")
except:
    pass

def update():
    def update_sql():
        fullname1 = ent11.get()
        username1 = ent21.get()
        

        ls.delete(selected_items1)
        ls.insert(tk.END,f"id: {id_to_check} ,fullname: {fullname1} \t  | username: {username1}")
        cur.execute(f"UPDATE users SET fullname=?,username=? WHERE id={id_to_check}",[fullname1,username1])
        con.commit()
        master1.destroy()
        messagebox.showinfo("Inserted","Your Data Successfully updated")

    # برای فهمدین این که کاربر ما دیتایی سلکت کرده یا نه
    try:
        selected_items1 = ls.curselection()
        for i in selected_items1:
            id_to_check = ls.get(i).split(',')[0].split(':')[1].strip() 
        if id_to_check == None:
            '''
                از عمد اروری تولید میکنیم تا اکسپت اجرا شود
            '''
            error

        master1 = tk.Tk()
        master1.title("Insert Data")
        lbl11 = tk.Label(master1,text='Fullname')
        lbl21 = tk.Label(master1,text="Username")
        ent11 = tk.Entry(master1)
        ent21 = tk.Entry(master1)
        btn1 = tk.Button(master1,text="Submit",command=update_sql)
        lbl11.grid(row=0,column=0)
        lbl21.grid(row=1,column=0)
        ent11.grid(row=0,column=1)
        ent21.grid(row=1,column=1)
        btn1.grid(row=2,column=1)
        master1.mainloop()
    except:
        messagebox.showwarning("warning","please select data from list box for update")

    

def insert():
    def inset_sql():
        try:
            fullname = ent1.get()
            username = ent2.get()
            cur.execute("INSERT INTO users(fullname,username) VALUES(?,?)",[fullname,username])
            con.commit()
            master.destroy()
            ls.insert(tk.END,f"id: {tk.END} ,fullname: {fullname} \t  | username: {username}")
            messagebox.showinfo("Inserted","Your Data Successfully created")
        except:
            messagebox.showerror("Error","Error on Save Datas")

    master = tk.Tk()
    master.title("Insert Data")
    lbl1 = tk.Label(master,text='Fullname')
    lbl2 = tk.Label(master,text="Username")
    ent1 = tk.Entry(master)
    ent2 = tk.Entry(master)
    btn = tk.Button(master,text="Submit",command=inset_sql)
    lbl1.grid(row=0,column=0)
    lbl2.grid(row=1,column=0)
    ent1.grid(row=0,column=1)
    ent2.grid(row=1,column=1)
    btn.grid(row=2,column=1)
    master.mainloop()

def delete():
    selected_items = ls.curselection()
    for i in selected_items:
        id_to_delete = ls.get(i).split(',')[0].split(':')[1].strip() 
        print(id_to_delete)
        cur.execute("DELETE FROM users WHERE id = ?", [id_to_delete])
        ls.delete(i)
    

    con.commit()

def about():
    messagebox.showinfo("About","About You")

win = tk.Tk()
win.title("Show Users")
win.resizable(False,False)
# Menu
menu = tk.Menu(win)
win.config(menu=menu)
filemenu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Insert Data',command=insert)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=win.quit)
helpmenu = tk.Menu(menu, tearoff = 0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About',command=about)


ls = tk.Listbox(win,width=100)
users = cur.execute("SELECT * FROM users")

for i in users:
    ls.insert(tk.END,f"id: {i[0]} , fullname: {i[1]} \t  | username: {i[2]}")

frame = tk.Frame(win)
btn1 = tk.Button(frame,text='Insert Data',command=insert)
btn2 = tk.Button(frame,text="Delete Data",command=delete)
btn3 = tk.Button(frame,text="Update Data",command=update)

ls.grid(row=1,column=1)
frame.grid(row=2,column=1)
btn1.grid(row=2,column=0)
btn2.grid(row=2,column=1)
btn3.grid(row=2,column=2)



win.mainloop()