#!/usr/bin/python
#DeleteEntries.py Written by David J Johns II
#https://github.com/djjohns
#Python script to delete specified data from a DBTable's fieldname

import sqlite3
#------------------------------------------------------------------------------#
#Connection to specified DB and cursor handlers
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor
#------------------------------------------------------------------------------#
#sql statement to delete specified data from a Table's fieldname
sql = """
DELETE FROM tablename
WHERE fieldname = 'DataToDelete'
"""
#------------------------------------------------------------------------------#
#Execute sql statement and commit changes
cursor.execute(sql)
conn.execute
