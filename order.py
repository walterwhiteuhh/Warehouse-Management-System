class Order:
    def __init__(self, db, customer_name, product_id, quantity):
        """
        Initialize an order with a product, amount and employee.
        
        Parameters:
        product (Product): The product for the order.
        amount (int): The amount of the product for the order.
        employee (Employee): The employee responsible for the order.
        """
        self.db = db
        self.customer_name = customer_name
        self.product_id = product_id
        self.quantity = quantity

        # Update the stock of the product
        self.db.cursor.execute('''UPDATE products SET stock = stock - ? WHERE id = ?''', (self.quantity, self.product_id))
        self.db.commit()
        
    def calculate_total_price(self):
        """
        Calculate the total price of the order.
        
        Returns:
        int: The total price of the order.
        """
        return self.product.price * self.quantity