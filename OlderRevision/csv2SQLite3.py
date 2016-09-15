#Written by David J Johns II
#Program to import CSV files to a SQLite3 DataBase Table

#Import required libaries
import csv
import sqlite3

#Create the database

#Create a connection variable to point to the path of the DB if not
# in current DIR
conn = sqlite3.connect('ProductInfoDB.db')
cursor = conn.cursor()

#Create the DB table using the above cursor variable
cursor.execute('DROP TABLE IF EXISTS ProductInfoTbl')
#Create the schema for the DB table
cursor.execute('CREATE TABLE ProductInfoTbl(UPC integer,WH varchar(2),Title text,Loc blob,Qty integer)')
#commit changes to the DB table using the conn variable
conn.commit()

#Load specified CSV file into CSV reader given path
csvfile = open('ProductInfo.csv', 'rb')
csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')

#Iterate through the above CSV reader, inserting values into the DB table
for text in csvreader:
    cursor.execute('INSERT INTO ProductInfoTbl VALUES (?,?,?,?,?)', text)

#Close the CSV file, Commit changes to DB table, and close the Connection.
csvfile.close()
conn.commit()
conn.close()
