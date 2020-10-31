#!/usr/bin/python
# cru_download_proc.py
#
# This script will process CRU precipitation ASCII files, although with slight modification could be
# 	used to download other CRU climate variables.  The files are downloaded as a large text file 
#	(~2.7 GB, '.dat').  The data is continuous so each 360 rows is a one 'dataset'.
# The dates go from 372 to 1643 months since 1-1-1870.
# The cru_ts_3_00.1901.2006.pre.xml metatdata file contains this information as well as a list of
#	center coordinates for each cell.
#
# The header format is:
#	ncols  720
#	nrows  360
#	xllcorner  -180
#	yllcorner  -89.9999999999999
#	cellsize 0.5
#	NODATA_value  -999
#
# Written by: 	 Kevin Guay (kguay@whrc.org)
# Date created:	 8-21-2012
# Last modified: 8-21-2012
#
# Version Log:
#  1.1	Fixed issue that caused image to be displayed upsidedown [kg]

inFileName = 'cru_ts_3_10_01.1901.2009.pre.dat'
inFile = open(inFileName, 'r')

header = ['ncols 720\n','nrows 360\n','xllcorner -180\n','yllcorner -89.9999999999999\n','cellsize 0.5\n','NODATA_value  -999\n']

startMonthNum = 372
endMonthNum = 1680
for monthNum in range(startMonthNum,endMonthNum):
	# calculate the year and month of the current "dataset"
	year = 1870 + (monthNum//12)
	month = (monthNum - ((year-1870)*12)) + 1
	
	# concatenate the filename
	outFileName = 'pre/cru_ts_3_10_01.1901.2009.pre_' + str(year) + '_' + str(month) + '.asc'
	outFile = open(outFileName, 'w')
	print(outFileName)
	
	startLineNum = 360*(monthNum-startMonthNum)
	endLineNum = startLineNum + 360
	# write the header to the beginning of the list
	lines = []
	
	for lineNum in range(startLineNum, endLineNum):
		line = inFile.readline()
		lines.append(line)
		#print(lineNum)
	# write header & lines to output file
	lines.reverse() # for some reason the lines reverse themselves in the list, so this puts them back in the right order
	lines = header + lines # concat. header and the lines 
	outFile.writelines(lines)
	outFile.close()	# close the output file
inFile.close()	# close the input file