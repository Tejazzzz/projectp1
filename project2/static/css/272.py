import tkinter as tk

def convert():
    decinum_int = float(inputdeci.get())
    decinum=int(decinum_int)
    binary=bin(decinum)
    octal=oct(decinum)
    Hexadeci=hex(decinum)
    DisplayBi.config(text=str(binary))
    DisplayOct.config(text=str(octal))
    DisplayHexa.config(text=str(Hexadeci))
w=tk.Tk()
w.geometry("900x700")

msg=tk.Label(w,text="Please Enter Any Decimal No")
msg.pack(pady=10)
inputdeci=(tk.Entry(w,width=60))
inputdeci.pack(pady=10)
subbtn=tk.Button(w,width=60, text="Convert Into Binary Octal And Hexa Decimal Number",command=convert)
subbtn.pack(pady=10)
DisplayBi=tk.Label(w, text="")
DisplayBi.pack(pady=10)
DisplayOct=tk.Label(w, text="")
DisplayOct.pack(pady=10)
DisplayHexa=tk.Label(w, text="")
DisplayHexa.pack(pady=10)

w.mainloop()