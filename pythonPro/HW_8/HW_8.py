"""Розробіть консольний застосунок для керування базою даних "Кінобаза", що містить інформацію про
 фільми та акторів, які в них знімалися. Ваша база даних повинна мати наступні таблиці:"""

import sqlite3  # Imports the sqlite3 module, which provides an API for working with SQLite databases in Python.


def create_tables():
    """To create the necessary tables for the database."""
    conn = sqlite3.connect("movie_db.sqlite")  # Creates a new database.
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # 1. Таблиця movies
    # id — унікальний ідентифікатор фільму (INTEGER, PRIMARY KEY).
    # title — назва фільму (TEXT).
    # release_year — рік випуску (INTEGER).
    # genre — жанр (TEXT).

    # An SQL query is executed to create the 'movies' table.
    # id, title, release_year, genre - сolumns names.
    # INTEGER, TEXT - data types.
    # PRIMARY KEY - the id field is the unique identifier of each row in the table.
    # AUTOINCREMENT - for this column, a unique value for each new record will be automatically generated.
    # and incremented by one for each new row.
    # NOT NULL - forbids storing empty values in this column.
    cursor.execute("""CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        release_year INTEGER NOT NULL,
        genre TEXT NOT NULL
    )""")

    # 2. Таблиця actors
    # d — унікальний ідентифікатор актора (INTEGER, PRIMARY KEY).
    # name — ім'я актора (TEXT).
    # birth_year — рік народження (INTEGER).

    # An SQL query is executed to create the 'actors' table.
    # id, name, birth_year - сolumns names.
    # INTEGER, TEXT - data types.
    # PRIMARY KEY - the id field is the unique identifier of each row in the table.
    # AUTOINCREMENT - for this column, a unique value for each new record will be automatically generated.
    # and incremented by one for each new row.
    # NOT NULL - forbids storing empty values in this column.
    cursor.execute("""CREATE TABLE IF NOT EXISTS actors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        birth_year INTEGER NOT NULL
    )""")

    # 3. Таблиця movie_cast
    # movie_id — ідентифікатор фільму (INTEGER, FOREIGN KEY).
    # actor_id — ідентифікатор актора (INTEGER, FOREIGN KEY).
    # PRIMARY KEY(movie_id, actor_id).

    # An SQL query is executed to create the 'movie_cast' table.
    # movie_id, actor_id - сolumns names.
    # INTEGER, TEXT - data types.
    # PRIMARY KEY - a composite primary key is defined here, which consists of two columns.
    # This avoids duplicate entries (i.e. the same actor cannot be linked to the same film twice).

    # 8. Запит з використанням FOREIGN KEY:
    # Зв'яжіть таблиці movies та actors через таблицю movie_cast за допомогою зовнішніх ключів.

    # FOREIGN KEY - indicates that the values of this column should be taken from another table.
    # REFERENCES - specifies that the foreign key references the column in the another table.
    cursor.execute("""CREATE TABLE IF NOT EXISTS movie_cast (
        movie_id INTEGER,
        actor_id INTEGER,
        PRIMARY KEY(movie_id, actor_id),
        FOREIGN KEY(movie_id) REFERENCES movies(id),
        FOREIGN KEY(actor_id) REFERENCES actors(id)
    )""")

    conn.commit()  # All changes made to the database are confirmed.
    conn.close()  # The connection to the database is closed.


create_tables()  # The create_tables function is called to create tables.


# ***Функціонал застосунку***

# 1. Додавання записів
# Реалізуйте можливість додавання нових фільмів і акторів.
# При додаванні фільму, користувач повинен мати можливість вказати, які актори знімалися у цьому фільмі
# (використовуйте таблицю movie_cast для цього).

def add_movie(title, release_year, genre, actor_ids):
    """Adding new films and actors."""
    conn = sqlite3.connect("movie_db.sqlite")  # Opens a connection to the database.
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # An SQL query is executed to add a new film to the 'movies' table.
    cursor.execute("INSERT INTO movies (title, release_year, genre) VALUES (?, ?, ?)", (title, release_year, genre))
    movie_id = (cursor.lastrowid)  # Get the ID of the last inserted string (the ID of the new movie).

    # For each actor ID from the actor_ids list, an SQL query is executed to add a record to the 'movie_cast' table
    for actor_id in actor_ids:
        cursor.execute("INSERT INTO movie_cast (movie_id, actor_id) VALUES (?, ?)", (movie_id, actor_id))

    conn.commit()  # All changes made to the database are confirmed.
    conn.close()  # The connection to the database is closed.


def add_actor(name, birth_year):
    """Adding a new actor to the database."""
    conn = sqlite3.connect("movie_db.sqlite")  # Opens a connection to the database.
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # An SQL query is executed to add a new actor to the 'actors' table.
    cursor.execute("INSERT INTO actors (name, birth_year) VALUES (?, ?)", (name, birth_year))

    conn.commit()  # All changes made to the database are confirmed.
    conn.close()  # The connection to the database is closed.


# 2. Запит з використанням JOIN
# Реалізуйте запит, який виводить список фільмів разом із іменами всіх акторів, які знімалися у кожному з фільмів.
# Використайте INNER JOIN для з'єднання таблиць movies, movie_cast і actors.
def show_movies_with_actors():
    """Displays a list of films with their actors."""
    conn = sqlite3.connect("movie_db.sqlite")  # Opens a connection to the database.
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # SELECT: specifies which columns should be selected to display the result.
    # GROUP_CONCAT: combines the actor names for each film, which are stored in the name field from the actors table.
    # AS: column alias.
    # FROM: specifies the main table from which to start the query.
    # JOIN ON: joins two tables, the movie/actors id in the movies table matches the movie_id/actor_idd  field in the movie_cast table.
    # GROUP BY: groups rows by the movies.title field. This means that for each unique movie title, all actors will be
    # grouped together. Without it, the query would return multiple rows for the same movie - one row for each actor.
    cursor.execute("""SELECT movies.title, GROUP_CONCAT(actors.name, ', ') AS actors
                      FROM movies
                      JOIN movie_cast ON movies.id = movie_cast.movie_id
                      JOIN actors ON actors.id = movie_cast.actor_id
                      GROUP BY movies.title""")
    movies = cursor.fetchall()

    # For each movie, its title and cast list are displayed.
    for movie in movies:
        print(f"Фільм: {movie[0]}, Актори: {movie[1]}")

    conn.close()  # Database connection is closed


# 3. Запит з використанням DISTINCT
# Додайте можливість вивести унікальний список жанрів фільмів (без повторень), використовуючи DISTINCT.


def show_unique_genres():
    """Display a list of unique genres"""
    conn = sqlite3.connect("movie_db.sqlite")  # Opens a connection to the database.
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # To obtain unique strings without duplicates.
    cursor.execute("SELECT DISTINCT genre FROM movies")
    # The method fetches all rows of a query result set and returns a list of tuples.
    # If no more rows are available, it returns an empty list.
    genres = cursor.fetchall()

    # Each genre is displayed.
    for genre in genres:
        print(genre[0])

    conn.close()  # Database connection is closed


# 4. Запит з використанням агрегатних функцій:
# Реалізуйте функцію для підрахунку кількості фільмів, знятих в кожному жанрі (використовуйте COUNT).
# Реалізуйте функцію, яка знаходить середній рік народження акторів, що знімалися у фільмах певного жанру
# (використовуйте AVG).


def count_movies_by_genre():
    """For counting the number of films in each genre."""
    conn = sqlite3.connect("movie_db.sqlite")  # Opens a connection to the database.
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # SELECT: specifies which columns should be selected.
    # COUNT(*): counts the number of films made in each genre
    # FROM: specifies the main table from which to start the query.
    # GROUP BY: groups rows by the genre field.
    cursor.execute("SELECT genre, COUNT(*) FROM movies GROUP BY genre")
    # The method fetches all rows of a query result set and returns a list of tuples.
    # If no more rows are available, it returns an empty list.
    genres = cursor.fetchall()

    for genre in genres:
        print(f"{genre[0]}: {genre[1]} фільмів")

    conn.close()  # Database connection is closed


def avg_birth_year_by_genre(genre):
    """For calculating the average year of birth of actors for films of a certain genre."""
    conn = sqlite3.connect("movie_db.sqlite")  # Opens a connection to the database.
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # SELECT: specifies which columns should be selected.
    # AVG: finds the average year of birth of actors who starred in films of a certain genre.
    # FROM: specifies the main table from which to start the query.
    # JOIN ON: joins two tables.
    # WHERE: selection of values with a specific parameter.
    cursor.execute("""SELECT AVG(actors.birth_year) FROM actors
                      JOIN movie_cast ON actors.id = movie_cast.actor_id
                      JOIN movies ON movies.id = movie_cast.movie_id
                      WHERE movies.genre = ?""", (genre,))
    # Retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available.
    avg_year = cursor.fetchone()[0]

    if avg_year:
        print(f"Середній рік народження акторів у фільмах жанру {genre}: {int(avg_year)}")
    else:
        print(f"Немає фільмів у жанрі {genre}.")

    conn.close()  # Database connection is closed


# 5. Запит з використанням LIKE:
# Додайте можливість пошуку фільмів за ключовим словом у назві.
# Використовуйте оператор LIKE для пошуку часткових збігів у назві фільму.


def search_movie_by_title(keyword):
    """Search for films by partial title matching."""
    conn = sqlite3.connect("movie_db.sqlite")  # Opens a connection to the database.
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # SELECT: specifies which columns should be selected.
    # FROM: specifies the main table from which to start the query.
    # WHERE: selection of values with a specific parameter.
    # LIKE: for pattern matching
    cursor.execute("SELECT * FROM movies WHERE title LIKE ?", ("%" + keyword + "%"))
    movies = (cursor.fetchall())  # The method fetches all rows of a query result set and returns a list of tuples.

    for movie in movies:
        print(f"Фільм: {movie[1]}, Рік випуску: {movie[2]}, Жанр: {movie[3]}")

    conn.close()  # Database connection is closed


# 6. Запит з використанням LIMIT та OFFSET:
# Реалізуйте можливість перегляду фільмів з пагінацією.
# Використайте LIMIT і OFFSET для обмеження кількості виведених результатів.


def show_movies_with_pagination(page, page_size):
    """For watching movies with pagination."""
    conn = sqlite3.connect("movie_db.sqlite")  # Opens a connection to the database.
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # The offset for the query is calculated.
    # page - 1: if the request is for a second page, for example,
    # we start at a position equal to the size of the first page.
    # * page_size: multiplication by the page size (number of records on one page)
    # determines which record to start sampling from.
    # Example: if the page size is 5 and a third page is requested,
    # the offset will be (3 - 1) * 5 = 10. This means that the query will start from the 11th record.
    offset = (page - 1) * page_size
    # LIMIT: limits the number of rows (movies) returned to the page_size value.
    # For example, if page_size = 5, the query will return only 5 records.
    # OFFSET: determines the offset from which row to start sampling data (value from the offset variable).
    # A query using LIMIT and OFFSET allows only a certain number of films to be displayed per page.
    cursor.execute("SELECT * FROM movies LIMIT ? OFFSET ?", (page_size, offset))
    # Retrieves all the rows (movies) returned by the query and store them in the movies variable.
    movies = (cursor.fetchall())  # This is a list of tuples, where each tuple represents one row from the table.

    for movie in movies:
        print(f"Фільм: {movie[1]}, Рік випуску: {movie[2]}, Жанр: {movie[3]}")

    conn.close()  # Database connection is closed


# 7. Запит з використанням UNION:
# Реалізуйте запит, який виводить імена всіх акторів та назви всіх фільмів в одному результаті (використовуючи UNION).
def show_actors_and_movies():
    """Outputs the names of all actors and the titles of all films, combining them in a single query."""
    conn = sqlite3.connect("movie_db.sqlite")  # Opens a connection to the database.
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # An SQL query is executed that combines the results of two selections:
    # SELECT name FROM actors: select the names of all actors from the actors table.
    # UNION: combines the results of two samples into a single data set. It automatically removes duplicates.
    # SELECT title FROM movies: select the titles of all movies from the movies table.
    # The result is a list of all actor names and film titles in one column.
    cursor.execute("""SELECT name FROM actors
                      UNION
                      SELECT title FROM movies""")
    results = cursor.fetchall()

    for result in results:
        print(result[0])

    conn.close()  # Database connection is closed


# 9. Запит з використанням власної функції:
# Реалізуйте пункт меню для виведення списку фільмів разом з їх віком, використовуючи створену функцію movie_age().


def movie_age(year):
    """Calculates the age of a film based on its year of release."""
    from datetime import (datetime)  # Import the datetime module to work with the current date and time.

    current_year = datetime.now().year  # Get the current year.
    return current_year - year  # Calculate the age of the film.


def show_movies_with_age():
    conn = sqlite3.connect("movie_db.sqlite")  # # Opens a connection to the database.
    # Register a custom function movie_age in the SQLite database.
    # It takes one argument (year of film release) and calculates the age of the film.
    conn.create_function("movie_age", 1, movie_age)
    cursor = conn.cursor()  # Object is used to execute SQL queries.

    # An SQL query is executed that selects the title of the film, its year of release, and the calculated age.
    cursor.execute("SELECT title, release_year, movie_age(release_year) AS age FROM movies")
    movies = (cursor.fetchall())  # Retrieve all query results and save them to a variable.

    for movie in movies:
        print(f"Фільм: {movie[0]}, Рік випуску: {movie[1]}, Вік: {movie[2]} років")

    conn.close()  # Database connection is closed


# Interaction with the programme
def main():
    create_tables()
    while True:
        print("\n1. Додати фільм")
        print("2. Додати актора")
        print("3. Показати всі фільми з акторами")
        print("4. Показати унікальні жанри")
        print("5. Показати кількість фільмів за жанром")
        print("6. Показати середній рік народження акторів у фільмах певного жанру")
        print("7. Пошук фільму за назвою")
        print("8. Показати фільми (з пагінацією)")
        print("9. Показати імена всіх акторів та назви всіх фільмів")
        print("0. Вихід")

        choice = input("Виберіть дію: ")

        if choice == "1":
            title = input("Введіть назву фільму: ")
            release_year = int(input("Введіть рік випуску: "))
            genre = input("Введіть жанр: ")
            actor_ids = list(map(int, input("Введіть ID акторів через кому: ").split(",")))
            add_movie(title, release_year, genre, actor_ids)

        elif choice == "2":
            name = input("Введіть ім'я актора: ")
            birth_year = int(input("Введіть рік народження актора: "))
            add_actor(name, birth_year)

        elif choice == "3":
            show_movies_with_actors()

        elif choice == "4":
            show_unique_genres()

        elif choice == "5":
            count_movies_by_genre()

        elif choice == "6":
            genre = input("Введіть жанр: ")
            avg_birth_year_by_genre(genre)

        elif choice == "7":
            keyword = input("Введіть ключове слово для пошуку: ")
            search_movie_by_title(keyword)

        elif choice == "8":
            page = int(input("Введіть номер сторінки: "))
            page_size = int(input("Введіть кількість фільмів на сторінку: "))
            show_movies_with_pagination(page, page_size)

        elif choice == "9":
            show_actors_and_movies()

        elif choice == "0":
            print("Вихід з програми.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
