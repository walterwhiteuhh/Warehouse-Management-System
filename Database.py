import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def connect():
        """
        Connect to the database and return a cursor.
    
        Returns:
        sqlite3.Cursor: A cursor for the database connection.
        """
        # Connect to the database
        conn = sqlite3.connect("warehouse.db")
        return conn.cursor()


    def create_tables():
        """
        Create the tables for products, orders and employees in the database.
        """
        cursor = connect()
    
        # Create the tables for products, orders and employees if they do not already exist
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price INTEGER,
                stock INTEGER
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                product_id INTEGER,
                amount INTEGER,
                employee_id INTEGER, 
                FOREIGN KEY(product_id) REFERENCES products(id),  
                FOREIGN KEY(employee_id) REFERENCES employees(id)  
            )
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY, 
                name TEXT,  
                salary INTEGER  
            )
            """
        )