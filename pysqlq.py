#!/usr/bin/python
#pysqlq.py Written by David J Johns II
#https://github.com/djjohns

#Simple sqlite3 db query

import sqlite3

conn = sqlite3.connect('LogDB.db')

#------------------------------------------------------------------------------#
#row_factory to return results as Row objects similar to python dictionaies
#giving one access to row's feilds like a dictionary
#however one can not do an item assignment with a Row object.
#
#conn.row_factory = sqlite3.Row
#------------------------------------------------------------------------------#

cursor = conn.cursor()

#------------------------------------------------------------------------------#
#First sql query to select all records from specified Field that match what
#we pass in.

#Swap comments to change from All results to First result
sql = 'SELECT * FROM ObjectLogTbl WHERE Discription=?'
cursor.execute(sql, [('verification error')])
print cursor.fetchall()
#print cursor.fetchone()

print'\nHere is a listing of all the records in the table:\n'
#print'\nHere is the listing you reqested:\n'

#------------------------------------------------------------------------------#
#Next query looping over the results from putting them in ascending
#order by rowid
#for row in cursor.execute('SELECT rowid, * FROM ObjectLogTbl ORDER BY Date'):
#   print row
#
#------------------------------------------------------------------------------#
#Lastly a sql query to use LIKE to search the entire table
#for partial strings using the % as a wildcard operator
#print '\nResults from LIKE query:\n'
#sql = """
#SELECT * FROM ObjectLogTbl
#WHERE Discription Like 'verifcation error%'"""
#cursor.execute(sql)
#print cursor.fetchall
#print cursor.fetchone
