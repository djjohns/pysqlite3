#Written by David J JohnsII
#Program for exporting a SQLite3 DB table to a CSV file

#import required libraries
import csv
import sqlite3

#Establish a connection variable(conn) to point to the path of the DB
# if not in the current DIR
conn = sqlite3.connect('ProductInfoDB.db')
cursor = conn.cursor()

#Create a data variable to store data from required DB table
# using the the above cursor variable
data = cursor.execute('SELECT * FROM ProductInfoTbl')

#Create and open an ouput file to write to using a FileHandler
# variable(fh), writing the above data variable into the specified output CSV
# file's rows
with open('CsvOut.csv', 'wb') as fh:
    writer = csv.writer(fh)
    writer.writerows(data)

#Close the File handler variable which closes the CsvOut.csv file
# then close the conn variable which closes the connection to the DB
fh.close()
conn.close()
