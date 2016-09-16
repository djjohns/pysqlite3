#!/usr/bin/python
#DailyReport.py Written by David J Johns II
#https://github.com/djjohns

import csv
import sqlite3

conn = sqlite3.connect('LogDB.db')
cursor = conn.cursor()
#------------------------------------------------------------------------------#
#First, sql query to select all records from specified Field that match what
#we pass in.
sql = 'SELECT * FROM ObjectLogTbl WHERE Discription=?'
data = cursor.execute(sql, [('verification error')])
#------------------------------------------------------------------------------#
#Writting Data to a csv file
with open('CsvOut2.csv','wb') as fh:
        writer = csv.writer(fh)
            writer.writerows(data)

            print'\nReport written:\n'
