import tkinter as tk
from tkinter import messagebox

def submit():
    ws_url = entry1.get()
    Sources = entry2.get()
    Filter = entry3.get()
    CharacterID = entry4.get()

    messagebox.showinfo("Inputs", f"Input 1: {input1}\nInput 2: {input2}\nInput 3: {input3}\nInput 4: {input4}")

root = tk.Tk()
root.title("Input Form")

tk.Label(root, text="Input 1").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Input 2").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Label(root, text="Input 3").grid(row=2, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=2, column=1)

tk.Label(root, text="Input 4").grid(row=3, column=0)
entry4 = tk.Entry(root)
entry4.grid(row=3, column=1)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2)

root.mainloop()