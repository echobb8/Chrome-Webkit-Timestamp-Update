#!/usr/bin/env python
import sqlite3

sqlite_file = 'History'
table_name = 'downloads'
start_time_column = 'start_time'
end_time_column = 'end_time'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

start_time = "SELECT datetime((start_time/1000000)-11644473600, 'unixepoch', 'localtime')"
end_time = "SELECT datetime((end_time/1000000)-11644473600, 'unixepoch', 'localtime')"

# Update start_time column with readable format
c.execute("UPDATE {tn} SET {st}=({dt})".\
    format(tn=table_name, st=start_time_column, dt=start_time))

# Update end_time column with readable format
c.execute("UPDATE {tn} SET {et}=({dt})".\
    format(tn=table_name, et=end_time_column, dt=end_time))

conn.commit()
conn.close()
