import sqlite3

class Category:
    def __init__(self, connection):
        self.connection = connection
        self.create_table()

    def create_table(self):
        """Creates Table if it doesn't exist."""
        with self.connection:
            self.connection.execute("""
                CREATE TABLE IF NOT EXISTS categories(
                    Category_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Category TEXT NOT NULL,
                    Category_Type TEXT NOT NULL,
                    Category_Description TEXT NOT NULL,
                    Staff_Hours REAL NOT NULL,
                    Senior_Hours REAL NOT NULL,
                    Manager_Hours REAL NOT NULL
                )
            """)

    def add_category(self, category, category_type, category_description, staff_hours, senior_hours, manager_hours):
        with self.connection:
            self.connection.execute("""INSERT INTO categories (Category, Category_Type, Category_Description, Staff_Hours, Senior_Hours, Manager_Hours) VALUES (:col1, :col2, :col3, :col4, :col5, :col6)""", {"col1":category,"col2":category_type,"col3":category_description,"col4":float(staff_hours),"col5":float(senior_hours),"col6":float(manager_hours)})