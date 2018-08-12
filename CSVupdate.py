'''

		MCCARDELL BICENTTENIAL HALL SASH HEIGHT MASTER CSV FILE UPDATE SCRIPT

		BENJAMIN GLASS 

		MIDDLEBURY COLLEGE

		08/11/2018

		DESCRIPTION: CSVupdate.py updates a master CSV file with fume hood ("sash") height data from all recorded time periods from
		labratory spaces in Bicenttenial Hall. Output is a multiple column CSV file that included fume hood number, and heights from
		various timestamps. The output could be used for statistical analysis in Rstudio or other software.

		Data Types: CSV -> CSV
'''

import CSVparsing
import pandas as pd


def parse(fileName):

	CSVparsing.main(fileName)


def add(fileName):


	dfNew = pd.read_csv('p%s'%fileName)
	file = 'p%s' % fileName
	saved_column = dfNew[file[5:-4]]
	dfMaster = pd.read_csv('MASTER.csv')
	dfMaster[file[5:-4]] = saved_column

	dfMaster.to_csv('MASTER.csv')
	dfMaster.drop(dfMaster.columns[[0]], axis=1)


def main():

	fileName = input("File In:")
	parse(fileName)
	add(fileName)


if __name__ == "__main__":
	main()





















#you can also use df['column_name']


'''
csv_input.to_csv('output.csv', index=False)

df1 = df.iloc[:,0:2]
'''
