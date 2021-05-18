import tkinter as tk
from hash import hasher
from Main import Person
from Main import Transaction


#Creating Tk() object
m = tk.Tk()
#Tk definitions
m.title("Hasher")
m.geometry("400x200")

def print_public_address():
    lbl_input.config(text="Input: " + txtbox_input.get("1.0",'end-1c') )
    lbl_public_address.config(text="Public" + " = " + hasher.hash(txtbox_input.get("1.0",'end-1c')))
    lbl_private_address.config(text="Private" + " = " + hasher.hash(hasher.hash(txtbox_input.get("1.0",'end-1c'))))


#Label hash
lbl_input = tk.Label(m,
    text="",
    font=("Arial",10))
lbl_public_address = tk.Label(m,
    text="",
    font=("Arial",10))

lbl_private_address = tk.Label(m,
    text="",
    font=("Arial",10))

#Button hash
btn_hash = tk.Button(m,text="Create hash",
    width=25,
    command=print_public_address)

#Input hash Textbox
txtbox_input = tk.Text(m,
     width=25,
     height=1)

#Pack everything
txtbox_input.pack(pady=20)
btn_hash.pack(pady=20)
lbl_input.pack()
lbl_public_address.pack()
lbl_private_address.pack()

#Execute
m.mainloop()
