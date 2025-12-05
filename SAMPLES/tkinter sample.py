from tkinter import *
import customtkinter as cu

cu.set_appearance_mode("dark")
cu.set_default_color_theme("blue")
root=cu.CTk()
root.title("SAMPLE TKINTER")

def game():
    if check.get()=="on":
        new_varnew_var = mylb.configure(text="You clicked it...")
        
    else:
        new_varnew_var = mylb.configure(text="You didnt click it.....")
        

def clear():
    mychk.deselect()

check=cu.StringVar(value="off")
text=cu.StringVar(value="off")
mychk=cu.CTkCheckBox(root, text="game?",
                     variable=check, onvalue="on",offvalue="off",
                     checkbox_width=25,
                     checkbox_height=25,
                     font=("helvetica",18))
def new_func(check):
    check.pack(pady=40)

def new_func1(check, new_func):
    new_func(check)

new_func1(check, new_func)








root.mainloop()

