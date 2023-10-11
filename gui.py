import tkinter as tk
from tkinter import messagebox
import psutil
import errno

# Create the main window
root = tk.Tk()
root.title("Select Process")

# Create a label with the text "Select a process"
label = tk.Label(root, text="Select a process:")
label.pack(pady=10)

# Create a listbox to display the list of processes
listbox = tk.Listbox(root)
listbox.pack(padx=10, pady=10)

# Populate the listbox with the names of the running processes
for proc in psutil.process_iter(['pid', 'name']):
    listbox.insert(tk.END, f"{proc.info['pid']} - {proc.info['name']}")

# Create a button to select the process
def select_process():
    # Get the selected process ID from the listbox
    selection = listbox.curselection()
    if len(selection) == 0:
        return
    pid = int(listbox.get(selection[0]).split()[0])

    # Open a handle to the selected process
    try:
        process_handle = open(f"/proc/{pid}/mem", "r+b")
    except IOError as e:
        if e.errno == errno.EACCES:
            tk.messagebox.showerror("Error", "Permission denied. Try running the script with elevated privileges.")
        else:
            tk.messagebox.showerror("Error", f"Error opening process handle: {e}")
        return

    # Create a text box to search the memory
    search_box = tk.Text(root, height=1)
    search_box.pack(padx=10, pady=10)

    # Create a button to search the memory
    def search_memory():
        # Get the search string from the text box
        search_string = search_box.get("1.0", tk.END).strip()

        # Search the memory for the search string
        process_handle.seek(0)
        memory_dump = process_handle.read()
        index = memory_dump.find(search_string.encode())
        if index == -1:
            tk.messagebox.showinfo("Search Results", "String not found")
        else:
            tk.messagebox.showinfo("Search Results", f"String found at offset {index}")

    search_button = tk.Button(root, text="Search", command=search_memory)
    search_button.pack(pady=10)

    # Close the handle to the process
    process_handle.close()

button = tk.Button(root, text="Select", command=select_process)
button.pack(pady=10)

# Run the main loop
root.mainloop()