'''
Created on May 5, 2016

@author: 502569308
'''
import csv
#fin = open("c:\private\work\python\OOR_REPORT.csv")
fin = 'c:\private\work\python\OOR_REPORT.csv'

with open(fin,newline = '') as f:
    reader = csv.reader(f)
    row1 = next(reader) 

print (row1)