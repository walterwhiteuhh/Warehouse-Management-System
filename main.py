# Import modules

import sqlite3

# Connect to the database

conn = sqlite3.connect("warehouse.db")
cursor = conn.cursor()

# Create the tables for products, orders and employees
cursor.execute(
    """
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,  # Unique ID for each product
        name TEXT,  # Name of the product
        price INTEGER,  # Price of the product
        stock INTEGER  # Stock level of the product
    )
    """
)
cursor.execute(
    """
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,  # Unique ID for each order
        product_id INTEGER,  # ID of the product for the order
        amount INTEGER,  # Amount of the product for the order
        employee_id INTEGER,  # ID of the employee responsible for the order
        FOREIGN KEY(product_id) REFERENCES products(id),  # Foreign key for product ID
        FOREIGN KEY(employee_id) REFERENCES employees(id)  # Foreign key for employee ID
    )
    """
)
cursor.execute(
    """
    CREATE TABLE employees (
        id INTEGER PRIMARY KEY,  # Unique ID for each employee
        name TEXT,  # Name of the employee
        salary INTEGER  # Salary of the employee
    )
    """
)

class Employee:
    def __init__(self, id, name, salary):
        """
        Initialize an employee with an id, name and salary.
        
        Parameters:
        id (int): The id of the employee.
        name (str): The name of the employee.
        salary (int): The salary of the employee.
        """
        self.id = id
        self.name = name
        self.salary = salary

class Product:
    def __init__(self, id, name, price, stock):
        """
        Initialize a product with a name, price and stock level.
        
        Parameters:
        id (int): The id of the product.
        name (str): The name of the product.
        price (int): The price of the product.
        stock (int): The stock level of the product.
        """
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        

    def update_stock(self, amount):
        """
        Update the stock level of the product by a given amount.
        
        Parameters:
        amount (int): The amount to add to the stock level. Can be positive or negative.
        """
        self.stock += amount
        
class Order:
    def __init__(self, product, amount, employee):
        """
        Initialize an order with a product, amount and employee.
        
        Parameters:
        product (Product): The product for the order.
        amount (int): The amount of the product for the order.
        employee (Employee): The employee responsible for the order.
        """
        self.product = product
        self.amount = amount
        self.employee = employee

    def calculate_total_price(self):
        """
        Calculate the total price of the order.
        
        Returns:
        int: The total price of the order.
        """
        return self.product.price * self.amount