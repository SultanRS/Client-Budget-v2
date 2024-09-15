import tkinter as tk
import sqlite3
from controller import Controller
from view import View

if __name__ == "__main__":
    root = tk.Tk()
    
    connection = sqlite3.connect("./database/Budget.db")

    controller = Controller(connection, None)
    view = View(root, controller)

    controller.view = view

    root.mainloop()

    connection.close()