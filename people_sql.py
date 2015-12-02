import sqlite3
import pprint
import tab
sqlite_file='test_db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('SELECT * FROM people ')
all_rows = c.fetchall()
#sqlite returns an array of tuples...
#Convert into a nested array
data=[[col for col in r] for r in all_rows]
"""
Now use the rndtab class -
"""
rt=tab.rndtab()
rt.setdata(data)
pprint.pprint(rt.random_row())
rt.dump()

