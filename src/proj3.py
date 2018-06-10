from prettytable import PrettyTable

valid = {'0':('INDI','FAM','HEAD','TRLR','NOTE'), '1':('NAME','SEX','BIRT','DEAT','FAMC', 'FAMS', 'CHIL'), '2':('DATE')}

file_name = "../files/oneGen.ged"

ind = {}
fam = {}
currInd = ""
currDate = ""
currFam = ""
isInd = True

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
		ind[currInd] = {'id':word_list[1]}

	if isInd:
		if level == '1' and tag == 'NAME':
			ind[currInd]['name'] = arguments
		if level == '1' and tag == 'BIRT' or tag == 'MARR' or tag == 'DEAT' or tag == 'DIV':
			currDate = tag
		if currDate != "" and tag == 'DATE' and level == '2':
			ind[currInd][currDate] = arguments
		if level == '1' and tag == 'SEX':
			ind[currInd]['sex'] = arguments
		if level == '1' and tag == 'FAMC' or tag == 'FAMS':
			ind[currInd]['family'] = arguments


	if level == '0' and tag == 'FAM': # start of fam tag
		isInd = False
		currFam = word_list[1]

		fam[currFam] = {'fam': currFam}
	if isInd == False:
		if level == '1' and word_list[1] == 'MARR' or word_list[1] == 'DIV':
			currDate = tag
		if level =='2' and tag == 'DATE':
			fam[currFam][currDate] = arguments
		if level == '1' and tag in ('HUSB', 'WIFE'):
			fam[currFam][tag] = arguments

		if level == '1' and tag == 'CHIL':
			if tag in fam[currFam]:
				fam[currFam][tag].append(arguments)
			else:
				fam[currFam][tag] = [arguments]

indTable = PrettyTable(["ID", "NAME", "Gender", "BDay", "Death", "Child", "Spouse"])
indTable.align["ID"] = "1" 
print("sort by ind id")
for key in sorted(ind):
	famID = ind[key]['family']
	if fam[famID]['HUSB'] == ind[key]['id'] or fam[famID]['WIFE'] == ind[key]['id']:
		spouse = famID
		chil = "----"
	else:
		spouse = "----"
		chil = famID
	if 'DEAT' in ind[key]:
		deat = ind[key]['DEAT']
	else:
		deat = "----"
	print ("%s: %s" % (key, ind[key]['name']))
	indTable.add_row([ind[key]['id'], ind[key]['name'], ind[key]['sex'], ind[key]['BIRT'], deat, chil, spouse])

print(indTable)

famTable = PrettyTable(["ID", "Married", "Divorced", "Husb Id", "Husb Name", "Wife Id", "Wife Name", "Children"])
famTable.align["ID"] = "1" 
# print(famTable.length)
print ('Sort by famid:')
for key in sorted(fam):
	if 'DIV' in fam[key]:
		div = fam[key]['DIV']
	else: 
		div = "----"

	hubID = fam[key]['HUSB']
	hubName = ind[hubID]['name']

	wifeID = fam[key]['WIFE']
	wifeName = ind[wifeID]['name']

	chil = ','.join(fam[key]['CHIL'])

	print ("%s: husband = %s, wife = %s" % (key, fam[key]['HUSB'], fam[key]['WIFE']))
	famTable.add_row([key, fam[key]['MARR'], div, hubID, hubName, wifeID, wifeName, chil])


print(famTable)