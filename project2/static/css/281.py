import tkinter as tk
w=tk.Tk()
label1=tk.Label(w,text="List Of all Computer Science Couses")
label1.pack(pady=10)
listbox1=tk.Listbox()
listbox1.insert(1,"DSA")
listbox1.insert(2,"SE")
listbox1.insert(3,"C")
listbox1.insert(4,"CPP")
listbox1.insert(5,"JAVA")
listbox1.insert(6,"PYTHON")
listbox1.insert(7,"SQL")
listbox1.pack()


w.mainloop()