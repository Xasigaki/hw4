import sqlite3
from pathlib import Path


def init_db():
    global db, cur
    DB_NAME = 'db.sqlite3'
    MAIN_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(MAIN_PATH/DB_NAME)
    cur = db.cursor()


def create_table():
    cur.execute(
        """CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY,
        namme TEXT,
        description TEXT,
        price INTEGER,
        phone TEXT
         )"""
        )
    cur.execute(
        """CREATE TABLE IF NOT EXISTS order(
         order_id INTEGER PRIMARY KEY,
         user_name TEXT,
         address TEXT,
         weeks TEXT,
         product_id INTEGER,
               """


def populate_products ():
    """
        запоняем таблицу
        """
    db.execute("""INSERT INTO products(
    name, description, price, photo
        )
    VALUES ('кроссовки', 'li-ning', 200, '/images/gg.jpg'),
        ('ботинки', 'зимние', 199, '/images/gg.jpg'),
        """)
    db.commit()
def get_products():
    print(cur)
    cur.execute("""
    SELECT * FROM products
    """)
    return cur.fetchall()
def