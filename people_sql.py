import sqlite3
import pprint
import tab
sqlite_file='test_db'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('SELECT * FROM people ')
all_rows = c.fetchall()
#sqlite returns an array of tuples...
data=[[col for col in r] for r in all_rows]
pprint.pprint(all_rows)
pprint.pprint(data)
rt=tab.rndtab()
rt.setdata(data)
rt.random_row()
rt.dump()

