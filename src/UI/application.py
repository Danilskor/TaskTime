import tkinter as tk
from tkinter import ttk
import webbrowser
import pyperclip


if __name__ == '__main__':
    import os
    import sys
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    sys.path.insert(0, root_path)
from src.YandexAPI.authorization import YandexAuth

class TaskManagerUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager")
        self.geometry("400x400")
        self.resizable(True, True)

        self.text_label = ttk.Label(self, text="Вы можете открыть ссылку на авторизацию в браузере или скопировать ее.")
        self.text_label.pack(pady=10)

        self.login_button = ttk.Button(self, text="Перейти в браузер", command=self.auth_browser)
        self.login_button.pack(side=tk.LEFT, pady=20)

        self.OK_button = ttk.Button(self, text="Копировать ссылку", command=self.copy_auth_link)
        self.OK_button.pack(side=tk.RIGHT,pady=20)

        self.auth_code_entry = ttk.Entry(self)
        self.auth_code_entry.pack(pady=20)

        self.OK_button = ttk.Button(self, text="ОК", command=self.get_headers)
        self.OK_button.pack(pady=20)

    def login(self):
        self.auth = YandexAuth()
        auth_code = self.auth_code_entry.get()
        self.auth.get_access_token(auth_code)
        self.auth.get_headers()
    
    def auth_browser(self):
        auth_url = self.auth.get_auth_url()
        webbrowser.open(auth_url)

    def copy_auth_link(self):
        auth_url = self.auth.get_auth_url()
        pyperclip.copy(auth_url)

    def start_application(self):
        self.mainloop()
    
    def get_headers(self):
        return self.auth.get_headers()
    



UI = TaskManagerUI()
UI.start_application()

