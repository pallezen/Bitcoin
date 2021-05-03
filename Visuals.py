import tkinter as tk
from hash import hasher

#Creating Tk() object
m = tk.Tk()
#Tk definitions
m.title("Hasher")
m.geometry("400x200")

def print_hash():
    lbl_hash.config(text=txtbox_input.get("1.0",'end-1c') + " = " + hasher.hash(txtbox_input.get("1.0",'end-1c')))

#Label hash
lbl_hash = tk.Label(m,
    text="",
    font=("Arial",10))

#Button hash
btn_hash = tk.Button(m,text="Create hash",
    width=25,
    command=print_hash)

#Input hash Textbox
txtbox_input = tk.Text(m,
     width=25,
     height=1)


#Pack everything
txtbox_input.pack(pady=20)
btn_hash.pack(pady=20)
lbl_hash.pack(pady=20)

#Execute
m.mainloop()