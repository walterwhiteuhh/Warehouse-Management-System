# Import modules

import tkinter as tk
import sqlite3

import Employee
import Product
import Order
import Database

class App:
    def __init__(self, master):
        self.master = master
        self.db = Database('warehouse.db')
        
        # Create the widgets
        self.employee_label = tk.Label(master, text='Employee')
        self.product_label = tk.Label(master, text='Product')
        self.order_label = tk.Label(master, text='Order')
        
        
        self.employee_name_label = tk.Label(master, text='Name:')
        self.employee_role_label = tk.Label(master, text='Role:')
        self.employee_salary_label = tk.Label(master, text='Salary:')
        self.product_name_label = tk.Label(master, text='Name:')
        self.product_stock_label = tk.Label(master, text='Stock:')
        self.product_price_label = tk.Label(master, text='Price:')
        self.order_product_id_label = tk.Label(master, text='Product ID:')
        self.order_quantity_label = tk.Label(master, text='Quantity:')

        self.employee_name_entry = tk.Entry(master)
        self.employee_role_entry = tk.Entry(master)
        self.employee_salary_entry = tk.Entry(master)
        self.product_name_entry = tk.Entry(master)
        self.product_stock_entry = tk.Entry(master)
        self.product_price_entry = tk.Entry(master)
        self.order_product_id_entry = tk.Entry(master)
        self.order_quantity_entry = tk.Entry(master)
        
        self.employee_add_button = tk.Button(master, text='Add', command=self.add_employee)
        self.product_add_button = tk.Button(master, text='Add', command=self.add_product)
        self.order_add_button = tk.Button(master, text='Place', command=self.place_order)

        self.employee_view_button = tk.Button(master, text='View', command=self.view_employees)
        self.product_view_button = tk.Button(master, text='View', command=self.view_products)
        self.order_view_button = tk.Button(master, text='View', command=self.view_orders)
        
        # Set the layout
        self.employee_label.grid(row=0, column=0)
        self.product_label.grid(row=0, column=3)
        self.order_label.grid(row=0, column=6)

        self.employee_name_label.grid(row=1, column=0)
        self.employee_role_label.grid(row=2, column=0)
        self.employee_salary_label.grid(row=3, column=0)
        self.product_name_label.grid(row=1, column=3)
        self.product_stock_label.grid(row=2, column=3)
        self.product_price_label.grid(row=3, column=3)
        self.order_product_id_label.grid(row=1, column=6)
        self.order_quantity_label.grid(row=2, column=6)

        self.employee_name_entry.grid(row=1, column=1)
        self.employee_role_entry.grid(row=2, column=1)
        self.employee_salary_entry.grid(row=3, column=1)
        self.product_name_entry.grid(row=1, column=4)
        self.product_stock_entry.grid(row=2, column=4)
        self.product_price_entry.grid(row=3, column=4)
        self.order_product_id_entry.grid(row=1, column=7)
        self.order_quantity_entry.grid(row=2, column=7)

        self.employee_add_button.grid(row=1, column=2)
        self.product_add_button.grid(row=1, column=5)
        self.order_add_button.grid(row=1, column=8)

        self.employee_view_button.grid(row=4, column=2)
        self.product_view_button.grid(row=4, column=5)
        self.order_view_button.grid(row=4, column=8)

        # Create the output text box
        self.output_text = tk.Text(master)
        self.output_text.grid(row=5, column=0, columnspan=9, padx=5, pady=5)
        
        
    def add_employee(self):
        Employee(self.db, self.employee_name_entry.get(), self.employee_role_entry.get(), self.employee_salary_entry.get())

    def add_product(self):
        Product(self.db, self.product_name_entry.get(), self.product_stock_entry.get(), self.product_price_entry.get())

    def place_order(self):
        Order(self.db, self.order_product_id_entry.get(), self.order_quantity_entry.get())

    def view_employees(self):
        self.output_text.delete(1.0, tk.END)
        self.db.cursor.execute('''SELECT * FROM employees''')
        rows = self.db.cursor.fetchall()
        for row in rows:
            self.output_text.insert(tk.END, f'ID: {row[0]}, Name: {row[1]}, Role: {row[2]}, Salary: {row[3]}\n')

    def view_products(self):
        self.output_text.delete(1.0, tk.END)
        self.db.cursor.execute('''SELECT * FROM products''')
        rows = self.db.cursor.fetchall()
        for row in rows:
            self.output_text.insert(tk.END, f'ID: {row[0]}, Name: {row[1]}, Stock: {row[2]}, Price: {row[3]}\n')
   
    def view_orders(self):
        self.output_text.delete(1.0, tk.END)
        self.db.cursor.execute('''SELECT * FROM products''')
        rows = self.db.cursor.fetchall()
        for row in rows:
            self.output_text.insert(tk.END, f'ID: {row[0]}, Name: {row[1]}, Stock: {row[2]}, Price: {row[3]}\n')   

if __name__ == '__main__':
    master = tk.Tk()
    app = App(master)
    master.mainloop()