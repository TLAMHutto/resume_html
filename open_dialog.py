import tkinter as tk
from tkinter import filedialog, simpledialog
import os
import uuid
import globals
from submit import submit_entries

def open_directory_dialog():
    directory = filedialog.askdirectory(title="Select Directory")
    if directory:
        file_name = simpledialog.askstring("File Name", "Enter a name for the file (without extension):")
        if file_name:
            unique_suffix = str(uuid.uuid4())
            globals.file_path = os.path.join(directory, f"{file_name}_{unique_suffix}.html")  # Include unique suffix
            print(f"File will be saved to: {globals.file_path}")
        else:
            print("No file name provided.")
            globals.file_path = None
    else:
        print("No directory selected.")
        globals.file_path = None

def handle_submit(company_name_entry, job_info_entry, keywords_entry, link_entry):
    if globals.file_path:
        submit_entries(company_name_entry, job_info_entry, keywords_entry, link_entry)
        clear_entries()  # Clear entries after submission
    else:
        print("No file path specified.")

def clear_entries():
    # Clear all entries here
    pass
