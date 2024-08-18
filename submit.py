
# import globals
# import datetime
# import tkinter as tk

# def submit_entries(company_name_entry, job_info_entry, keywords_entry, link_entry):
#     # Retrieve the text from the entries
#     company_name = company_name_entry.get().strip()
#     job_info = job_info_entry.get().strip()
#     keywords = keywords_entry.get().strip()
#     link = link_entry.get().strip()

#     # Generate a unique ID for each submission
#     unique_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

#     # Wrap the text in HTML tags
#     company_name_html = f"<h1 name='Company Name' id='{unique_id}_{company_name}'>{company_name}</h1>"
#     job_info_html = f"<p name='Job Description'>{job_info}</p>"
#     keywords_list = [keyword.strip() for keyword in keywords.split(',')]
#     keywords_html = "<!-- Keywords -->\n<ul name='Keywords'>"
#     keywords_html += "".join(f"<li>{keyword}</li>" for keyword in keywords_list)
#     keywords_html += "</ul>"
#     link_html = f"<a name='Link' href='{link}'>{link}</a>"

#     # Print the HTML to the console
#     print("Submitted HTML:")
#     print(company_name_html)
#     print(job_info_html)
#     print(keywords_html)
#     print(link_html)

#     with open(globals.file_path, "a") as file:  # Append mode
#         file.write(f"""
#             {company_name_html}
#             {job_info_html}
#             {keywords_html}
#             {link_html}
#         """)
#     print(f"Data successfully saved to {globals.file_path}")

#     company_name_entry.delete(0, tk.END)
#     job_info_entry.delete(0, tk.END)
#     keywords_entry.delete(0, tk.END)
#     link_entry.delete(0, tk.END)
import globals
import datetime
import tkinter as tk

def submit_entries(company_name_entry, job_info_entry, keywords_entry, link_entry):
    # Retrieve the text from the entries
    company_name = company_name_entry.get().strip()
    job_info = job_info_entry.get().strip()
    keywords = keywords_entry.get().strip()
    link = link_entry.get().strip()

    # Generate a unique ID for each submission
    unique_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    # Wrap the text in HTML tags
    company_name_html = f"<h1 name='Company Name' id='{unique_id}_{company_name}'>{company_name}</h1>"
    job_info_html = f"<p name='Job Description'>{job_info}</p>"

    keywords_html = f"<h3 name='Key words'>{keywords}</h3>"

    link_html = f"<a name='Link' href='{link}'>Link</a>"

    # Print the HTML to the console
    print("Submitted HTML:")
    print(company_name_html)
    print(job_info_html)
    print(keywords_html)
    print(link_html)

    # Write to the file
    with open(globals.file_path, "a") as file:  # Append mode
        file.write(f"""
            {company_name_html}
            {job_info_html}
            {keywords_html}
            {link_html}
        """)
    print(f"Data successfully saved to {globals.file_path}")

    # Clear the entries
    company_name_entry.delete(0, tk.END)
    job_info_entry.delete(0, tk.END)
    keywords_entry.delete(0, tk.END)
    link_entry.delete(0, tk.END)
