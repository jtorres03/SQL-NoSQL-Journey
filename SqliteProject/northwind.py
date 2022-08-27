import sqlite3


expensive_items_query = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
"""

avg_hire_age_query = """
SELECT AVG(HireDate - BirthDate)
FROM Employee
"""

ten_most_expensive_query = """
SELECT Product.ProductName, OrderDetail.UnitPrice, Supplier.CompanyName
FROM Supplier
JOIN Product
on Supplier.Id = Product.SupplierId
JOIN OrderDetail
on OrderDetail.ProductId = Product.Id
GROUP by Product.ProductName
ORDER by OrderDetail.UnitPrice DESC
LIMIT 10
"""

largest_category_query = """
SELECT Category.CategoryName, count(DISTINCT Product.ProductName)
as numberUniqueProducts
FROM Product
JOIN Category
on Product.CategoryId = Category.Id
GROUP by Category.CategoryName
Order by numberUniqueProducts DESC
LIMIT 1
"""


def connect_to_db(db_name='northwind_small.sqlite3'):
    """Connect to a database"""
    return sqlite3.connect(db_name)


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def execute_ddl(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)


expensive_items = execute_query(connect_to_db(), expensive_items_query)
avg_hire_age = execute_query(connect_to_db(), avg_hire_age_query)
ten_most_expensive = execute_query(connect_to_db(), ten_most_expensive_query)
largest_category = execute_query(connect_to_db(), largest_category_query)

if __name__ == '__main__':
    conn = connect_to_db
    # print(expensive_items)
    # print(avg_hire_age)
    # print(ten_most_expensive)
    # print(largest_category)
