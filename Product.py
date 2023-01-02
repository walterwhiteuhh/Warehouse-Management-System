class Product:
    def __init__(self, db, name, stock, price):
        """
        Initialize a product with an id, name, price and stock level.
        
        Parameters:
        id (int): The id of the product.
        name (str): The name of the product.
        price (int): The price of the product.
        stock (int): The stock level of the product.
        """
        self.db = db
        self.name = name
        self.stock = stock
        self.price = price
        
        # Create the 'products' table if it doesn't exist
        self.db.cursor.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, stock INTEGER, price REAL)''')

        # Insert the new product into the table
        self.db.cursor.execute('''INSERT INTO products (name, stock, price) VALUES (?, ?, ?)''', (self.name, self.stock, self.price))
        self.db.commit()

    def update_stock(self, stock):
        """
        Update the stock level of the product by a given amount.
        
        Parameters:
        amount (int): The amount to add to the stock level. Can be positive or negative.
        """
        self.stock += stock