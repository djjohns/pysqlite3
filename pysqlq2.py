#!/usr/bin/python
#pysqlq.py Written by David J Johns II
#https://github.com/djjohns

#Simple sqlite3 db query
import csv
import sqlite3

conn = sqlite3.connect('LogDB.db')

cursor = conn.cursor()

#------------------------------------------------------------------------------#
#First sql query to select all records from specified Field that match what
#we pass in.

#Swap comments to change from All results to First result
sql = 'SELECT * FROM ObjectLogTbl WHERE Discription=?'
data =cursor.execute(sql, [('verification error')])

with open('CsvOut2.csv','wb') as fh:
    writer = csv.writer(fh)
    writer.writerows(data)

#print cursor.fetchall()
#print cursor.fetchone()

print'\nReport written:\n'
#print'\nHere is the listing you reqested:\n'

