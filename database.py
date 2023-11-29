import sqlite3


from datetime import datetime

db = sqlite3.connect("dostavka.db")

fake_evos = db.cursor()


fake_evos.execute('CREATE TABLE IF NOT EXISTS user(tg_id INTEGER,name TEXT,'
                  'phone_number TEXT,address TEXT, reg_date DATETIME);')

fake_evos.execute('CREATE TABLE IF NOT EXISTS products(pr_id INTEGER PRIMARY KEY AUTOINCREMENT, pr_name TEXT'
                  'pr_price REAL,pr_quantity INTEGER, pr_des TEXT, pr_photo TEXT, reg_data DATETIME);')

fake_evos.execute('CREATE TABLE IF NOT EXISTS user_cart(user_id INTEGER, user_product TEXT, quantity INTEGER, total_for_price REAL);')


def register_user(tg_id, name, phone_number,address):
    db=sqlite3.connect("dostavka.db")

    fake_evos = db.cursor()

    fake_evos.execute("INSERT INTO users(tg_id,name,phone_number,address,reg_date) VALUES"
                      "(?,?,?,?,?);",(tg_id,name,phone_number,address,datetime.now()))

    db.commit()


def check_user(tg_id):
    db=sqlite3.connect("dostavka.db")

    fake_evos = db.cursor()

    checker = fake_evos.execute("SELECT tg_id FROM users WHERE tg_id=?;",(tg_id,))

    if checker.fetchone():
        return True
    else:
        return False

def add_product(pr_name,pr_price,pr_quantity,pr_des,pr_photo):
    db = sqlite3.connect("dostavka.db")

    fake_evos = db.cursor()

    fake_evos.execute("INSERT INTO products(pr_name,pr_price,pr_quantity,pr_des,pr_photo,reg_date) VALUES"
                      "(?,?,?,?,?,?);",(pr_price,pr_name,pr_quantity,pr_des,pr_photo,datetime.now()))
    db.commit()

# Получаем все продукты из базы только его(name, pr_id)

def get_pr_name_id():
    db = sqlite3.connect("dostavka.db")

    fake_evos = db.cursor()

    products = fake_evos.execute("SELECT pr_id,pr_name FROM products;").fetchall()

    sorted_products= [(i[1],i[0]) for i in products if i[2]>0]
    return sorted_products