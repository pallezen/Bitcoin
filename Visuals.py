import tkinter as tk

#Creating Tk() object
m = tk.Tk()
#Tk definitions
m.title("Hasher")
m.geometry("400x200")


#Button hash
btn_hash = tk.Button(m,text="Create hash",width=25,command=m.destroy)
btn_hash.pack(pady=20)


#Label hash
lbl_hash = tk.Label(m,
    text="Hash kommer her",
    font=("Arial",25))
lbl_hash.pack(pady=20)

#Execute
m.mainloop()