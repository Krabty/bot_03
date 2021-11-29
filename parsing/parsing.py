import sqlite3
from sqlite3 import Error
import requests
from bs4 import BeautifulSoup

import logging

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
                    )


def create_connection(db_file):
    """
    create a database connection to the SQLite database
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return connection


def execute(connection, query, param=None, many=False):
    """
    Create a new project into the projects table
    :param many: executemany()
    :param connection: connect object
    :param query: sql query to execute
    :param param: tuple of  values
    """
    cursor = connection.cursor()
    if param is None:
        cursor.execute(query)
    else:
        if many:
            cursor.executemany(query, param)
        else:
            cursor.execute(query, param)
    connection.commit()


def parsing(url):
    """
    Parsing URL to get product name, price, link
    :param url: connect object
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 '
                      'Safari/537.3'}
    response = requests.get(url, 'html.parser', headers=headers)

    soup = BeautifulSoup(response.text, features='html.parser')  # TODO: features='lxml'
    category_site = soup.find_all('span', class_="inline-title")
    all_items = soup.find_all('div', class_='porto-products wpb_content_element')

    result = []
    for n, i in enumerate(category_site):
        db_category = i.text
        items = all_items[n].find_all('h3')
        price = all_items[n].find_all('span', class_='woocommerce-Price-amount amount')
        link = all_items[n].find_all('a', class_='product-loop-title')

        for m, q in enumerate(items):
            db_item = q.text
            db_price = price[m].text.replace("руб.", "")
            db_url = link[m].get('href')
            db_list = (db_category, db_item, db_price, db_url)
            result.append(db_list)
    return result


def run_parsing():
    target_url = 'https://prisma.by'
    database = "db.sqlite"

    create_query = "CREATE TABLE IF NOT EXISTS goods(category TEXT,item TEXT, price TEXT,url TEXT);"
    insert_query = "INSERT INTO goods(category, item, price, url) VALUES (?, ?, ?, ?) ;"
    conn = create_connection(database)

    with conn:
        execute(conn, create_query)
        r = parsing(target_url)

        # вставляем по одной строке за раз
        # for elem in r:
        #     execute(connection=conn, query=insert_query, param=elem)

        # вставляем весь список кортежей за раз
        execute(connection=conn, query=insert_query, param=r, many=True)


if __name__ == '__main__':
    run_parsing()
