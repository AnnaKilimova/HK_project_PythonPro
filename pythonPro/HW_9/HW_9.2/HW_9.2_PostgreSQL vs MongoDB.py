# Частина 2: Порівняння SQL і NoSQL
# Виконайте порівняння між реляційною базою даних (наприклад, PostgreSQL) та NoSQL (наприклад, MongoDB):
# Виконайте аналогічні CRUD операції для однієї й тієї ж моделі даних.
# Проаналізуйте переваги та недоліки кожної системи для різних завдань.

# MongoDB

from pymongo import MongoClient # The MongoClient allows сonnection to and perform operations on the MongoDB.
from datetime import datetime # To work with date and time.

# Create an object to connect to the MongoDB server, which is located at localhost on port 27017
# (the standard port for MongoDB). Now the client object can be used to interact with the database.
client = MongoClient("mongodb://localhost:27017/")

# Create a database.
db = client["online_store"]

# Create a collection of products inside the online_store database.
products_collection = db["products"]

# Create a collection of orders inside the online_store database.
orders_collection = db["orders"]

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

# Переваги:
# Гнучкість у структурі даних:
#
# MongoDB є NoSQL базою даних і зберігає дані в форматі JSON-подібних документів. Це дозволяє зберігати дані з динамічними та різними структурами без необхідності суворої схеми.
# Поля можна легко додавати або змінювати в документах, без потреби змінювати всю базу, що дуже зручно для швидкого розвитку системи.
# Швидкість і масштабованість:
#
# MongoDB забезпечує високу продуктивність для запису даних, оскільки вона віддає перевагу гнучкості над ACID-гарантіями.
# Вона добре підходить для горизонтальної масштабованості (розширення кластера шляхом додавання серверів).
# Природна підтримка вкладених структур:
#
# Легко працювати з вкладеними документами та масивами, наприклад, при зберіганні переліку товарів у замовленні, що дозволяє уникнути складних JOIN-операцій.
# Простота для CRUD операцій:
#
# Записи, оновлення та видалення даних прості та ефективні в MongoDB, оскільки її модель документів дозволяє маніпулювати даними за допомогою зрозумілих команд.

# Недоліки:
# Відсутність транзакцій на рівні багатьох документів:
#
# Хоча MongoDB підтримує транзакції, вони були додані пізніше і можуть не працювати так само ефективно, як у реляційних базах даних (наприклад, PostgreSQL). Це може бути важливим для систем, де гарантії ACID є критичними.
# Відсутність відносин між даними:
#
# MongoDB не забезпечує чітких відносин між документами, як це роблять реляційні бази даних. Це може призводити до дублювання даних і складності при необхідності роботи з відносинами між об'єктами (наприклад, зв'язки між замовленнями та продуктами).
# Потреба в обробці великих обсягів даних:
#
# Для великих обсягів даних MongoDB може бути не такою ефективною, як реляційні бази даних, особливо якщо потрібно виконувати складні аналітичні запити.



# PostgreSQL

import psycopg2
from psycopg2 import sql
import datetime

# Parameters for connecting to PostgreSQL
connection_info = {
    'dbname': 'postgres_db',  # database
    'user': 'ann_kilimova',  # username
    'password': 'A2l3i0S8A41_aNnAndriI',  # password
    'host': 'localhost',  # host
    'port': '5432' # port
}

# Connecting to PostgreSQL
try:
    conn = psycopg2.connect(**connection_info)
    conn.autocommit = True  # enable auto-commit to create a database
    cur = conn.cursor()

    # Creating a new database
    db_name = 'online_store'
    cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
    print(f"Database {db_name} was created successfully.")

    # Close the connection to the database to create a new one
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error during database creation: {e}")

# Now let's connect to the newly created database and create the following tables
connection_info['dbname'] = 'online_store'  # new database

try:
    conn = psycopg2.connect(**connection_info)
    cur = conn.cursor()

    # Create a product table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            price NUMERIC(10, 2) NOT NULL,
            category VARCHAR(50),
            stock_quantity INT NOT NULL
        );
    ''')

# ***Create***

    # Adding products to the products table
    def add_product(name, price, category, stock_quantity):
        try:
            conn = psycopg2.connect(**connection_info)
            cur = conn.cursor()
            cur.execute(
                '''
                INSERT INTO products (name, price, category, stock_quantity)
                VALUES (%s, %s, %s, %s);
                ''', (name, price, category, stock_quantity)
            )
            conn.commit()
            print(f"Product ‘{name}’ has been added successfully.")
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Error while adding a product: {e}")


    # Adding an order to the orders table.
    def add_order(client_name, product_list, total_amount):
        try:
            conn = psycopg2.connect(**connection_info)
            cur = conn.cursor()
            cur.execute(
                '''
                INSERT INTO orders (client_name, product_list, total_amount)
                VALUES (%s, %s, %s);
                ''', (client_name, product_list, total_amount)
            )
            conn.commit()
            print(f"The order for customer ‘{client_name}’ was added successfully.")
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Error while adding an order: {e}")


    # Adding products
    add_product("Laptop", 1000, "Electronics", 50)
    add_product("Phone", 500, "Electronics", 100)
    add_product("Shoes", 80, "Fashion", 200)

    # Adding an order
    add_order("John Doe", "Laptop: 1, Phone: 2", 2000)

    # Create an orders table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            order_id SERIAL PRIMARY KEY,
            client_name VARCHAR(100) NOT NULL,
            product_list TEXT NOT NULL,  -- a list of products as text or або JSON
            total_amount NUMERIC(10, 2) NOT NULL,
            order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    ''')

    conn.commit()  # save changes
    print("The ‘products’ and ‘orders’ tables have been created successfully.")

    # Close the connection
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error while creating tables: {e}")

# ***Read***
def get_recent_orders():
    try:
        conn = psycopg2.connect(**connection_info)
        cur = conn.cursor()

        # Date 30 days ago
        thirty_days_ago = datetime.datetime.now() - datetime.timedelta(days=30)

        cur.execute(
            '''
            SELECT * FROM orders WHERE order_date >= %s;
            ''', (thirty_days_ago,)
        )
        orders = cur.fetchall()

        if orders:
            for order in orders:
                print(order)
        else:
            print("No orders for the last 30 days.")

        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error when receiving orders: {e}")

# Orders received in the last 30 days.
get_recent_orders()

# ***Update***
def update_stock_quantity(product_id, quantity_purchased):
    try:
        conn = psycopg2.connect(**connection_info)
        cur = conn.cursor()

        cur.execute(
            '''
            UPDATE products
            SET stock_quantity = stock_quantity - %s
            WHERE product_id = %s AND stock_quantity >= %s;
            ''', (quantity_purchased, product_id, quantity_purchased)
        )
        conn.commit()
        print(f"Updated product quantity with ID {product_id}.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error when updating product quantity: {e}")

# Update product quantity after purchasing 2 units of product with ID 1
update_stock_quantity(1, 2)

# ***Delete***
def delete_out_of_stock_products():
    try:
        conn = psycopg2.connect(**connection_info)
        cur = conn.cursor()

        cur.execute(
            '''
            DELETE FROM products
            WHERE stock_quantity = 0;
            '''
        )
        conn.commit()
        print("Products that are out of stock have been successfully removed.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error while deleting products: {e}")

# Delete products that are no longer in stock
delete_out_of_stock_products()

# Переваги:
# Підтримка ACID:
#
# PostgreSQL є реляційною базою даних з повною підтримкою ACID (Atomicity, Consistency, Isolation, Durability). Це робить її підходящою для систем, де важлива надійність транзакцій, наприклад, у фінансових додатках.
# Потужні можливості для складних запитів:
#
# PostgreSQL підтримує складні SQL-запити, включаючи JOIN, підзапити, індекси та агрегації, що робить її ідеальною для систем з високими вимогами до аналітичних запитів і складних реляційних даних.
# Типізація даних:
#
# PostgreSQL забезпечує сувору типізацію даних, що гарантує валідність і цілісність введених даних, що важливо для критично важливих додатків.
# Розширюваність:
#
# PostgreSQL підтримує розширення, такі як JSONB, що дозволяє зберігати та обробляти документи JSON, надаючи певну гнучкість для неструктурованих даних.
# Масштабованість та розширені функції:
#
# PostgreSQL добре масштабується на потужних серверах і підтримує розширені функції, як-то індекси для тексту або географічні дані.

# Недоліки:
# Складність роботи з неструктурованими даними:
#
# Хоча PostgreSQL підтримує JSONB, робота з неструктурованими даними все ще складніша, ніж у MongoDB, особливо якщо структури даних часто змінюються або є непередбачуваними.
# Швидкість запису:
#
# Через забезпечення ACID-гарантій PostgreSQL може бути повільнішою для масових операцій запису, особливо в сценаріях, де гнучкість даних важливіша за цілісність.
# Складність горизонтальної масштабованості:
#
# PostgreSQL краще масштабується вертикально (додаванням ресурсів до одного сервера), тоді як горизонтальна масштабованість (додавання нових серверів) може бути складнішою в налаштуванні, на відміну від MongoDB.
# Ускладнені CRUD операції:
#
# Операції створення, читання, оновлення та видалення можуть бути складнішими через потребу в суворих схемах і типах даних, а також через необхідність писати більш детальні SQL-запити.