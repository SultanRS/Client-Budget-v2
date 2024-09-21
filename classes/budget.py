import sqlite3

class Budget:
    def __init__(self, route):
        self.connection = sqlite3.connect(route)
        self.create_table()

    def create_table(self):
        """Creates Table if it doesn't exist."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS budgets(
                    Client_ID TEXT PRIMARY KEY NOT NULL,
                    Category_ID INTEGER NOT NULL,
                    Analyzer_ID INTEGER NOT NULL,
                    Staff_Hours REAL NOT NULL,
                    Senior_Hours REAL NOT NULL,
                    Manager_Hours REAL NOT NULL,
                    Is_Dummy INTEGER NOT NULL DEFAULT 0,
                    Is_Load_Only INTEGER NOT NULL DEFAULT 0,
                    Is_Download_Only INTEGER NOT NULL DEFAULT 0,
                    Custom_Hours INTEGER NOT NULL DEFAULT 0,
                    FOREIGN KEY (Client_ID) REFERENCES clients(Client_ID) ON UPDATE CASCADE,
                    FOREIGN KEY (Category_ID) REFERENCES categories(Category_ID) ON UPDATE CASCADE,
                    FOREIGN KEY (Analyzer_ID) REFERENCES analyzers(Analyzer_ID) ON UPDATE CASCADE
                )
            """)
