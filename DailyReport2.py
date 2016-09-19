#!/usr/bin/python
#DailyReport.py Written by David J Johns II
#https://github.com/djjohns
#------------------------------------------------------------------------------#
#Python script to parse data from a /t delimited txt file and write to
#a , delimited csv file.
#Then takes the csv file and injects it into a DB table.
#Lastly queries  said table for specified data and writes out to another csv
#file to be injected into a seperate DBtable.
#------------------------------------------------------------------------------#

import csv
import sqlite3
#------------------------------------------------------------------------------#
#Convert input txt file to to write out to csv file
#------------------------------------------------------------------------------#
#Program will try to open users requested file into file handler
with open('SampleData.txt','rb') as txt_in:
    with open('LogFile.csv','wb') as csv_out:
        for line in txt_in:
            fields = line.split('\t')
            csv_out.write(','.join(fields))

csv_out.close()

#------------------------------------------------------------------------------#
#Setup our DB connection and cursor
#------------------------------------------------------------------------------#

conn = sqlite3.connect('LogDB.db')
cursor = conn.cursor()

#------------------------------------------------------------------------------#
#Drop or create table to push the data from input file to
#------------------------------------------------------------------------------#

#Create the DB table using the above cursor variable
cursor.execute('DROP TABLE IF EXISTS ObjectLogTbl')
#Create the schema for the DB table
cursor.execute('CREATE TABLE ObjectLogTbl(Date smalldatetime,UPC interger,Bin interger,Event interger,Discription VARCHAR)')
#commit changes to the DB table using the conn variable
conn.commit()
#Load specified CSV file into CSV reader given path
csvfile = open('LogFile.csv', 'rb')
csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')

#Iterate through the above CSV reader, inserting values into the DB table
for text in csvreader:
    cursor.execute('INSERT INTO ObjectLogTbl VALUES (?,?,?,?,?)', text)

#Close the CSV file, Commit changes to DB table, and close the Connection.
csvfile.close()
conn.commit()

#------------------------------------------------------------------------------#
#First, sql query to select all records from specified Field that match what
#we pass in.
sql = 'SELECT * FROM ObjectLogTbl WHERE Discription=?'
data = cursor.execute(sql, [('verification error')])

#------------------------------------------------------------------------------#
#Writting data to a csv file
with open('CsvOut2.csv','wb') as fh:
    writer = csv.writer(fh)
    writer.writerows(data)
    print'\nReport written:\n'

conn.close()
