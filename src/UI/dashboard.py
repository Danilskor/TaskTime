import tkinter as tk
from tkinter import ttk

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.columns = ["Open", "Requires Information", "In Progress", "In Review", "Closed"]
        self.tasks = {column: [] for column in self.columns}

        self.create_widgets()
        self.tasks["Open"] = ["Task 1", "Task 2", "Task 3"]
        self.tasks["Requires Information"] = ["Task 4", "Task 5"]
        self.tasks["In Progress"] = ["Task 6"]
        self.tasks["In Review"] = ["Task 7"]
        self.tasks["Closed"] = ["Task 8", "Task 9"]

        for column, tasks in self.tasks.items():
            for task in tasks:
                self.lists[column].insert(tk.END, task)
        self.selected_task = None

    def create_widgets(self):
        self.frames = {}
        self.lists = {}

        for i, column in enumerate(self.columns):
            frame = tk.Frame(self.root)
            frame.grid(row=0, column=i, padx=10, pady=10)

            label = tk.Label(frame, text=column)
            label.pack()

            listbox = tk.Listbox(frame)
            listbox.pack()

            self.frames[column] = frame
            self.lists[column] = listbox

            listbox.bind("<Button-1>", lambda event, col=column: self.on_select(event, col))
            listbox.bind("<B1-Motion>", lambda event, col=column: self.on_drag(event, col))
            listbox.bind("<ButtonRelease-1>", lambda event, col=column: self.on_drop(event, col))

    def on_select(self, event, column):
        widget = event.widget
        self.selected_task = widget.get(widget.curselection())

    def on_drag(self, event, column):
        widget = event.widget
        self.selected_task = widget.get(widget.nearest(event.y))
        widget.delete(widget.nearest(event.y))

    def on_drop(self, event, column):
        widget = event.widget
        if widget.size() > 0:
            widget.insert(widget.nearest(event.y), self.selected_task)
        else:
            widget.insert(tk.END, self.selected_task)
        self.tasks[column].append(self.selected_task)


if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)
    root.mainloop()
