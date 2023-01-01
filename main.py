# Import modules

import sqlite3

# Connect to the database

conn = sqlite3.connect("warehouse.db")
cursor = conn.cursor()

# Create the tables for products, orders and employees
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
        Initialize a product with an id, name, price and stock level.
        
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