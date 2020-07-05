import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
org = 1
cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
row = cur.fetchone()
print(row)
