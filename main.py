#setup and functions -------------------------------------------------------------------------------
import tkinter as tk
import time

#setup main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("620x850")
root.configure(bg = "#0A2947")

#update task counter function
def update_task_count():
    count = task_listbox.size()
    task_count_label.config(text=f"Total Tasks: {count}")

#function to get text from task entry
def get_task():
    task = task_entry.get("1.0", tk.END).strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete("1.0",tk.END)
    update_task_count()

#delete task function
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected[0])
    update_task_count()

#delete all tasks function
def delete_all():
    task_listbox.delete(0, tk.END)
    update_task_count()

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

#clear completed function
def clear_completed():
    for i in range(task_listbox.size() -1, -1, -1):
        if task_listbox.get(i).startswith("✓ "):
            task_listbox.delete(i)
    update_task_count()

#clock function (updates time every second)
def update_clock():
    current_time = time.strftime("%I:%M %p")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

#placeholder text functions
def add_placeholder(event):
    if task_entry.get("1.0", "end-1c") == "":
        task_entry.insert("1.0", "Enter your task here...")
        task_entry.config(fg="grey")

def remove_placeholder(event):
    if task_entry.get("1.0", "end-1c") == "Enter your task here...":
        task_entry.delete("1.0", tk.END)
        task_entry.config(fg="#224C6E")

#all GUI components -------------------------------------------------------------------------------------------------

#top label
label = tk.Label(root, text="To-Do List",font=("Times New Roman", 30), fg="#FFFFFF", bg="#0A2947")
label.grid(row=0, column=0, columnspan=4, pady=20)

#task entry field
task_entry = tk.Text(root, width=40, height= 3, font=("Times New Roman", 25), fg="#224C6E", bg="#DEECFC")
task_entry.grid(row=1, column=2, padx=35)

#buttons --------------------------------------------------
#add task button
add_button = tk.Button(root, text="Add Task", font=("Times New Roman", 20), command= get_task )
add_button.grid(row=2, columnspan=4, pady=10, sticky="w", padx=35)

#delete task button
delete_button = tk.Button(root, text="Delete Task", font=("Times New Roman", 20), command = delete_task )
delete_button.grid(row=3, columnspan=4, sticky="w", padx=35)

#delete all tasks button
delete_all_button = tk.Button(root, text="Clear All", font=("Times New Roman", 20), command = delete_all)
delete_all_button.grid(row=2, columnspan=4, sticky="e", padx=35)

#complete task button
complete_button = tk.Button(root, text="Complete Task", font=("Times New Roman", 20), command = complete_task)
complete_button.grid(row=3, columnspan=4, sticky="e", padx=35)

#clear completed tasks button
clear_completed_button = tk.Button(root, text="Clear Completed", font=("Times New Roman", 20), command = clear_completed)
clear_completed_button.grid(row=2, columnspan=4)

#remaining GUI components -----------------------------------------

#listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15, font=("Times New Roman", 22), fg="#000000", bg="#E5DCFF", selectbackground="#7FEBAE")
task_listbox.grid(row=4, column=0, columnspan=4, pady=40)

#scrollbar for listbox
scrollbar= tk.Scrollbar(root)
scrollbar.grid(row=4, column=4, sticky="ns")
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

#task counter label
task_count_label = tk.Label (root, text="Total Tasks: 0", font=("Times New Roman", 20), fg="#FFD1E5", bg="#0A2947")
task_count_label.grid(row=5, column=0, columnspan=4, pady=10)

#clock label
clock_label = tk.Label(root, font=("Times New Roman", 20), fg="#FFFFFF", bg="#0A2947")
clock_label.grid(row=6, column=0, columnspan=4)
update_clock()

#placeholder text setup
task_entry.insert("1.0", "Enter your task here...")
task_entry.config(fg="grey")
task_entry.bind("<FocusIn>", remove_placeholder)
task_entry.bind("<FocusOut>", add_placeholder)

#key binding
root.bind("<Return>", lambda event: get_task(), update_task_count())

#goes at end of program
update_task_count()
root.mainloop()