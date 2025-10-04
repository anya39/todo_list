import tkinter as tk

#setup main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x700")
root.configure(bg = "#0A2947")

#function to get text from task entry
def get_task():
    task = task_entry.get("1.0", tk.END).strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete("1",tk.END)

#top label
label = tk.Label(root, text="To-Do List",font=("Times New Roman", 30), fg="#FFFFFF", bg="#0A2947")
label.pack(pady=10)

#task entry field
task_entry = tk.Text(root, width=40, height= 3, font=("Times New Roman", 25), fg="#224C6E", bg="#DEECFC")
task_entry.pack(pady=20)


#add task button
add_button = tk.Button(root, text="Add Task", font=("Times New Roman", 20), command= get_task )
add_button.pack()

#listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15, font=("Times New Roman", 22), fg="#000000", bg="#E5DCFF", selectbackground="#7FEBAE")
task_listbox.pack(pady=20)

#goes at end of program
root.mainloop()