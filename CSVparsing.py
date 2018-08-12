'''

		MCCARDELL BICENTTENIAL HALL SASH HEIGHT RAW DATA PARSING SCRIPT

		BENJAMIN GLASS 

		MIDDLEBURY COLLEGE

		08/09/2018

		DESCRIPTION: CSVparsing.py parses extraneous characters and spaces from raw data files of fume hood ("sash") heights in
		labratory spaces in Bicenttenial Hall. Output is a three column CSV file that included timestamps, fume hood number, and height.
		The output could be used for statistical analysis in Rstudio or other software. The outputed data file is also better for
		general reading. 

		Data Types: CSV -> CSV
'''


import csv
import pandas as pd
import numpy as np
import statistics



# Reads in csv.file with input variable, grabs metadata(timestamp) and all sash names and heights, returns an array with all three values
def readin(file, sashArray):


	with open(file, 'r') as f:
	    reader = csv.reader(f)

	    #MIGHT NEED TO NOT HARD CODE THIS - GETS RID OF EMPTY LINES AT BEGGINING OF CSV
	    next(reader)
	    next(reader)
	    next(reader)


	    metadata = next(reader)[0]
	    #print(metadata)
	    metadata = str(file)[4:-4]
	    print(metadata)

	    for row in reader:

	    	if len(row) == 0:
	    		pass

	    	elif row[0].find('49 BCHFH') != -1:
	    		sashArray.append(row[0])

	return [sashArray,metadata]



# Parses the sash names and heights from the original csv to just their names and heights (no extranious characters or spaces). Returns this data in a two column array.
def parse(sashArray):

	Rooms = []
	Heights = []

	for row in sashArray:
		
		first = row.find('RM')
		second = row.find(':')
		Rooms.append(row[first:second])

		third = row.find('SASH1')
		fourth = row.find('INCHES')

		num = row[third+5:fourth]

		newNum = ""

		for i in num:
			if i != " ":
				newNum+=i


		Heights.append(float(newNum))

	return [Rooms,Heights]


# writes parsed data out into a new csv file.
def writeOut(metadata,Rooms,Heights,fileOut):


	df = pd.DataFrame({"HOOD NUMBER (RM-NNN-L)" : Rooms, "%s" % (metadata) : Heights})
	df.to_csv(fileOut, index=False)




def main(fileName):

	# Initilize list variable
	newArray = []

	print("\n")
	file = fileName
	[midArray,metadata] = readin(file, newArray)
	[Rooms,Heights] = parse(midArray)

	writeOut(metadata,Rooms,Heights,"p%s"%(file))


	count = 0
	for i in Heights:
		if i>1:
			count+=1

	guilty = []
	for i in zip(Rooms,Heights):

		if i[1] > 1:
			guilty.append(i)

	print("\n\n\nSASHES - STATISTICAL DATA")
	print("********************************************\n")
	print("Count:", len(Heights))
	print("Count < 1 inch:", len(Heights)-count)
	print("Count > 1 inch:", count)
	print("Maximum height (in):",max(Heights))
	print("Median height (in):",statistics.median(Heights))

	print("Percentage > 1 inch (%): ",round(count/len(Heights)*100,2))
	print("\n\nSashes > 1 inch (",count,"):\n")
	for i in guilty:
		print(i[0],"\t",i[1])
	
	print("\n\n\n")










  

