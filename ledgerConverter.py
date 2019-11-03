import sys
import os
import csv
import re
import datetime
import itertools as it


# account identifiers (e.g. 4-digit acct#)
boa_cc_acct='1234'				
boa_chk_acct='5678'

def ledgerConvert(filename, outfile):

	with open(filename) as csvFile:
		readCSV= csv.reader(csvFile, delimiter=',')
		l1= next(readCSV)

		if l1[0]=='Posted Date':
			print('parsing bofa cc')
			bofa_convert_cc(filename, outfile)

		elif l1[0]=='Description':
			print('parsing bofa checking')
			bofa_convert_chkng(filename, outfile)

		elif l1[0]==' Username':
			print('parsing venmo transactions')
			venmo_convert(filename, outfile)
		
		elif l1[0]=='Transaction Date':
			print('parsing capital1')
			with open(outfile,'a', newline='') as csvOut:
				writeCSV= csv.writer(csvOut)
				for r in readCSV:
					writeCSV.writerow(r)

		else:
			print('Unrecognized file type!!', filename)

	return
			

def bofa_convert_cc(filename, outfile):

	acct=boa_cc_acct	# Number on account

	with open(filename) as csvFile:
		with open(outfile,'a', newline='') as csvOut:
			readCSV= csv.reader(csvFile, delimiter=',')
			writeCSV= csv.writer(csvOut)
			next(readCSV) # Iterate through header line

			for r in readCSV:
				if len(r) != 5:
					print('Error, cannot parse row %s'% r[-1])
				if float(r[4]) < 0:
					writeCSV.writerow([' ', r[0], acct, r[2], 'fill_category', -float(r[4]), ' '])
				if float(r[4]) >= 0:
					writeCSV.writerow([' ', r[0], acct, r[2], 'fill_category', ' ', r[4]])
	return


def bofa_convert_chkng(filename, outfile):
	acct=boa_chk_acct    # Hardcoded checking number

	with open(filename) as csvFile:
		with open(outfile,'a', newline='') as csvOut:
			readCSV= csv.reader(csvFile, delimiter=',')
			readCSV=it.islice(readCSV, 8, None)
			writeCSV= csv.writer(csvOut)

			for r in readCSV:
				if len(r) != 4:
					print('Error, cannot parse row %s'% r[-1])
				if float(r[2]) < 0:
					writeCSV.writerow([' ', r[0], acct, r[1], 'fill_category', -float(r[2]), ' '])
				if float(r[2]) >= 0:
					writeCSV.writerow([' ', r[0], acct, r[1], 'fill_category', ' ', r[2]])	
	return


def venmo_convert(filename, outfile):
	acct='venmo'    # Hardcoded checking number

	with open(filename) as csvFile:
		with open(outfile,'a', newline='') as csvOut:
			readCSV= csv.reader(csvFile, delimiter=',')
			readCSV=it.islice(readCSV, 2, None)
			writeCSV= csv.writer(csvOut)

			for r in readCSV:
				if len(r) != 17:
					print('Error, cannot parse row %s'% r[-1])
				if r[1]=='':
					return;

				dt= datetime.datetime.strptime(r[2], '%Y-%m-%dT%H:%M:%S')
				date=dt.strftime("%m/%d/%Y")

				amt=r[8].split()
				num= re.findall(r'\d+.\d+',amt[1]) 

				if amt[0] == '+':
					writeCSV.writerow([' ', date, acct, r[5]+', '+r[6]+' to  '+r[7], 'fill_category', num[0], ' '])
				if amt[0] == '-':
					writeCSV.writerow([' ', date, acct, r[5]+', '+r[6]+' to  '+r[7], 'fill_category', ' ', num[0], ' '])

	return

if __name__=="__main__":

	if len(sys.argv)==1:
		fold= './'
	else:
		fold = sys.argv[1]

	outfile='fullLedger.csv'

	if os.path.exists(outfile):
		os.remove(outfile)

	fileList= os.listdir(fold)
		
	for file in fileList:
		if file.endswith('.csv'):
			print(fold+file)
			ledgerConvert(fold+file, outfile)



	
