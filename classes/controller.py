from .client import Client
from .category import Category
import sqlite3

class Controller:
    def __init__(self, connection, view):
        self.client_model = Client(connection)
        self.category_model = Category(connection)
        self.view = view
        # analyzer
        # budget

    def get_clients(self):
        """Gets the list of clients"""
        return self.client_model.get_clients()

    def add_client(self):
        """Adds a client to the database getting view entries and inserting them into client model"""
        client_id = self.view.entry_1.get()
        client_name = self.view.entry_2.get()
        eng_id = self.view.entry_3.get()

        validation = self.client_model.validate_duplicated(client_id, client_name)

        if not client_id or not client_name:
            self.view.show_message("ERROR", "You must fill the first two fields.")
        elif len(validation) != 0:
            self.view.show_message("ERROR", f"ERROR: Client ID: {client_id} with Name {client_name} already exists.")
        else:
            result = self.client_model.get_maxID(client_id)
            max_id = []

            if len(result) != 0:
                for entities in result:
                    for entity in entities:
                        max_id.append(int(entity.split("-")[-1]))
                max_id = str(max(max_id)+1)
            else:
                max_id = "1"

            try:
                self.client_model.add_client(client_id+"-"+max_id, client_name, eng_id)
                self.view.show_message("INFO", "Client successfully created.")
            except sqlite3.IntegrityError:
                self.view.show_message("ERROR", f"Client ID {client_id} already exists!")
        
    def update_client(self):
        """Updates a client getting the values from the view and passing them into client model."""
        selected_id = self.view.dropdown_1.get()
        selected_field = self.view.dropdown_2.get()
        value = self.view.entry_1.get()
        if selected_id == "Select an option" or selected_field == "Select an option":
            self.view.show_message("ERROR","You must select a value from both dropdown lists.")
        elif not value:
            self.view.show_message("ERROR","You must input a value to update.")
        else:
            selected_id = selected_id.split("|")[0]
            try:
                self.client_model.update_client(selected_id, selected_field, value)
                self.view.show_message("INFO", "Client successfully updated.")
                self.view.update_clientGUI()
            except sqlite3.IntegrityError:
                self.view.show_message("ERROR", f"Client ID {selected_id} already exists!")

    def add_category(self):
        """Adds a category to the database getting view entries and inserting them into category model"""
        category, category_type, category_description, staff_hours, senior_hours, manager_hours = self.view.entry_1.get(), self.view.dropdown_1.get(), self.view.entry_2.get(), self.view.entry_3.get(), self.view.entry_4.get(), self.view.entry_5.get()

        if not category or not category_description or not staff_hours or not senior_hours or not manager_hours:
            self.view.show_message("ERROR", "You must fill all entries.")
        else:
            try:
                self.category_model.add_category(category, category_type, category_description, staff_hours, senior_hours, manager_hours)
                self.view.show_message("INFO", "Category successfully updated.")
            except sqlite3.IntegrityError:
                self.view.show_message("ERROR", "UNDEFINED ERROR.")