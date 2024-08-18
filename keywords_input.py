import tkinter as tk

def create_keywords_input(app):
    tk.Label(app, text="Keywords").grid(row=4, column=2)
    keywords_entry = tk.Entry(app)
    keywords_entry.grid(row=5, column=2)
    return keywords_entry
