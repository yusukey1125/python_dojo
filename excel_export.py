resultFile=open("C:\\Users\\.....\\output.csv",'w')
with open("C:\\Users\\.....\\....txt") as file_1:
	for i, line in enumerate(file_1):
		if i < 1:
    			continue
		intermediary_object=line.split("|")
		state=intermediary_object[42] 
		yearVal=intermediary_object[96]
		if yearVal!='':
			yearVal=int(yearVal[0:4])
			if state=="WI":
				if yearVal>=2000 and yearVal<=2019:
					line=line.replace('|',',')
					resultFile.write(line)
					resultFile.write('\n')#WriteElementtoRow
resultFile.close()