
import tkinter as tk
from tkinter import *
from tkinter import ttk


def add():
    itemname=Entry.get(inputitem)
    listbox.insert(3,itemname)
    
def print_selected():
    selected_indices = listbox.curselection()
    selected_values = [listbox.get(index) for index in selected_indices]
    printitem.config(text=selected_values)



def delete():
    selected=listbox.curselection()
    listbox.delete(selected)
    

window=tk.Tk()
window.geometry("900x736")

listbox=tk.Listbox()
listbox.insert(1,"Python")
listbox.insert(2,"Java")
listbox.pack()

inputitem=Entry(window, width=60)
inputitem.pack(pady=10)

addbtn=tk.Button(window, text="Add Widget", command=add)
addbtn.pack(pady=10)

printbtn=tk.Button(window, text="Print Widget", command=print)
printbtn.pack(pady=10)

deletebtn=tk.Button(window,text="Delete Widget", command=delete)
deletebtn.pack(pady=10)

printitem=tk.Label(window,text="" )
printitem.pack()

window.mainloop()