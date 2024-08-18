# import tkinter as tk
# from tkinter import messagebox, Entry
# from tkinter import filedialog, simpledialog
# import os
# import time
# import threading
# import sys
# from reload import watch_files
# from company_name_input import create_company_name_input
# from job_info_input import create_job_info_input
# from keywords_input import create_keywords_input
# from link_input import create_link_input
# from submit import submit_entries
# import globals

# def run_app():
#     global app
#     app = tk.Tk()
#     app.title("Job Input Form")
#     app.geometry("240x240+1745+100")
#     def on_configure(event):
#         print(f"Window size: {event.width}x{event.height}")
#         print(f"Window position: {app.winfo_x()}x{app.winfo_y()}")

#     file_path = None

#     global company_name_var
#     global job_info_var
#     global keywords_var
#     global link_var

#     company_name_var = tk.StringVar()
#     job_info_var = tk.StringVar()
#     keywords_var = tk.StringVar()
#     link_var = tk.StringVar()

#     global company_name_entry
#     company_name_entry = create_company_name_input(app)
#     company_name_entry.config(textvariable=company_name_var)
    
#     global job_info_entry
#     job_info_entry = create_job_info_input(app)
#     job_info_entry.config(textvariable=job_info_var)

#     global keywords_entry
#     keywords_entry = create_keywords_input(app)
#     keywords_entry.config(textvariable=keywords_var)

#     global link_entry
#     link_entry = create_link_input(app)
#     link_entry.config(textvariable=link_var)

#     dir_button = tk.Button(app, text="+", command=open_directory_dialog)
#     dir_button.grid(row=10, column=1, pady=10)

#     global submit_button
#     submit_button = tk.Button(app, text="Submit", command=lambda: submit_entries(company_name_entry, job_info_entry, keywords_entry, link_entry))
#     submit_button.grid(row=10, column=2)
#     submit_button.config(state=tk.DISABLED)

#     company_name_var.trace("w", update_button_state)
#     job_info_var.trace("w", update_button_state)
#     keywords_var.trace("w", update_button_state)
#     link_var.trace("w", update_button_state)

#     app.bind("<Configure>", on_configure)
#     app.protocol("WM_DELETE_WINDOW", on_closing)  
#     app.mainloop()

# def open_directory_dialog():
#     global file_path  # Use global variable
#     directory = filedialog.askdirectory(title="Select Directory")
#     if directory:
#         file_name = simpledialog.askstring("File Name", "Enter a name for the file (without extension):")
#         if file_name:
#             globals.file_path = os.path.join(directory, f"{file_name}.txt")  # Use globals.file_path
#             print(f"File will be saved to: {globals.file_path}")
#         else:
#             print("No file name provided.")
#             globals.file_path = None
#     else:
#         print("No directory selected.")
#         globals.file_path = None

# def handle_submit():
#     if globals.file_path:
#         submit_entries(company_name_entry, job_info_entry, keywords_entry, link_entry)
#     else:
#         print("No file path specified.")

# def update_button_state(*args):
#     if all(var.get().strip() for var in [company_name_var, job_info_var, keywords_var, link_var]):
#         submit_button.config(state=tk.NORMAL)
#     else:
#         submit_button.config(state=tk.DISABLED)

# def on_configure(event):
#     x = app.winfo_x()
#     y = app.winfo_y()

# def on_closing():
#     app.quit() 

# if __name__ == "__main__":
#     print("Current working directory:", os.getcwd())  # Debugging line
#     file_path = __file__
#     base_dir = os.path.dirname(os.path.abspath(file_path))
#     input_files = [
#         os.path.join(base_dir, 'company_name_input.py'),
#         os.path.join(base_dir, 'job_info_input.py'),
#         os.path.join(base_dir, 'keywords_input.py'),
#         os.path.join(base_dir, 'link_input.py')
#     ]
    
#     # Debugging: Print the input files to check their validity
#     print("Monitoring the following files for changes:")
#     for f in input_files:
#         print(f" - {f} (Exists: {os.path.exists(f)})")  # Check if the file exists

#     threading.Thread(target=watch_files, args=(input_files,), daemon=True).start()
#     run_app()
import tkinter as tk
from tkinter import messagebox
import os
import threading
from reload import watch_files
from company_name_input import create_company_name_input
from job_info_input import create_job_info_input
from keywords_input import create_keywords_input
from link_input import create_link_input
import globals
from open_dialog import open_directory_dialog, handle_submit

def run_app():
    global app
    app = tk.Tk()
    app.title("Job Input Form")
    app.geometry("240x240+1745+100")

    def on_configure(event):
        print(f"Window size: {event.width}x{event.height}")
        print(f"Window position: {app.winfo_x()}x{app.winfo_y()}")

    global company_name_var
    global job_info_var
    global keywords_var
    global link_var

    company_name_var = tk.StringVar()
    job_info_var = tk.StringVar()
    keywords_var = tk.StringVar()
    link_var = tk.StringVar()

    global company_name_entry
    company_name_entry = create_company_name_input(app)
    company_name_entry.config(textvariable=company_name_var)
    
    global job_info_entry
    job_info_entry = create_job_info_input(app)
    job_info_entry.config(textvariable=job_info_var)

    global keywords_entry
    keywords_entry = create_keywords_input(app)
    keywords_entry.config(textvariable=keywords_var)

    global link_entry
    link_entry = create_link_input(app)
    link_entry.config(textvariable=link_var)

    dir_button = tk.Button(app, text="+", command=open_directory_dialog)
    dir_button.grid(row=10, column=1, pady=10)

    global submit_button
    submit_button = tk.Button(app, text="Submit", command=lambda: handle_submit(company_name_entry, job_info_entry, keywords_entry, link_entry))
    submit_button.grid(row=10, column=2)
    submit_button.config(state=tk.DISABLED)

    company_name_var.trace("w", update_button_state)
    job_info_var.trace("w", update_button_state)
    keywords_var.trace("w", update_button_state)
    link_var.trace("w", update_button_state)

    app.bind("<Configure>", on_configure)
    app.protocol("WM_DELETE_WINDOW", on_closing)
    app.mainloop()

def update_button_state(*args):
    if all(var.get().strip() for var in [company_name_var, job_info_var, keywords_var, link_var]) and globals.file_path:
        submit_button.config(state=tk.NORMAL)
    else:
        submit_button.config(state=tk.DISABLED)

def on_closing():
    app.quit()

if __name__ == "__main__":
    print("Current working directory:", os.getcwd())  # Debugging line
    file_path = __file__
    base_dir = os.path.dirname(os.path.abspath(file_path))
    input_files = [
        os.path.join(base_dir, 'company_name_input.py'),
        os.path.join(base_dir, 'job_info_input.py'),
        os.path.join(base_dir, 'keywords_input.py'),
        os.path.join(base_dir, 'link_input.py')
    ]
    
    # Debugging: Print the input files to check their validity
    print("Monitoring the following files for changes:")
    for f in input_files:
        print(f" - {f} (Exists: {os.path.exists(f)})")  # Check if the file exists

    threading.Thread(target=watch_files, args=(input_files,), daemon=True).start()
    run_app()
