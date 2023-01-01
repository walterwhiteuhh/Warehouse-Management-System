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