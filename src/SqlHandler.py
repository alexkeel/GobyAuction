import sqlite3


def add_to_database(database, item_id, title, link, image_link, price, purchase_type, website):

    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    title = title.replace("\"", "\\""")
    print(title)
    sql_command = ("INSERT OR IGNORE INTO item(item_id, title, price, item_link,"
                   + "image_link, purchase_type, website)"
                   + "VALUES (" + "\"" + item_id + "\"" + ", " + "\""
                   + title + "\"" + ", "
                   + "\"" + link + "\"" + ", " + "\""
                   + image_link + "\"" + ", "
                   + "\"" + price + "\"" + ", " + "\""
                   + purchase_type + "\"" + ", "
                   + "\"" + website + "\"" + "); ")

    cursor.execute(sql_command)
    connection.commit()
    connection.close()


def create_database(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
        
    sql_command = """
    CREATE TABLE IF NOT EXISTS item(
    item_id INTEGER PRIMARY KEY,
    title VARCHAR(50),
    price VARCHAR(10),
    item_link VARCHAR(500),
    image_link VARCHAR(500),
    purchase_type varchar(10),
    website varchar(20)); """

    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    print("Database Created")

    
def drop_table(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    sql_command = "DROP TABLE IF EXISTS item;"

    cursor.execute(sql_command)
    connection.commit()
    connection.close()
    print("Dropped table")

    
def print_table(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM item")
    for row in cursor.fetchall():
        print(row)
        print()
    connection.commit()
    connection.close()
    
    
def get_table(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM item")
    return cursor.fetchall()
