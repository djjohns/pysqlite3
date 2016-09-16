#!/usr/bin/python
#txt2csv.py written by David J. Johns II to aid in converting a tab
#dilimited text file into a csv file for easier data manipulation
#https://github.com/djjohns

#import the csv library
import csv

#Prompts user for file name
#if user presses enter, program will open specified txt file
FileName = raw_input('Enter file name:')
if len(FileName) < 1 : FileName = 'SampleData.txt'

#Program will try to open users requested file into file handler
try:
    fh_in = FileName

#Error message to inform of bad input
except:
    print 'File could not be found: ',FileName

#File handler for the output file
fh_out = r'LogFile.csv'

#txt_in reads the input file, csv_out writes to specified file
#'b' imporves portablity to windows reading in binary
txt_in = csv.reader(open(fh_in, 'rb'), delimiter='\t')
csv_out = csv.writer(open(fh_out,'wb'),delimiter=',')

#Writes out file given in file
csv_out.writerows(txt_in)

