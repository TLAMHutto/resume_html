import tkinter as tk

def create_link_input(app):
    tk.Label(app, text="Link").grid(row=6, column=2)
    link_entry = tk.Entry(app)
    link_entry.grid(row=7, column=2)
    return link_entry
