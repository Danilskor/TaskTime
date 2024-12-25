import tkinter as tk
from tkinter import ttk

class TaskManagerUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("400x400")
        self.resizable(True, True)

    def start_application(self):
        self.mainloop()


UI = TaskManagerUI().start_application()