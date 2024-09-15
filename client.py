import sqlite3

class Client:
    def __init__(self, connection):
        self.connection = connection
        self.create_table()

    def create_table(self):
        """Creates Table if it doesn't exist."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS clients(
                    Client_ID TEXT PRIMARY KEY NOT NULL,
                    Client_Name TEXT NOT NULL,
                    Eng_ID TEXT
                )
            """)
    
    def add_client(self, client_id, client_name, eng_id):
        """Adds a new client in the database"""
        with self.connection:
            self.connection.execute("""INSERT INTO clients VALUES (:col1, :col2, :col3)""", {"col1":client_id, "col2":client_name, "col3":eng_id})

    def update_client(self, selected_id, selected_field, value):
        """Updates an existing client in the database"""
        with self.connection:
            self.connection.execute(f"""UPDATE clients SET {selected_field} = :value WHERE Client_ID = :selected""", {"value":value, "selected":selected_id})

    def get_clients(self):
        """Queries all existing clients"""
        with self.connection:
            return self.connection.execute("""SELECT * FROM clients""")

    def validate_duplicated(self, client_id, client_name):
        """This function returns if there is a client with the same ID and Name."""
        with self.connection:
            return self.connection.execute("""SELECT Client_ID, Client_Name FROM clients WHERE Client_ID LIKE :val1 AND Client_Name = :val2""", {"val1":client_id+"%","val2":client_name}).fetchall()

    def get_maxID(self, client_id):
        with self.connection:
            return self.connection.execute("""SELECT Client_ID FROM clients WHERE Client_ID LIKE :val""", {"val":client_id+"%"}).fetchall()