#Emtpy :)import tkinter as tk
import psutil

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
    process_handle = open(f"/proc/{pid}/mem", "r+b")

    # TODO: Use the process handle to read and write memory

    # Close the handle to the process
    process_handle.close()

button = tk.Button(root, text="Select", command=select_process)
button.pack(pady=10)

# Run the main loop
root.mainloop()