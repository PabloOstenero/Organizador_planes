# Organizador Planes

**What does this program do?**

This program is a schedule generator created with Python's Tkinter library. It allows the user to input a list of tasks, the importance and duration of each task, and the available free hours for each day of the week. The program then generates a schedule that assigns tasks to the available time slots, prioritizing the most important tasks. The generated schedule is displayed in a table within the application.

# **Motivation**

The main motivation behind this project is to provide a simple and efficient tool for time management. Many people struggle to organize their daily tasks and prioritize them effectively. This program aims to solve that problem by automating the assignment of tasks to available time slots, ensuring that the most important tasks are completed first. Additionally, the use of a user-friendly graphical interface makes it accessible to users with varying levels of technical experience.

# **Instructions for deployment on different platforms**

1. **Prerequisites:**
   - Make sure you have Python 3.7 or higher installed on your system.
   - Install the necessary dependencies (Tkinter is included in most Python distributions).

2. **Steps to run the program:**
   - Download the `Organizador_tareas.py` file and place it in a folder of your choice.
   - Open a terminal or command prompt.
   - Navigate to the folder where the downloaded file is located.
   - Run the program with the following command:
     ```bash
     python Organizador_tareas.py
     ```

3. **Compatible platforms:**
   - **Windows:** Run the program directly from the Windows terminal or an environment like Anaconda.
   - **MacOS:** Ensure that Tkinter is enabled in your Python installation. Run the program from the terminal.
   - **Linux:** Install Tkinter if it is not included in your Python distribution. Use your system's package manager (e.g., `sudo apt install python3-tk` on Ubuntu).

**How to use the program:**

The program has three main tabs: "Tasks," "Free Hours," and "Generated Schedule."

**"Tasks" Tab:**

- **Task:** Enter the name of the task in the "Task" field.
- **Importance:** Enter an integer representing the importance of the task in the "Importance" field. Higher numbers indicate greater importance.
- **Duration:** Enter the estimated duration of the task in hours in the "Duration" field.
- **Add Task:** Click the "Add Task" button to add the task to the task list. The task will appear in the Listbox below.

Repeat the above steps to add all your tasks.

**"Free Hours" Tab:**

- **Day:** Select the day of the week from the "Day" dropdown menu.
- **Hour:** Select the available free hour from the "Hour" dropdown menu. Hours are displayed in 24-hour format (8 to 19, corresponding to 8:00 a.m. to 7:00 p.m.).
- **Add Hour:** Click the "Add Hour" button to add the free hour to the selected day.

Repeat the above steps to add all your available free hours for each day.

**"Generated Schedule" Tab:**

- **Generate Schedule:** Once you have added all your tasks and free hours, click the "Generate Schedule" button.
- The program will generate a schedule based on your inputs and display it in a table format in the text widget below the button. The table will show the assigned tasks for each hour of each day.

**Important Considerations:**

- The program prioritizes tasks with higher importance.
- Tasks are assigned sequentially to the available free hours.
- Make sure to enter valid integers for the importance and duration of tasks.
- If a task cannot be completed in a single day, the program will continue assigning it to subsequent days as long as free hours are available.
- The schedule is generated based on the order in which you entered the tasks and free hours, along with their importance and duration.

This program is a useful tool for organizing your time and ensuring that the most important tasks are completed.

# **Examples of use**

1. **Daily task organization:**
   - Suppose you have the following tasks:
     - "Study math" (Importance: 5, Duration: 3 hours).
     - "Exercise" (Importance: 3, Duration: 1 hour).
     - "Read a book" (Importance: 2, Duration: 2 hours).
   - And you have the following free hours:
     - Monday: 8:00, 9:00, 10:00.
     - Tuesday: 8:00, 9:00.
   - When generating the schedule, the program will assign the most important tasks first, distributing them across the available days and hours.

2. **Work schedule management:**
   - A manager can use the program to assign tasks to employees based on their availability and the priority of the tasks.

3. **Study planning:**
   - Students can input their subjects and available study hours to create a schedule that allows them to cover all important subjects before exams.
