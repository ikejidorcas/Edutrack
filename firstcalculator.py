import tkinter as tk
import customtkinter as ctk
import re

a = tk.Tk()
a.geometry('280x500')
a.title('Bianca calc 📲')

def display(input):
    Question_box.insert(index=tk.INSERT, string=input)
    show_answer()

def show_answer():
    try:

        problem = Question_box.get()
        problem= problem.replace('×', '*').replace('÷', '/')
        if re.search(pattern= r'[\+\-\*\/\%]', string=problem):
            result = eval(problem)
            solution.config(text=f'= {result}')
        else:
            solution.config(text='')
    except Exception as error:
        print(error)

def to_delete():
    index = Question_box.index(tk.INSERT)-1
    Question_box.delete(index)

    show_answer()

def to_clear():
    Question_box.delete(0, tk.END)
    solution.config(text='')
    Question_box.config(font=('Bold', 20))
    solution.config(font=('Bold', 15))
def equal_to():
    Question_box.config(font=('Bold', 15))
    solution.config(font=('Bold', 25))

def change_theme():
    if a.cget('bg') == 'SystemButtonFace':
        a.tk_setPalette('black')
        Question_box.config(bg='black')
        theme.config(text='☀')
    else:
        a.tk_setPalette('SystemButtonFace')
        theme.config(text='🌙')




Question_box = tk.Entry(a, font=('Bold', 20), justify=tk.RIGHT, bd=0, bg='SystemButtonFace')
Question_box.place(x= 15, y=10, width=250, height=50)

solution = tk.Label(a,font=('Bold', 15), fg='white', anchor=tk.E, bg='blue')
solution.place(x=15, y=75,width=250, height=40 )

clear = ctk.CTkButton(master=a, text='C', width=40, height=40, font=('Bold', 30), fg_color="#FF7433", corner_radius=8, command=to_clear)
clear.place(x= 15, y=135)

delete = ctk.CTkButton(master=a, text='D', width=40, height=40, font=('Bold', 30), fg_color="#FF7433", corner_radius=8,  command=to_delete)
delete.place(x= 80, y=135)

percent = ctk.CTkButton(master=a, text='%', width=40, height=40, font=('Bold', 25), fg_color="#FF7433", corner_radius=8, command=lambda: display(input='%'))
percent.place(x= 145, y=135)

division = ctk.CTkButton(master=a, text='÷', width=40, height=40, font=('Bold', 25), fg_color="#FF7433", corner_radius=8, command=lambda: display(input='÷'))
division.place(x= 215, y=135)

num7 = ctk.CTkButton(master=a, text='7', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='7'))
num7.place(x= 15, y=210)

num8 = ctk.CTkButton(master=a, text='8', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='8'))
num8.place(x= 80, y=210)

num9 = ctk.CTkButton(master=a, text='9', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='9'))
num9.place(x= 145, y=210)

multiply = ctk.CTkButton(master=a, text='×', width=40, height=40, font=('Bold', 30),fg_color="#FF7433", corner_radius=8, command=lambda: display(input='×'))
multiply.place(x= 215, y=210)

num4 = ctk.CTkButton(master=a, text='4', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='4'))
num4.place(x= 15, y=285)

num5 = ctk.CTkButton(master=a, text='5', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='5'))
num5.place(x= 80, y=285)

num6 = ctk.CTkButton(master=a, text='6', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='6'))
num6.place(x= 145, y=285)

minus = ctk.CTkButton(master=a, text='-', width=40, height=40, font=('Bold', 25), fg_color="#FF7433", corner_radius=8, command=lambda: display(input='-'))
minus.place(x= 215, y=285)

num1 = ctk.CTkButton(master=a, text='1', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='1'))
num1.place(x= 15, y=360)

num2 = ctk.CTkButton(master=a, text='2', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='2'))
num2.place(x= 80, y=360)

num3 = ctk.CTkButton(master=a, text='3', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='3'))
num3.place(x= 145, y=360)

plus = ctk.CTkButton(master=a, text='+', width=40, height=40, font=('Bold', 30),fg_color="#FF7433", corner_radius=8, command=lambda: display(input='+'))
plus.place(x= 215, y=360)

theme = tk.Button(a, text='🌙', font=('Bold', 20), bd=0, command=change_theme)
theme.place(x= 15, y=435, width=40, height=40)

num0 = ctk.CTkButton(master=a, text='0', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='0'))
num0.place(x= 80, y=435)

dot = ctk.CTkButton(master=a, text='.', width=40, height=40, font=('Bold', 20), corner_radius=8, command=lambda: display(input='.'))
dot.place(x= 145, y=435)

equal_to = ctk.CTkButton(master=a, text='=', width=40, height=40, font=('Bold', 30),fg_color="#FF7433", corner_radius=8, command=equal_to)
equal_to.place(x= 215, y=435)
a.mainloop()