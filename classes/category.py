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
                    Manager_Hours REAL NOT NULL,
                    Is_Downloaded INTEGER NOT NULL DEFAULT 0,
                    CHECK (Is_Downloaded in (0, 1)),
                    UNIQUE (Category, Category_Type, Is_Downloaded)
                )
            """)

    def add_category(self, category, category_type, category_description, staff_hours, senior_hours, manager_hours, is_downloaded):
        with self.connection:
            self.connection.execute("""INSERT INTO categories (Category, Category_Type, Category_Description, Staff_Hours, Senior_Hours, Manager_Hours, Is_Downloaded) VALUES (:col1, :col2, :col3, :col4, :col5, :col6, :col7)""", {"col1":category,"col2":category_type,"col3":category_description,"col4":float(staff_hours),"col5":float(senior_hours),"col6":float(manager_hours),"col7":int(is_downloaded)})

    def update_category(self, category, category_type, is_downloaded, selected_fied, value):
        with self.connection:
            self.connection.execute(f"""UPDATE categories SET {selected_fied} = :value WHERE Category = :category AND Category_Type = :category_type AND Is_Downloaded = :is_downloaded""", {"value":value, "category":category, "category_type":category_type, "is_downloaded":is_downloaded})

    def get_categories(self):
        with self.connection:
            return self.connection.execute("""SELECT * FROM categories""").fetchall()
            