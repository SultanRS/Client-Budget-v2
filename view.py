import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class View:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.main_window()
    
    def on_closing(self):
        """Overwrites the program close functionality"""
        if messagebox.askokcancel("Quit", "Do you really want to quit?"):
            self.root.destroy()  # Close the window if the user confirms

    def clear_gui(self):
        """Clears the current GUI Window"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_window(self):
        self.clear_gui()
        self.root.title("Client Budget Administration Tool")
        self.root.geometry("800x600")
        tk.Label(self.root, text="Client Administration:").pack(padx=10, pady=10)
        self.button_1 = tk.Button(self.root, text="Create Client", command=self.insert_clientGUI)
        self.button_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
        #button_2 = tk.Button(self.root, text="UpdateClient", command=UpdateClientGUI)
        #button_2.pack(fill=tk.X, expand=True, padx=10, pady=5)
    
    def insert_clientGUI(self):
        self.clear_gui()
        self.root.title("Client Creation")
        self.root.geometry("400x400")

        tk.Label(self.root, text="Client ID: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.entry_1 = tk.Entry(self.root)
        self.entry_1.pack(fill=tk.X, expand=True, padx=10, pady=5)

        tk.Label(self.root, text="Client Name: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.entry_2 = tk.Entry(self.root)
        self.entry_2.pack(fill=tk.X, expand=True, padx=10, pady=5)

        tk.Label(self.root, text="Engagement ID: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.entry_3 = tk.Entry(self.root)
        self.entry_3.pack(fill=tk.X, expand=True, padx=10, pady=5)

        self.button_1 = tk.Button(self.root, text="Create", command=self.controller.add_client)
        self.button_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.button_2 = tk.Button(self.root, text="Go Back", command=self.main_window)
        self.button_2.pack(fill=tk.X, expand=True, padx=10, pady=5)

    def show_message(self, msg_type, msg):
        messagebox.showinfo(f"{msg_type}", f"{msg}")