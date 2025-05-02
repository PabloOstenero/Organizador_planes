import tkinter as tk
from tkinter import ttk, messagebox
import heapq

# Function to create the schedule based on tasks and available hours
def create_schedule(tasks, free_hours):
    # Prioritize tasks using a max-heap (negative importance for max-heap behavior)
    prioritized_tasks = [(-importance, name, duration) for name, importance, duration in tasks]
    heapq.heapify(prioritized_tasks)
    
    # Initialize the schedule with empty slots for each day and hour
    schedule = {day: {hour: "" for hour in range(8, 20)} for day in free_hours}

    for day, hours in free_hours.items():
        sorted_hours = sorted(hours)  # Sort available hours for the day
        hour_index = 0
        remaining_hours = len(sorted_hours)
        
        while prioritized_tasks and hour_index < len(sorted_hours):
            importance, name, duration = heapq.heappop(prioritized_tasks)
            
            assigned_hours = 0
            while assigned_hours < duration and hour_index < len(sorted_hours):
                current_hour = sorted_hours[hour_index]
                
                # Check if the hour is already occupied before assigning
                if schedule[day][current_hour] == "":
                    schedule[day][current_hour] = name
                    assigned_hours += 1
                    remaining_hours -= 1
                
                hour_index += 1
                
            # If the task is not fully assigned, push the remaining part back into the heap
            if assigned_hours < duration:
                heapq.heappush(prioritized_tasks, (-importance, name, duration - assigned_hours))

            if remaining_hours <= 0:
                break

    return schedule

# Main application class for the schedule generator
class ScheduleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Schedule Generator")
        self.root.geometry("800x600")  # Set the window size
        self.tasks = []
        self.free_hours = {day: [] for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]}
        
        self.setup_ui()
    
    # Set up the user interface
    def setup_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(pady=10, expand=True)
        
        frame_tasks = ttk.Frame(notebook, padding=10)
        frame_hours = ttk.Frame(notebook, padding=10)
        frame_result = ttk.Frame(notebook, padding=10)
        
        notebook.add(frame_tasks, text="Tasks")
        notebook.add(frame_hours, text="Free Hours")
        notebook.add(frame_result, text="Generated Schedule")
        
        self.setup_tasks(frame_tasks)
        self.setup_hours(frame_hours)
        self.setup_result(frame_result)
    
    # Set up the "Tasks" tab
    def setup_tasks(self, frame):
        ttk.Label(frame, text="Task:").grid(row=0, column=0, padx=5, pady=5)
        self.task_name = ttk.Entry(frame, width=30)
        self.task_name.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Importance:").grid(row=1, column=0, padx=5, pady=5)
        self.importance = ttk.Entry(frame, width=10)
        self.importance.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(frame, text="Duration:").grid(row=2, column=0, padx=5, pady=5)
        self.duration = ttk.Entry(frame, width=10)
        self.duration.grid(row=2, column=1, padx=5, pady=5)
        
        ttk.Button(frame, text="Add Task", command=self.add_task).grid(row=3, columnspan=2, pady=10)
        
        self.task_list = tk.Listbox(frame, width=50, height=5)
        self.task_list.grid(row=4, columnspan=2, pady=10)
    
    # Set up the "Free Hours" tab
    def setup_hours(self, frame):
        ttk.Label(frame, text="Day:").grid(row=0, column=0, padx=5, pady=5)
        self.day_selector = ttk.Combobox(frame, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], state="readonly")
        self.day_selector.grid(row=0, column=1, padx=5, pady=5)
        self.day_selector.set("Monday")
        
        ttk.Label(frame, text="Hour:").grid(row=1, column=0, padx=5, pady=5)
        self.hour_selector = ttk.Combobox(frame, values=[str(i) for i in range(8, 20)], state="readonly")
        self.hour_selector.grid(row=1, column=1, padx=5, pady=5)
        self.hour_selector.set("8")
        
        ttk.Button(frame, text="Add Hour", command=self.add_hour).grid(row=2, columnspan=2, pady=10)
    
    # Set up the "Generated Schedule" tab
    def setup_result(self, frame):
        ttk.Button(frame, text="Generate Schedule", command=self.generate_schedule).pack(pady=10)
        
        # Use a Text widget with a monospaced font for better alignment
        self.result_text = tk.Text(frame, width=90, height=20, font=("Courier", 10))
        self.result_text.pack()
    
    # Add a task to the list
    def add_task(self):
        name = self.task_name.get()
        try:
            importance = int(self.importance.get())
            duration = int(self.duration.get())
        except ValueError:
            messagebox.showerror("Error", "Importance and duration must be numbers.")
            return
        
        if name and importance > 0 and duration > 0:
            self.tasks.append((name, importance, duration))
            self.task_list.insert(tk.END, f"{name} (Importance: {importance}, Duration: {duration} hrs)")
            self.task_name.delete(0, tk.END)
            self.importance.delete(0, tk.END)
            self.duration.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "All fields must be filled out and valid.")
    
    # Add a free hour to the schedule
    def add_hour(self):
        day = self.day_selector.get()
        hour = int(self.hour_selector.get())
        if hour not in self.free_hours[day]:
            self.free_hours[day].append(hour)
            messagebox.showinfo("Success", f"Hour {hour}:00 added to {day}.")
        else:
            messagebox.showinfo("Info", f"Hour {hour}:00 is already selected for {day}.")
    
    # Generate the schedule and display it
    def generate_schedule(self):
        if not self.tasks or not any(self.free_hours.values()):
            messagebox.showerror("Error", "You must add tasks and free hours.")
            return
        
        schedule = create_schedule(self.tasks, self.free_hours)
        
        # Calculate the cell width based on the longest task name
        max_task_length = max([len(task[0]) for task in self.tasks] or [0])
        cell_width = max(7, max_task_length)  # Ensure a minimum width of 7 for hours
        
        self.result_text.delete(1.0, tk.END)
        
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        header = "Hour     " + "".join([f"| {day:<{cell_width}} " for day in days]) + "|\n"
        separator = "---------" + "+".join(["-" * (cell_width + 3)] * len(days)) + "+\n"
        
        self.result_text.insert(tk.END, header)
        self.result_text.insert(tk.END, separator)
        
        for hour in range(8, 20):
            row = f"{hour:02d}:00   "  # Format the hour with two digits
            for day in days:
                task = schedule[day].get(hour, "")
                row += f"| {task:<{cell_width}} "
            row += "|\n"
            self.result_text.insert(tk.END, row)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScheduleApp(root)
    root.mainloop()
