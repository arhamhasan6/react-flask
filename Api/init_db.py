import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO todo ( content) VALUES   ('Content for the first post')" )
cur.execute("INSERT INTO todo ( content) VALUES   ('Content for the second post')" )
cur.execute("INSERT INTO todo ( content) VALUES   ('Content for the third post')" )

     
# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )


connection.commit()
connection.close()