from prettytable import PrettyTable
import mmstories
import male_names
import rs_stories
import us08
import us09
import indi_story

def gedComProj():
	valid = {'0':('INDI','FAM','HEAD','TRLR','NOTE'), '1':('NAME','SEX','BIRT','DEAT','FAMC', 'FAMS', 'CHIL'), '2':('DATE')}

	file_name = "../test/acceptanceTest.ged"

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

			# US22
			#if currInd in ids_seen:
			#	print(currInd)
			#	print ("Error: Multiple individuals with the ID " + currInd)
			#	currInd = currInd+"0"
			#	word_list[1] = currInd
			#ids_seen.append(currInd)
			#print(ids_seen[0])

			ind[currInd] = {'id':word_list[1]}


		if isInd:
			if level == '1' and tag == 'NAME':
				ind[currInd]['name'] = arguments
			if level == '1' and tag == 'BIRT' or tag == 'MARR' or tag == 'DEAT' or tag == 'DIV':
				currDate = tag
			if currDate != "" and tag == 'DATE' and level == '2':
				mmstories.checkIfDateBeforeNow(arguments)
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
				mmstories.checkIfDateBeforeNow(arguments)
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
	indi_story.checkIndividual(fam, ind)

	f= open("../test/acceptanceTestOutput.txt","a+")

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

	famTable = PrettyTable(["ID", "Married", "Divorced", "Husb Id", "Husb Name", "Wife Id", "Wife Name", "Children"])
	famTable.align["ID"] = "1" 
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
			#print(ind[fam[key]['CHIL'][0]]['BIRT'])
		else:
			chil = "----"

		if 'MARR' in fam[key]:
			marr = fam[key]['MARR']
		else:
			marr = "----"

		#US02 - RS
		if (wifeID != "----"):
			rs_stories.us02(wifeID, wifeName, ind[fam[key]['WIFE']]['BIRT'], marr, "her");
		if (hubID != "----"):
			rs_stories.us02(hubID, hubName, ind[fam[key]['HUSB']]['BIRT'], marr, "his")

		#US04 - RS
		if div != "----" and marr != "----":
			rs_stories.us04(marr, div, hubName, wifeName)

		#US08 - RS & JA
		count = 0
		if (chil != "----"):
			for i in fam[key]['CHIL']:
				if (div != "----"):
					us08.birthbeforemarri(ind[fam[key]['CHIL'][count]]['name'], i, ind[fam[key]['CHIL'][count]]['BIRT'], marr, div, True)
				else:	
					us08.birthbeforemarri(ind[fam[key]['CHIL'][count]]['name'], i, ind[fam[key]['CHIL'][count]]['BIRT'], marr, "N/A", False)	
				count = count + 1
		
		#US09 - JA
		count = 0
		if (chil != "----"):
			for i in fam[key]['CHIL']:
				if ("DEAT" in ind[fam[key]["WIFE"]] and ind[fam[key]["WIFE"]]["DEAT"] != "----"):
					us09.birthbeforedeath(ind[fam[key]['CHIL'][count]]['name'], i, ind[fam[key]['CHIL'][count]]['BIRT'], ind[fam[key]["WIFE"]]["DEAT"], True)
				elif "DEAT" in ind[fam[key]["HUSB"]] and ind[fam[key]["HUSB"]]["DEAT"]  != "----":
					us09.birthbeforedeath(ind[fam[key]['CHIL'][count]]['name'], i, ind[fam[key]['CHIL'][count]]['BIRT'], ind[fam[key]["HUSB"]]["DEAT"], False)
					ind[fam[key]["HUSB"]]["DEAT"]
				count = count + 1

		#US06 - RS
		if ((wifeID != "----") and (hubID != "----") and (div != "----")):
			if ("DEAT" in ind[fam[key]["WIFE"]] and (ind[fam[key]["WIFE"]] != "----") and (ind[fam[key]["WIFE"]]["DEAT"] != "----")):
				rs_stories.us06(wifeName, hubName, ind[fam[key]["WIFE"]]["DEAT"], div)
			elif(("DEAT" in ind[fam[key]["HUSB"]] and (ind[fam[key]['HUSB']]["DEAT"]) != "----" and (ind[fam[key]["HUSB"]]["DEAT"] != "----"))):
				rs_stories.us06(wifeName, hubName, ind[fam[key]["HUSB"]]["DEAT"], div)

		#US18 - RS
		rs_stories.us18(wifeName, wifeID, hubName, hubID, fam)
		
		f.write("%s: husband = %s, wife = %s" % (key, hubName, wifeName+"\n"))
		famTable.add_row([key, marr, div, hubID, hubName, wifeID, wifeName, chil])
		

	f.write(famTable.get_string())
	f.write("\n")

	return {"fam":fam, "ind":ind}
