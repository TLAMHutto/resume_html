import tkinter as tk

def create_company_name_input(app):
    tk.Label(app, text="Company Name").grid(row=0, column=2)
    company_name_entry = tk.Entry(app)
    company_name_entry.grid(row=1, column=2)
    return company_name_entry