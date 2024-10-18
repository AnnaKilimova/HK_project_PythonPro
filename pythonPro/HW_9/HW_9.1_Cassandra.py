# Варіант 3: Cassandra (колонкова база даних)

from cassandra.cluster import Cluster # To connect to the Cassandra cluster.
import uuid # To generate unique UUID identifiers.
from datetime import datetime, timedelta # To work with date and time.

# Connecting to the Cassandra cluster.
cluster = Cluster(['127.0.0.1']) # Connection to Cassandra on the local host (IP address 127.0.0.1).
session = cluster.connect() # Creating a session to execute requests to Cassandra.

# Creating a key space.
session.execute("""
    CREATE KEYSPACE IF NOT EXISTS event_logs_space
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'}
""")
# KEYSPACE: keyspace is the analogue of a database in Cassandra.
# event_logs_space: the name of the keyspace that is created when a query is made.
# SimpleStrategy: defines the data replication strategy.
# replication_factor = 3: means that each record will be replicated on three nodes.

# Use of key space.
session.set_keyspace('event_logs_space') # Sets the key space as active for subsequent operations.

# 1. Зберігання логів подій:
# Створіть таблицю для зберігання логів подій у Cassandra. Логи можуть містити поля:
# event_id, user_id, event_type, timestamp, metadata.

# Table creation. The query creates the event_logs table if it does not already exist.
session.execute("""
    CREATE TABLE IF NOT EXISTS event_logs (
        event_id UUID PRIMARY KEY,
        user_id UUID,
        event_type TEXT,
        timestamp TIMESTAMP,
        metadata MAP<TEXT, TEXT>
    )
""")
# The table contains the following columns:
# event_id: unique event identifier.
# user_id: unique user identifier.
# event_type: event type (e.g. ‘login’, ‘logout’).
# timestamp: the time at which the event occurred.
# metadata: additional information about the event in the form of a map (dictionary) that contains key-value pairs.

# 2. CRUD операції:
# Create: Додайте новий лог події до таблиці.
# Read: Отримайте всі події певного типу за останні 24 години.
# Update: Оновіть додаткову інформацію в полі metadata для певного event_id.
# Delete: Видаліть старі події (старші за 7 днів) з бази даних.

# ***Create***

# Request to add a new log.
# An SQL query is created to insert data into the event_logs table.
insert_query = """
    INSERT INTO event_logs (event_id, user_id, event_type, timestamp, metadata)
    VALUES (%s, %s, %s, %s, %s)
"""
# %s: placeholders are used for subsequent substitution of values.

# Adding a new event log.
session.execute(insert_query, (
    uuid.uuid4(), # Generates unique UUIDs for the event and user.
    uuid.uuid4(),
    'login',
    datetime.now(), # Current time when the event occurred.
    {'ip': '192.168.0.1', 'browser': 'Chrome'} # Dictionary with event metadata (IP address and browser).
))

# ***Read***

# Receive events for the last 24 hours.
current_time = datetime.now() # Сurrent time.
past_24_hours = current_time - timedelta(days=1) # Calculates the time 24 hours ago.

# Query to sample all events of type ‘login’ that occurred in the last 24 hours.
select_query = """
    SELECT * FROM event_logs
    WHERE event_type = %s AND timestamp > %s ALLOW FILTERING
"""
# ALLOW FILTERING: allows filtering of data in Cassandra by fields that are not part of the key.

# Executes the query by substituting the event type and time 24 hours ago.
rows = session.execute(select_query, ('login', past_24_hours))

# Results output
for row in rows:
    print(row)

# ***Update***

# Metadata update requestю
update_query = """
    UPDATE event_logs
    SET metadata['ip'] = %s
    WHERE event_id = %s
"""

# Updating metadataю
event_id_to_update = uuid.uuid4()  # Unique UUID
new_ip_address = '203.0.113.10'

# Update request.
session.execute(update_query, (new_ip_address, event_id_to_update))

# ***Delete***

# Delete old events.
past_7_days = current_time - timedelta(days=7)

# First, select the events to be deleted.
select_query = """
    SELECT event_id FROM event_logs
    WHERE timestamp < %s ALLOW FILTERING
"""

# Get all events that are older than 7 days
rows_to_delete = session.execute(select_query, (past_7_days,))

# Now delete each line by its event_id
delete_query = """
    DELETE FROM event_logs WHERE event_id = %s
"""

# Go through each line and delete by event_id
for row in rows_to_delete:
    session.execute(delete_query, (row.event_id,))

# 3. Реплікація та масштабування:
# Поясніть, як Cassandra забезпечує реплікацію даних та горизонтальне масштабування.

# Cassandra забезпечує високу доступність за допомогою реплікації. Дані розподіляються по різних вузлах (нодах)
# кластера, що дозволяє автоматично зберігати кілька копій даних.
# Кількість реплік визначає, скільки копій даних буде збережено в кластері.
# В кодi ми вже використовували SimpleStrategy і встановили кількість реплік у 3. Це означає, що кожен запис буде
# копіюватися на 3 різні вузли в кластері.
# Cassandra підтримує горизонтальне масштабування, що дозволяє додавати нові вузли в кластер без зупинки системи:
# Дані автоматично перерозподіляються між новими і старими вузлами.
# Вузли працюють незалежно, що забезпечує високу стійкість до відмов і доступність.