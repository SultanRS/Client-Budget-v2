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

    def show_message(self, msg_type, msg):
        """Function to return a messagebox"""
        messagebox.showinfo(f"{msg_type}", f"{msg}")

    def main_window(self):
        """Main Application window"""
        self.clear_gui()
        self.root.title("Client Budget Administration Tool")
        self.root.geometry("800x600")
        # Client Administration
        tk.Label(self.root, text="Client Administration:").pack(padx=10, pady=10)
        self.button_1 = tk.Button(self.root, text="Create Client", command=self.insert_clientGUI)
        self.button_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.button_2 = tk.Button(self.root, text="Update Client", command=self.update_clientGUI)
        self.button_2.pack(fill=tk.X, expand=True, padx=10, pady=5)
        # Categories Administration
        tk.Label(self.root, text="Categories Administration:").pack(padx=10, pady=10)
        self.button_3 = tk.Button(self.root, text="Create Category", command=self.insert_categoryGUI)
        self.button_3.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.button_4 = tk.Button(self.root, text="Update Category", command=self.update_categoryGUI)
        self.button_4.pack(fill=tk.X, expand=True, padx=10, pady=5)
    
    def insert_clientGUI(self):
        """Client Creation GUI"""
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

    def update_clientGUI(self):
        """Client Update GUI"""
        self.clear_gui()
        self.root.title("Update Client")
        self.root.geometry("400x400")

        list = self.controller.get_clients()

        options = [f"{client[0]}|{client[1]}" for client in list]
        
        tk.Label(self.root, text="Select client to update:").pack(padx=10, pady=10)
        self.dropdown_1 = ttk.Combobox(self.root, values=options)
        self.dropdown_1.set("Select an option")
        self.dropdown_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.dropdown_1.config(state="readonly")

        options = ["Client_ID", "Client_Name", "Eng_ID"]

        tk.Label(self.root, text="Select field to update:").pack(padx=10, pady=10)
        self.dropdown_2 = ttk.Combobox(self.root, values=options)
        self.dropdown_2.set("Select an option")
        self.dropdown_2.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.dropdown_2.config(state="readonly")

        tk.Label(self.root, text="Enter a value to be updated.").pack(padx=10, pady=10)
        self.entry_1 = tk.Entry(self.root)
        self.entry_1.pack(fill=tk.X, expand=True, padx=10, pady=5)

        self.button_1 = tk.Button(self.root, text="Update", command=self.controller.update_client)
        self.button_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.button_2 = tk.Button(self.root, text="Go Back", command=self.main_window)
        self.button_2.pack(fill=tk.X, expand=True, padx=10, pady=5)

    def insert_categoryGUI(self):
        """Category Creation GUI"""
        self.clear_gui()
        self.root.title("Create Category")
        self.root.geometry("400x470")

        tk.Label(self.root, text="Category Name: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.entry_1 = tk.Entry(self.root)
        self.entry_1.pack(fill=tk.X, expand=True, padx=10, pady=5)

        options = ["General Ledger", "Trade Receivables", "Trade Payables", "Payroll", "Inventory", "Simple Random Sample", "Property, Plant & Equipment", "Interim Review"]

        tk.Label(self.root, text="Category Type: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.dropdown_1 = ttk.Combobox(self.root, values=options)
        self.dropdown_1.set(options[0])
        self.dropdown_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.dropdown_1.config(state="readonly")

        tk.Label(self.root, text="Category Description: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.entry_2 = tk.Entry(self.root)
        self.entry_2.pack(fill=tk.X, expand=True, padx=10, pady=5)

        tk.Label(self.root, text="Staff Hours: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.entry_3 = tk.Entry(self.root)
        self.entry_3.pack(fill=tk.X, expand=True, padx=10, pady=5)

        tk.Label(self.root, text="Senior Hours: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.entry_4 = tk.Entry(self.root)
        self.entry_4.pack(fill=tk.X, expand=True, padx=10, pady=5)

        tk.Label(self.root, text="Manager Hours: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.entry_5 = tk.Entry(self.root)
        self.entry_5.pack(fill=tk.X, expand=True, padx=10, pady=5)

        self.checkbox_var1 = tk.IntVar()
        self.checkbox_1 = tk.Checkbutton(self.root, text="Is Downloaded", variable=self.checkbox_var1)
        self.checkbox_1.pack(fill=tk.X, expand=True, padx=10, pady=5)

        self.button_1 = tk.Button(self.root, text="Create", command=self.controller.add_category)
        self.button_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.button_2 = tk.Button(self.root, text="Go Back", command=self.main_window)
        self.button_2.pack(fill=tk.X, expand=True, padx=10, pady=5)

    def update_categoryGUI(self):
        """Update Category GUI"""
        self.clear_gui()
        self.root.title("Create Category")
        self.root.geometry("500x450")

        list = self.controller.get_categories()

        options = [f"{category[1]}|{category[2]}|{category[3]}|Staff: {category[4]}|Senior: {category[5]}|Manager: {category[6]}|Downloads: {category[7]}" for category in list]

        tk.Label(self.root, text="Select Category to Update: ").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.dropdown_1 = ttk.Combobox(self.root, values=options)
        self.dropdown_1.set("Select an option")
        self.dropdown_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.dropdown_1.config(state="readonly")

        options = ["Category", "Category_Type", "Category_Description", "Staff_Hours", "Senior_Hours", "Manager_Hours", "Is_Downloaded"]

        tk.Label(self.root, text="Select field to update:").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.dropdown_2 = ttk.Combobox(self.root, values=options)
        self.dropdown_2.set("Select an option")
        self.dropdown_2.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.dropdown_2.config(state="readonly")

        tk.Label(self.root, text="Enter a value to be updated.").pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.entry_1 = tk.Entry(self.root)
        self.entry_1.pack(fill=tk.X, expand=True, padx=10, pady=5)

        self.button_1 = tk.Button(self.root, text="Update", command=self.controller.update_category)
        self.button_1.pack(fill=tk.X, expand=True, padx=10, pady=5)
        self.button_2 = tk.Button(self.root, text="Go Back", command=self.main_window)
        self.button_2.pack(fill=tk.X, expand=True, padx=10, pady=5)