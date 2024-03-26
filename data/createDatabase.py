import sqlite3

conn = sqlite3.connect('signals.db')

cur = conn.cursor()

##TODO : read csv and insert data in database
#conn.commit()

rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
