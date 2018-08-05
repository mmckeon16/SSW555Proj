import unittest
from datetime import datetime
from prettytable import PrettyTable

#US01
def checkIfDateBeforeNow(date, f):
	try:
		givenDate = datetime.strptime(date, '%d %b %Y')
		currDate = datetime.today()
		if givenDate <= currDate:
			return True
		else:
			f.write("ERROR: US01 The date "+ date+ " is after the current date\n")
			return False
	except:
		return False

#US14
def checkLessThan5SharedSiblingBdays(fam, ind, file):
	for f in fam:
		if "CHIL" in fam[f]:
			if len(fam[f]["CHIL"]) > 4: #could be situation where more than 5
				children = fam[f]["CHIL"].copy()
				dates = {}
				for c in children: #have list of children
					cDate = ind[c]["BIRT"]
					if cDate in dates:
						dates[cDate] = dates[cDate] + 1
					else:
						dates[cDate] = 1
				for d in dates:
					if dates[d] >= 5:
						#NOT VALID, maybe delete individuals, and siblings in fam
						for i in range(len(fam[f]["CHIL"])):
							newList = []
							if ind[fam[f]["CHIL"][i]]["BIRT"] != d:
								newList.append(fam[f]["CHIL"][i])
						fam[f]["CHIL"] = newList.copy()

						for c in children:
							if ind[c]["BIRT"] == d:
								ind.pop(c, None)

						newList = []
						family = str(f)
						
						file.write("ERROR: US14 - Sorry this amount of children born on the same day in "+family+" fam is not valid\n")

#Get Age
def getAge(born):
	born = datetime.strptime(born, '%d %b %Y')
	today = datetime.today()
	return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

#Get Age
def getAgeAt(born, given):
	born = datetime.strptime(born, '%d %b %Y')
	given = datetime.strptime(given, '%d %b %Y')
	return given.year - born.year - ((given.month, given.day) < (born.month, born.day))

#US10
def marrAfter14(fam, ind, file):
	result = True
	
	for f in fam:
		if("HUSB" in fam[f]): #check husb age
			husb = fam[f]["HUSB"]
			if(husb in ind and "BIRT" in ind[husb]):
				age = 0
				if("MARR" in fam[f]):
					age = getAgeAt(ind[husb]["BIRT"], fam[f]["MARR"])
				if(age <=14):
					file.write("ERROR: US10 - The individual "+husb+" was married before 14, this is invalid\n")
					result = False
		if("WIFE" in fam[f]): #check wife age
			wife = fam[f]["WIFE"]
			if(wife in ind and "BIRT" in ind[wife]):
				age = 0
				if("MARR" in fam[f]):
					age = getAge(ind[wife]["BIRT"])
				if(age <=14):
					file.write("ERROR: US10 - The individual "+wife+" was married before 14, this is invalid\n")
					result = False			
	return result

#US34
def logLargeAgeDif(fam, ind, file):
	result = True
	for f in fam:
		husAge = 0
		wifeAge = 0
		if("HUSB" in fam[f]):
			husb = fam[f]["HUSB"]
			if husb in ind and "BIRT" in ind[husb]:
				husAge = getAge(ind[husb]["BIRT"])
		if("WIFE" in fam[f]):
			wife = fam[f]["WIFE"]
			if wife in ind and "BIRT" in ind[wife]:
				wifeAge = getAge(ind[wife]["BIRT"])
		if abs(husAge-wifeAge) > wifeAge or abs(husAge-wifeAge) > husAge:
			file.write("ERROR US34: The couple "+husb+" and "+wife+" have a large age difference\n")
			result = False
	return result

#US28
def orderChildrenByAge(fam, ind, file):
	result = False
	for f in fam:
		famTable = PrettyTable(["Child", "Age"])
		child_tuple = ()
		if "CHIL" in fam[f]:
			for c in fam[f]["CHIL"]:
				if("BIRT" in ind[c]):
					age = getAge(ind[c]["BIRT"])
				else:
					age = 0
				child_tuple = child_tuple + ((c, age),)
			child_tuple = sorted(child_tuple, key=lambda child: child[1])
			result = True
			file.write("Here is a list of the children and their ages in family "+f+": "+str(child_tuple)+"\n")
	return result

#US29
def listDeceased(ind, file):
	count = 0
	listDeceased = list()
	for i in ind:
		if "DEAT" in ind[i]:
			listDeceased.append(i)
			count = count +1
	file.write("This is a list of deceased people: "+str(listDeceased)+"\n")
	return count

#US12
def parentsNotTooOld(fam, ind, file):
	result = True
	for f in fam:
		if "CHIL" in fam[f]:
			wife = "0"
			husb = "0"
			if "HUSB" in fam[f]:
				husb = fam[f]["HUSB"]
			if "WIFE" in fam[f]:
				wife = fam[f]["WIFE"]
			wifeAge = 0
			husbAge = 0
			if wife in ind and "BIRT" in ind[wife]:
				wifeAge = getAge(ind[wife]["BIRT"])
			if husb in ind and "BIRT" in ind[husb]:
				husbAge = getAge(ind[husb]["BIRT"])
			for c in fam[f]["CHIL"]:
				childAge = 0
				if "BIRT" in ind[c]:
					childAge = getAge(ind[c]["BIRT"])
				if wifeAge - childAge > 60: #throw wife error
					file.write("ERROR US12: Mother " +wife+ " is older than their child, "+c+" by over 60 years\n")
					result = False
				if husbAge - childAge >80: #throw husb error
					file.write("ERROR US12: Father " +husb+ " is older than their child, "+c+" by over 80 years\n")
					result = False
	return result

#US03
def birthBeforeDeath(ind, file):
	result = True
	for i in ind:
		if "BIRT" in ind[i] and "DEAT" in ind[i]:
			birthday = datetime.strptime(ind[i]["BIRT"], '%d %b %Y')
			deathday = datetime.strptime(ind[i]["DEAT"], '%d %b %Y')
			if birthday > deathday:
				file.write("ERROR US03: Birth of "+i+" comes before their death\n")
				result = False
	return result


#NOTE Tests for these user stories are now in /test under mmstoriesTest