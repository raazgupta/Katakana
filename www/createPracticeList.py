import csv

#Open the katakana csv file to read
ifile = open('katakana.csv', 'rb')
reader = csv.reader(ifile)

#Create a list to store the values to write to practiceList.js
pList = []
filenameWrite = 'practiceList.js'

pList.append("var practiceList = new Array();\n");

#Populate pList with the contents of the Javascript file
rownum = 0;
for row in reader:
	pList.append("practiceList["+str(rownum)+"] = new Array();\n")
	colnum = 0
	for col in row:
		pList.append("practiceList["+str(rownum)+"]["+ str(colnum) +"] = '" + col + "';\n")
		colnum = colnum + 1
	rownum = rownum + 1

#create a file object in write mode
FILE = open(filenameWrite, "w")
for line in pList:
	FILE.write(line)
FILE.close()
