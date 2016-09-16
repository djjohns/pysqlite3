#!/usr/bin/python
CreateTable.py Written by David J Johns II
#https://github.com/djjohns
#Python script to create a DBtable

#------------------------------------------------------------------------------#
#There are five datatypes in sqlite3 the are:
#-Null- a null value
#-INTEGER- an integer stored as 1-8 bytes depndent on magnitude of value
#-REAL-floating point value stored as 8byte IEEE floating point number
#-TEXT- text string value stored using the DB encoding UTF-8,UTF-16BE,UTF-16LE
#-BLOB- blob of data stored exactly as it was input
#Date and time stored as three types:
#-TEXT- as ISO8601 strings ("YYYY-MM--DD HH:MM:SS.SSS")
#-REAL- as julian day numbers,the number of days since noon in Greenwich
#on November 24, 4714 B.C. according to the proleptic Gregorian calendar.
#-INTEGER-as Unix time,the number of seconds since 1970-01-01 00:00:00 UTC.
#------------------------------------------------------------------------------#

import sqlite3

conn = sqlite3.connect('mydatabase')
cursor = conn.cursor

cursor.execute("""CREATE TABLE tablename
               (fieldname1 datatype, fieldname2 datatype,
                fieldname3 datatype, fieldname4 datatpye,
                fieldname5 datatype)
               """)

