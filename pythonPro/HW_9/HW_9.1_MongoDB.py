# Варіант 1: MongoDB (документо-орієнтована база даних)

from pymongo import MongoClient # The MongoClient allows сonnection to and perform operations on the MongoDB.
from datetime import datetime # To work with date and time.

# 1. Створення бази даних та колекцій:
# • Створіть базу даних для зберігання інформації про онлайн-магазин.
# • Створіть колекцію products, яка містить дані про продукти (назва, ціна, категорія, кількість на складі).
# • Створіть колекцію orders, яка містить інформацію про замовлення
#   (номер замовлення, клієнт, список продуктів із кількістю, загальна сума).

# Create an object to connect to the MongoDB server, which is located at localhost on port 27017
# (the standard port for MongoDB). Now the client object can be used to interact with the database.
client = MongoClient("mongodb://localhost:27017/")

# Create a database.
db = client["online_store"]

# Create a collection of products inside the online_store database.
products_collection = db["products"]

# Create a collection of orders inside the online_store database.
orders_collection = db["orders"]

# 2. CRUD операції:
# • Create: Додайте кілька продуктів і замовлень у відповідні колекції.
# • Read: Витягніть всі замовлення за останні 30 днів.
# • Update: Оновіть кількість продукту на складі після його купівлі.
# • Delete: Видаліть продукти, які більше не доступні для продажу.

# ***Create***

# Adding multiple products
products_collection.insert_many([
    {"name": "Laptop", "price": 1000, "category": "Electronics", "stock": 50},
    {"name": "Phone", "price": 500, "category": "Electronics", "stock": 100},
    {"name": "Shoes", "price": 80, "category": "Fashion", "stock": 200}
])

# Adding multiple orders
orders_collection.insert_many([
    {"order_id": 1, "client": "John Doe", "products": [{"name": "Laptop", "quantity": 1}], "total": 1000, "date": datetime(2024, 10, 1)},
    {"order_id": 2, "client": "Jane Smith", "products": [{"name": "Phone", "quantity": 2}], "total": 1000, "date": datetime(2024, 10, 5)}
])

# ***Read***

from datetime import timedelta # To work with the difference between dates.

# Extract of orders for the last 30 days
last_30_days = datetime.now() - timedelta(days=30)
recent_orders = orders_collection.find({"date": {"$gte": last_30_days}}) # $gte (> || ==): filter by date.

# Go through all found orders and display each found order on the screen.
for order in recent_orders:
    print(order)

# ***Update***

# Update the quantity of a product in stock after purchase (for example, ‘Laptop’ after ordering)
products_collection.update_one(
    {"name": "Laptop"},
    {"$inc": {"stock": -1}}  # Reduction in stock by 1
)

# ***Delete***

# Delete products with zero or negative values in the warehouse.
products_collection.delete_many({"stock": {"$lte": 0}}) # $lte (< || ==): find such products.

# 3. Агрегація даних:
# • Порахуйте загальну кількість проданих продуктів за певний період часу.
# • Використовуйте функцію агрегації для підрахунку загальної суми всіх замовлень клієнта.

# Calculating the total number of products sold for a certain period
start_date = datetime(2024, 10, 1)
end_date = datetime(2024, 10, 31)

# Define the pipeline for the aggregate query that will be executed in MongoDB.
# This is a sequence of stages that will allow to calculate the number of sold products for the specified period.
pipeline = [
    # 1 stage: filtering orders by date. Find orders made between start_date and end_date (inclusive).
    {"$match": {"date": {"$gte": start_date, "$lte": end_date}}}, # $gte and $lte are used to filter by date range.
    # 2 Stage: Convert each element of the products array into a separate document for individual work with them.
    {"$unwind": "$products"},
    # Third stage: group the results and calculate the total number of products sold using the $sum operator.
    # The products.quantity field contains the quantity of each product in the order.
    {"$group": {"_id": None, "total_sold": {"$sum": "$products.quantity"}}}
]

# Execute the aggregate query and save the result to the total_sold list.
total_sold = list(orders_collection.aggregate(pipeline))
print(f"Total number of products sold: {total_sold[0]['total_sold']}")

# Set the name of the client for which we will calculate the total amount of orders.
client_name = "John Doe"

# Define a new pipeline for the aggregate query that will calculate the sum of customer orders.
pipeline = [
    # Stage one: find all orders placed by a customer with the name John Doe.
    {"$match": {"client": client_name}},
    # Stage two: group orders by customer name and calculate the total amount of orders using the $sum operator,
    # using the total field, which stores the total value of the order.
    {"$group": {"_id": "$client", "total_spent": {"$sum": "$total"}}}
]

total_spent = list(orders_collection.aggregate(pipeline)) # Execute the aggregate query and save the result to a list
print(f"Total amount of customer orders {client_name}: {total_spent[0]['total_spent']}")

# 4. Індекси:
# Додайте індекси для поля category в колекції products, щоб прискорити пошук продуктів по категоріях.

# Add an index to the category field in the products collection. Indexes help to speed up the search on this field.
products_collection.create_index("category")


# Search for products in the category ‘Electronics’
electronics_products = products_collection.find({"category": "Electronics"})

for product in electronics_products:
    print(product)
