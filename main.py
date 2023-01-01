class Employee:
    def __init__(self, name, salary):
        """
        Initialize an Employee with a name and salary.
        
        Parameters:
        - name (str): The name of the employee.
        - salary (int): The salary of the employee.
        """
        self.name = name
        self.salary = salary

class Product:
    def __init__(self, name, price, stock):
        """
        Initialize a product with a name, price and stock level.
        
        Parameters:
        name (str): The name of the product.
        price (int): The price of the product.
        stock (int): The stock level of the product.
        """
        self.name = name
        self.price = price
        self.stock = stock