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
        task_entry.delete("1.0",tk.END)

#delete task function
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])

#delete all tasks function
def delete_all():
    task_listbox.delete(0, tk.END)

#complete fuction
def complete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        task = task_listbox.get(index)
        if not task.startswith("✓ "):
            updated_task = "✓ " + task
            task_listbox.delete(index)
            task_listbox.insert(index, updated_task)

#top label
label = tk.Label(root, text="To-Do List",font=("Times New Roman", 30), fg="#FFFFFF", bg="#0A2947")
label.pack(pady=10)

#task entry field
task_entry = tk.Text(root, width=40, height= 3, font=("Times New Roman", 25), fg="#224C6E", bg="#DEECFC")
task_entry.pack(pady=20)

#buttons --------------------------------------------------
#add task button
add_button = tk.Button(root, text="Add Task", font=("Times New Roman", 20), command= get_task )
add_button.pack()

#delete task button
delete_button = tk.Button(root, text="Delete Task", font=("Times New Roman", 20), command = delete_task )
delete_button.pack(pady=10)

#delete all tasks button
delete_all_button = tk.Button(root, text="Clear All", font=("Times New Roman", 20), command = delete_all)
delete_all_button.pack(pady=8)

#complete task button
complete_button = tk.Button(root, text="Complete Task", font=("Times New Roman", 20), command = complete_task)
complete_button.pack(pady=10)

#listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15, font=("Times New Roman", 22), fg="#000000", bg="#E5DCFF", selectbackground="#7FEBAE")
task_listbox.pack(pady=20)

#goes at end of program
root.mainloop()