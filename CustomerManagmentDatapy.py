import pypyodbc as odbc
from faker import Faker
from random import randint, choice
from datetime import datetime, timedelta


fake = Faker()


DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'EGY-W-064'
DATABASE_NAME = 'CustomerManagement'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={{{SERVER_NAME}}};
    DATABASE={{{DATABASE_NAME}}};
    Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)
cursor = conn.cursor()

def random_date(start, end):
    return start + timedelta(days=randint(0, (end - start).days))

# Insert data into Customers table with phone number fix (remove extensions)
def insert_customers(n):
    for _ in range(n):
        full_name = fake.name()
        email = fake.email()
        phone = fake.phone_number()[:15]  
        shipping_address = fake.address()
        billing_address = fake.address()
        dob = random_date(datetime(1970, 1, 1), datetime(2000, 12, 31))
        loyalty_points = randint(0, 500)
        
        cursor.execute("""
            INSERT INTO Customers (FullName, Email, PhoneNumber, ShippingAddress, BillingAddress, DateOfBirth, LoyaltyPoints)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (full_name, email, phone, shipping_address, billing_address, dob, loyalty_points))
    conn.commit()

# Insert data into Orders table
def insert_orders(n):
    for _ in range(n):
        customer_id = randint(1, 100)
        order_date = random_date(datetime(2020, 1, 1), datetime.now())
        shipping_address = fake.address()
        billing_address = fake.address()
        order_total = round(fake.random_number(digits=5), 2)
        payment_method = choice(['Credit Card', 'PayPal', 'Bank Transfer'])
        order_status = choice(['Pending', 'Shipped', 'Delivered', 'Canceled'])
        
        cursor.execute("""
            INSERT INTO Orders (CustomerID, OrderDate, ShippingAddress, BillingAddress, OrderTotal, PaymentMethod, OrderStatus)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (customer_id, order_date, shipping_address, billing_address, order_total, payment_method, order_status))
    conn.commit()

# Insert data into Order Items table
def insert_order_items(n):
    for _ in range(n):
        order_id = randint(1, 100)
        product_id = randint(1, 50)
        quantity = randint(1, 10)
        unit_price = round(fake.random_number(digits=4), 2)
        total_price = round(quantity * unit_price, 2)
        
        cursor.execute("""
            INSERT INTO OrderItems (OrderID, ProductID, Quantity, UnitPrice, TotalPrice)
            VALUES (?, ?, ?, ?, ?)
        """, (order_id, product_id, quantity, unit_price, total_price))
    conn.commit()

# Insert data into Products table
def insert_products(n):
    for _ in range(n):
        product_name = fake.word()
        category_id = randint(1, 10)
        brand_id = randint(1, 5)
        price = round(fake.random_number(digits=4), 2)
        stock_quantity = randint(0, 1000)
        rating = round(fake.random_number(digits=1), 2)
        description = fake.text()
        
        cursor.execute("""
            INSERT INTO Products (ProductName, CategoryID, BrandID, Price, StockQuantity, Rating, Description)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (product_name, category_id, brand_id, price, stock_quantity, rating, description))
    conn.commit()

# Insert data into Categories table
def insert_categories(n):
    for _ in range(n):
        category_name = fake.word()
        description = fake.text()
        
        cursor.execute("""
            INSERT INTO Categories (CategoryName, Description)
            VALUES (?, ?)
        """, (category_name, description))
    conn.commit()

# Insert data into Brands table
def insert_brands(n):
    for _ in range(n):
        brand_name = fake.company()
        description = fake.text()
        
        cursor.execute("""
            INSERT INTO Brands (BrandName, Description)
            VALUES (?, ?)
        """, (brand_name, description))
    conn.commit()

# Insert data into Customer Reviews table
def insert_reviews(n):
    for _ in range(n):
        customer_id = randint(1, 100)
        product_id = randint(1, 50)
        rating = randint(1, 5)
        review_text = fake.text()
        review_date = random_date(datetime(2020, 1, 1), datetime.now())
        
        cursor.execute("""
            INSERT INTO CustomerReviews (CustomerID, ProductID, Rating, ReviewText, ReviewDate)
            VALUES (?, ?, ?, ?, ?)
        """, (customer_id, product_id, rating, review_text, review_date))
    conn.commit()

# Insert data into Wishlists table
def insert_wishlists(n):
    for _ in range(n):
        customer_id = randint(1, 100)
        product_id = randint(1, 50)
        added_date = random_date(datetime(2020, 1, 1), datetime.now())
        
        cursor.execute("""
            INSERT INTO Wishlists (CustomerID, ProductID, AddedDate)
            VALUES (?, ?, ?)
        """, (customer_id, product_id, added_date))
    conn.commit()

# Insert data into Shopping Cart table
def insert_shopping_cart(n):
    for _ in range(n):
        customer_id = randint(1, 100)
        product_id = randint(1, 50)
        quantity = randint(1, 10)
        date_added = random_date(datetime(2020, 1, 1), datetime.now())
        
        cursor.execute("""
            INSERT INTO ShoppingCart (CustomerID, ProductID, Quantity, DateAdded)
            VALUES (?, ?, ?, ?)
        """, (customer_id, product_id, quantity, date_added))
    conn.commit()

# Insert data into Payments table
def insert_payments(n):
    for _ in range(n):
        order_id = randint(1, 100)
        payment_method = choice(['Credit Card', 'PayPal', 'Bank Transfer'])
        payment_date = random_date(datetime(2020, 1, 1), datetime.now())
        amount = round(fake.random_number(digits=5), 2)
        
        cursor.execute("""
            INSERT INTO Payments (OrderID, PaymentMethod, PaymentDate, Amount)
            VALUES (?, ?, ?, ?)
        """, (order_id, payment_method, payment_date, amount))
    conn.commit()

# Insert data into Customer Support Tickets table
def insert_support_tickets(n):
    for _ in range(n):
        customer_id = randint(1, 100)
        order_id = randint(1, 100)
        issue_type = choice(['Product Issue', 'Payment Issue', 'Shipping Issue', 'Other'])
        description = fake.text()
        status = choice(['Open', 'In Progress', 'Resolved', 'Closed'])
        created_date = random_date(datetime(2020, 1, 1), datetime.now())
        resolved_date = random_date(created_date, datetime.now())
        
        cursor.execute("""
            INSERT INTO CustomerSupportTickets (CustomerID, OrderID, IssueType, Description, Status, CreatedDate, ResolvedDate)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (customer_id, order_id, issue_type, description, status, created_date, resolved_date))
    conn.commit()


insert_customers(50)        
insert_orders(50)           
insert_order_items(50)      
insert_products(50)         
insert_categories(10)       
insert_brands(5)           
insert_reviews(50)          
insert_wishlists(50)        
insert_shopping_cart(50)    
insert_payments(50)         
insert_support_tickets(50)  


cursor.close()
conn.close()
