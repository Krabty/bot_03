import sqlite3

connection = sqlite3.connect('db.sqlite')
cursor = connection.cursor()
cur = cursor.execute("SELECT * FROM goods")
result = cur.fetchall()
for i in result:
    print(i)

