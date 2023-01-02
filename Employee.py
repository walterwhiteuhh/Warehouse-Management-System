
class Employee:
    def __init__(self, db, name, role, salary):
        """
        Initialize an employee with an id, name, role and salary.
        
        Parameters:
        id (int): The id of the employee.
        name (str): The name of the employee.
        salary (int): The salary of the employee.
        """
        self.db = db
        self.name = name
        self.role = role
        self.salary = salary

        # Create the 'employees' table if it doesn't exist
        self.db.cursor.execute('''CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, role TEXT, salary REAL)''')

        # Insert the new employee into the table
        self.db.cursor.execute('''INSERT INTO employees (name, role, salary) VALUES (?, ?, ?)''', (self.name, self.role, self.salary))
        self.db.commit()