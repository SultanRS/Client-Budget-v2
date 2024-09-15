import sqlite3

class Analyzer:
    def __init__(self, route):
        self.connection = sqlite3.connect(route)
        self.create_table()

    def create_table(self):
        """Creates Table if it doesn't exist."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS analyzers(
                    Analyzer_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Tool TEXT NOT NULL,
                    Tool_Description TEXT NOT NULL
                )
            """)
