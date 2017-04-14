#!/usr/bin/python

# Import the urllib2 module to read files from football-data.co.uk
import urllib2
import csv
import os
import os.path

# Assign the file URL to variable
file = "http://www.football-data.co.uk/mmz4281/1617/E3.csv"
# Assign the target file to variable
target = "/home/andy/Documents/Target.csv"

#Clean up target
if os.path.isfile(target):
	os.remove(target)
	print "Target deleted ready."
else:
	print "Target does not exist, continue."

# User urllib2  to open the file url
inputfile = urllib2.urlopen(file)
# Read the file
csvfilereader = csv.reader(inputfile, delimiter=',')
# Open our output file (file to write to)
outputfile = open(target, "wb")
# Write the file
csvfilewriter = csv.writer(outputfile, delimiter=',')


# Write each row to the target
for row in csvfilereader:
	csvfilewriter.writerow(row)

# Close the input and output files
inputfile.close()	
outputfile.close()