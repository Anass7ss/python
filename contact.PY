import tkinter as tk
from tkinter import messagebox

# Global list to store contacts
contacts = []

def add_contact():
    """Add a new contact."""
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    
    if name and phone:
        contacts.append({"name": name, "phone": phone})
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        update_contact_list()
    else:
        messagebox.showwarning("Input Error", "Please enter both name and phone.")

def delete_contact():
    """Delete the selected contact."""
    try:
        selected_index = contact_list.curselection()[0]
        contacts.pop(selected_index)
        update_contact_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")

def update_contact_list():
    """Update the contact list display."""
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Initialize the main application window
root = tk.Tk()
root.title("Contact Manager")
root.geometry("400x500")
root.resizable(False, False)

# Create and pack widgets
frame_top = tk.Frame(root, pady=10)
frame_top.pack()

label_title = tk.Label(frame_top, text="Contact Manager", font=("Arial", 18, "bold"))
label_title.pack()

frame_form = tk.Frame(root, pady=10)
frame_form.pack()

label_name = tk.Label(frame_form, text="Name:", font=("Arial", 12))
label_name.grid(row=0, column=0, padx=5, pady=5, sticky="e")

entry_name = tk.Entry(frame_form, width=25, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_phone = tk.Label(frame_form, text="Phone:", font=("Arial", 12))
label_phone.grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_phone = tk.Entry(frame_form, width=25, font=("Arial", 12))
entry_phone.grid(row=1, column=1, padx=5, pady=5)

button_add = tk.Button(root, text="Add Contact", command=add_contact, font=("Arial", 12), bg="#4CAF50", fg="white")
button_add.pack(pady=10)

frame_list = tk.Frame(root)
frame_list.pack(pady=10)

label_list = tk.Label(frame_list, text="Contacts:", font=("Arial", 12))
label_list.pack()

contact_list = tk.Listbox(frame_list, width=40, height=15, font=("Arial", 12))
contact_list.pack()

button_delete = tk.Button(root, text="Delete Contact", command=delete_contact, font=("Arial", 12), bg="#f44336", fg="white")
button_delete.pack(pady=10)

# Start the application loop
root.mainloop()
