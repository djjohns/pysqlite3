#!/usr/bin/python
#UpdateTable.py Written by David J Johns II
#https://github.com/djjohns
#Python script to change data in a database table's field
#from one thing to another for all entries in a DBTable.

import sqlite3
#------------------------------------------------------------------------------#
#connect to specifed DataBase
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

#------------------------------------------------------------------------------#
#sql statement to change data in a specified fieldname from
#DataToChange>ChangeDataTo for all recurenses within the table
sql = """
UPDATE tablename
SET fieldname = 'ChangeDataTo'
WHERE fieldname = 'DataToChange'
"""
#------------------------------------------------------------------------------#
#execute sql statement then commit changes
cursor.execute(sql)
conn.commit
