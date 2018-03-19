#!/usr/bin/env python
import sqlite3

sqlite_file = 'History' # path to the sqlite Chrome History database file.
table_name = 'downloads' # the table you want to manipulate, in this case the downloads history.
start_time_column = 'start_time' # first column you want to edit with the Chrome/webkit formatted timestamps.
end_time_column = 'end_time' # this is an additional column you may want to edit in the downloads table.
# you can always add more columns that contain timestamp data and modify the code below.

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# creating a variable to hold the converted timestamps for each of the above defined columns
start_time = "SELECT datetime((start_time/1000000)-11644473600, 'unixepoch', 'localtime')"
end_time = "SELECT datetime((end_time/1000000)-11644473600, 'unixepoch', 'localtime')"

# Update start_time column with readable format
c.execute("UPDATE {tn} SET {st}=({dt})".\
    format(tn=table_name, st=start_time_column, dt=start_time))

# Update end_time column with readable format
c.execute("UPDATE {tn} SET {et}=({dt})".\
    format(tn=table_name, et=end_time_column, dt=end_time))

# Commit changes and close the connection.
conn.commit()
conn.close()
