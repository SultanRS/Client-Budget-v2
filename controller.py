from client import Client
import sqlite3

class Controller:
    def __init__(self, connection, view):
        self.client_model = Client(connection)
        self.view = view
        # category
        # analyzer
        # budget

    def add_client(self):
        client_id = self.view.entry_1.get()
        client_name = self.view.entry_2.get()
        eng_id = self.view.entry_3.get()

        validation = self.client_model.validate_duplicated(client_id, client_name)
        print(validation)
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