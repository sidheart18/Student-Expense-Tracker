import tkinter as tk
from tkinter import messagebox
from database import create_table, insert_expense

create_table()

root = tk.Tk()
root.title("Student Expense Tracker")
root.geometry("400x400")

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Date (DD-MM-YYYY)").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Note").pack()
note_entry = tk.Entry(root)
note_entry.pack()

def add_expense():
    category = category_entry.get()
    amount = amount_entry.get()
    date = date_entry.get()
    note = note_entry.get()

    if not category or not amount or not date:
        messagebox.showwarning("Error", "Please fill required fields")
        return

    insert_expense(category, float(amount), date, note)
    messagebox.showinfo("Success", "Expense added")

    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)

tk.Button(root, text="Add Expense", command=add_expense).pack(pady=10)

root.mainloop()
