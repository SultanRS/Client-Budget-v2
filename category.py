import sqlite3

class Category:
    def __init__(self, route):
        self.connection = sqlite3.connect(route)
        self.create_table()

    def create_table(self):
        """Creates Table if it doesn't exist."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS categories(
                    Category_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Category TEXT NOT NULL,
                    Category_Description TEXT NOT NULL,
                    Staff_Hours REAL NOT NULL,
                    Senior_Hours REAL NOT NULL,
                    Manager_Hours REAL NOT NULL
                )
            """)
