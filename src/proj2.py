valid = {'0':('INDI','FAM','HEAD','TRLR','NOTE'), '1':('NAME','SEX','BIRT','DEAT','FAMC', 'FAMS', 'CHIL'), '2':('DATE')}

file_name = "../files/oneGen.ged"

ind = {}
fam = {}
count = 0
currInd = ""
currDate = ""
currFam = ""
famCount =0
isInd = True
idList = {}
famList = {}

try:
	file = open(file_name)
except IOError:
	raise IOError("Can't open '{}'".format(file_name))

for line in file:
	#print("--> {}".format(line.strip()))

	word_list = line.strip().split()
	isValid = 'N'
	level = "NA"
	tag = "NA"
	arguments = " ".join(word_list[2:])

	if len(word_list) == 1:
		level = word_list[0]

	elif len(word_list) > 1:
		level = word_list[0]
		tag = word_list[1]

	if len(word_list) == 3 and word_list[0] == '0' and word_list[2] in ('INDI', 'FAM'):
		isValid = 'Y'
		tag = word_list[2]

	elif len(word_list) > 1 and level in valid and tag in valid[level]:
		isValid = 'Y'

	
	
#if isValid == 'Y': # can create id 
	if level == '0' and tag == 'INDI': #start of individual
		currInd = word_list[1]
		isInd = True
		count +=1
		ind[count] = {'id':word_list[1]}
		idList[currInd] = count

	if isInd:
		if level == '1' and tag == 'NAME':
			ind[count]['name'] = arguments
		if level == '1' and tag == 'BIRT' or tag == 'MARR' or tag == 'DEAT' or tag == 'DIV':
			currDate = tag
		if currDate != "" and tag == 'DATE' and level == '2':
			ind[count][currDate] = arguments
		if level == '1' and tag == 'SEX':
			ind[count]['sex'] = arguments
		if level == '1' and tag == 'FAMC' or tag == 'FAMS':
			ind[count]['family'] = arguments


	if level == '0' and tag == 'FAM': # start of fam tag
		isInd = False
		currFam = word_list[1]
		famCount +=1
		famList[currFam] = famCount

		fam[famCount] = {'fam': currFam}
	if isInd == False:
		if level == '1' and word_list[1] == 'MARR' or word_list[1] == 'DIV':
			currDate = tag
		if level =='2' and tag == 'DATE':
			fam[famCount][currDate] = arguments
		if level == '1' and tag in ('HUSB', 'WIFE'):
			fam[famCount][tag] = arguments

		if level == '1' and tag == 'CHIL':
			if tag in fam[famCount]:
				fam[famCount][tag].append(arguments)
			else:
				fam[famCount][tag] = [arguments]
print(ind)
print(fam)
print(idList)

print ('Sort by keys:')
for key in sorted(idList.keys()):
	num = idList[key]
	print ("%s: %s" % (key, ind[num]['name']))

print ('Sort by keys:')
for key in sorted(famList.keys()):
	numFam = famList[key]
	print ("%s: husband = %s, wife = %s" % (key, fam[numFam]['HUSB'], fam[numFam]['WIFE']))