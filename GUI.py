import tkinter as tk
from tkinter import messagebox

def submit():
    ws_url = entry1.get()
    Sources = entry2.get()
    Filter = entry3.get()
    CharacterID = entry4.get()

    messagebox.showinfo("Inputs", f"Input 1: {ws_url}\nInput 2: {Sources}\nInput 3: {Filter}\nInput 4: {CharacterID}")

root = tk.Tk()
root.title("OBSHitPointSync")

tk.Label(root, text="OBS URL").grid(column=0, row=0, padx=10, pady=5)
entry1 = tk.Entry(root, width=50)
entry1.grid(row=0, column=1)
entry1.insert(0, "ws://localhost:4444")

tk.Label(root, text="Source Name").grid(row=1, column=0, padx=10, pady=5)
entry2 = tk.Entry(root, width=50)
entry2.grid(row=1, column=1)

tk.Label(root, text="Filter Name").grid(row=2, column=0, padx=10, pady=5)
entry3 = tk.Entry(root, width=50)
entry3.grid(row=2, column=1)

tk.Label(root, text="Character ID").grid(row=3, column=0, padx=10, pady=5)
entry4 = tk.Entry(root, width=50)
entry4.grid(row=3, column=1)


submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()