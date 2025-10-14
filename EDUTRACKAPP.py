import tkinter as tk
import customtkinter as ctk
import os
import json
import re
save = []

edu = tk.Tk()
edu.tk_setPalette('blue')
edu.geometry('1000x2000')
edu.title('EDUTRACK APP')
file1 = 'STUDENT.json'
if os.path.exists(file1):
    with open(file1, "r") as file:
        save = json.load(file)
else:
    save = []

def add():
    name = namebox.get()
    dept = deptbox.get()
    matric = matric_nobox.get()
    q1 ={'name': name, 'dept': dept, 'matric':matric}
    save.append(q1)
    namebox.delete(0, tk.END)
    matric_nobox.delete(0, tk.END)
    deptbox.delete(0, tk.END)
def show():
    text_box.delete(1.0, tk.END)
    text_box.delete(1.0, tk.END)
    if not save:
        text_box.insert(tk.END, "No records found.\n")
        return
    for s in save:
        text_box.insert(tk.END, f"Name: {s['name']} | Matric number: {s['matric']} | Department: {s['dept']}\n")

def save_data():
    with open(file1, "w") as file:
        json.dump(save, file, indent=3)

def load():
    global save
    if os.path.exists(file1):
        with open(file1, "r") as file:
            save = json.load(file)
        label_status.configure(text="📂 Data loaded successfully!")
    else:
        label_status.configure(text="⚠️ No saved data found!")



    


namebox = ctk.CTkEntry(edu, placeholder_text='NAME', font=('Italics', 20), width=500, height=20)
deptbox = ctk.CTkEntry(edu, placeholder_text='DEPARTMENT', font=('Italics', 20), width=500, height=20)
matric_nobox = ctk.CTkEntry(edu, placeholder_text='MATRIC NUMBER', font=('Italics', 20), width=500, height=20)


namebox.pack(pady= 20)
deptbox.pack(pady= 20)
matric_nobox.pack(pady= 20)




Add_button = ctk.CTkButton(master= edu, text='ADD STUDENTS RECORD', width=40, height=10, font=('Italics', 20), fg_color="#FF7433", corner_radius=8, command=add)
Add_button.pack(pady= 20)

show_button = ctk.CTkButton(master= edu, text='SHOW STUDENTS RECORD', width= 40, height=10, font=('Italics', 20), fg_color="#FF7433", corner_radius=8, command=show)
show_button.pack(pady= 20)

save_button = ctk.CTkButton(master=edu, text='SAVE STUDENTS RECORD', width=40, height=10,
                            font=('Italics', 20), fg_color="#FF7433", corner_radius=8, command=save_data)
save_button.pack(pady=20)


reload_button = ctk.CTkButton(master= edu, text='LOAD STUDENTS RECORD', width= 49, height=10, font=('Italics', 20), fg_color="#FF7433", corner_radius=8, command=load)
reload_button.pack(pady=20)

text_box = tk.Text(edu, height=50, width=200, bg='Black', font=('Bold', 20))
text_box.pack(pady=40)

label_status = ctk.CTkLabel(edu, text=" ")
edu.mainloop()
