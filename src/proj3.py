from prettytable import PrettyTable
import mmstories
import male_names

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
			if(mmstories.checkIfDateBeforeNow(arguments)): #checks to see if after or before date and does not add if after
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
			if(mmstories.checkIfDateBeforeNow(arguments)):
				fam[currFam][currDate] = arguments
		if level == '1' and tag in ('HUSB', 'WIFE'):
			fam[currFam][tag] = arguments

		if level == '1' and tag == 'CHIL':
			if tag in fam[currFam]:
				fam[currFam][tag].append(arguments)
			else:
				fam[currFam][tag] = [arguments]

mmstories.checkLessThan5SharedSiblingBdays(fam, ind);
male_names.checkSameLastNames(fam, ind)

f= open("../test/proj3.txt","a+")

indTable = PrettyTable(["ID", "NAME", "Gender", "BDay", "Death", "Child", "Spouse"])
indTable.align["ID"] = "1" 
f.write("sort by ind id:"+"\n")
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
	f.write("%s: %s" % (key, ind[key]['name'])+"\n")
	indTable.add_row([ind[key]['id'], ind[key]['name'], ind[key]['sex'], ind[key]['BIRT'], deat, chil, spouse])

f.write(indTable.get_string() + "\n")

print(fam)
print(ind)

famTable = PrettyTable(["ID", "Married", "Divorced", "Husb Id", "Husb Name", "Wife Id", "Wife Name", "Children"])
famTable.align["ID"] = "1" 
# print(famTable.length)
f.write('Sort by famid:'+"\n")
for key in sorted(fam):
	if 'DIV' in fam[key]:
		div = fam[key]['DIV']
	else: 
		div = "----"

	if "HUSB" in fam[key]:
		hubID = fam[key]['HUSB']
		hubName = ind[hubID]['name']
	else:
		hubID = "----"
		hubName = "----"

	if "WIFE" in fam[key]:
		wifeID = fam[key]['WIFE']
		wifeName = ind[wifeID]['name']
	else:
		wifeID = "----"
		wifeName = "----"

	if 'CHIL' in fam[key] :
		chil = ','.join(fam[key]['CHIL'])
	else:
		chil = "----"

	if 'MARR' in fam[key]:
		marr = fam[key]['MARR']
	else:
		marr = "----"

	f.write("%s: husband = %s, wife = %s" % (key, hubName, wifeName+"\n"))
	famTable.add_row([key, marr, div, hubID, hubName, wifeID, wifeName, chil])


f.write(famTable.get_string())