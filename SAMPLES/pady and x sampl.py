import tkinter as tk
root=tk.Tk()
root.title("bruh")
but=tk.Button(root,text="clickme", padx=10, pady=5)
but.grid(row=1, column=0)
samplelabel=tk.Label(root, text="ehe")
samplelabel.grid(row=0,column=4,padx=10,pady=5)
root.mainloop()
