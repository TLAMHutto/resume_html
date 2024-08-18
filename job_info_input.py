import tkinter as tk

def create_job_info_input(app):
    tk.Label(app, text="Job Info").grid(row=2, column=2)
    job_info_entry = tk.Entry(app)
    job_info_entry.grid(row=3, column=2)
    return job_info_entry
