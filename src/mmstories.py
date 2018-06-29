import unittest
from datetime import datetime

#takes date in form DD Mon YYYY
#US01
def checkIfDateBeforeNow(date):
	try:
		datetime_object = datetime.strptime(date, '%d %b %Y')
		currDate = datetime.today()
		if datetime_object <= currDate:
			return True
		else:
			f=open("../test/acceptanceTestOutput.txt","a+")
			f.write("ERROR: US01 The date "+ date+ " is after the current date\n")
			f.close()
			return False
	except:
		return False

#US14
def checkLessThan5SharedSiblingBdays(fam, ind):
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
					
						# print(fam)
						# print(ind)
						family = str(f)
						
						f=open("../test/acceptanceTestOutput.txt","a+")
						f.write("ERROR: US14 - Sorry this amount of children born on the same day in "+family+" fam is not valid\n")
						f.close()

#US04
def marrBeforeDivorce(fam):
	for f in fam:
		if("MARR" in fam[f]):
			mdate = datetime.strptime(fam[f]["MARR"], '%d %b %Y')
		else:
			mdate = "null"
		if("DIV" in fam[f]):
			ddate = datetime.strptime(fam[f]["DIV"], '%d %b %Y')
		else:
			ddate = "null"
		if mdate != "null" and ddate!= "null":
			if mdate > ddate: # divorce came before marrige
				family = str(f)
				f=open("../test/acceptanceTestOutput.txt","a+")
				f.write("ERROR: US04 - in fam "+family+" the divorce is before the marriage\n")
				f.close()
				return False
			else:
				return True
	

ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
		'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
		'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F16'},
		'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'},
		'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'}}


fam = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
		 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','HUSB': 'I32', 'WIFE': 'I30'},
		 'F12': {'fam': 'F12', 'MARR': '12 DEC 2008','DIV':'12 DEC 2001','HUSB': 'I32', 'WIFE': 'I30'}}

fam2 = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
		 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','HUSB': 'I32', 'WIFE': 'I30'},
		 'F12': {'fam': 'F12', 'MARR': '12 DEC 2008','DIV':'12 DEC 2019','HUSB': 'I32', 'WIFE': 'I30'}}




class MyTest(unittest.TestCase):
	def test(self):
		#US01
		self.assertTrue(checkIfDateBeforeNow("23 SEP 1960"))
		self.assertEqual(checkIfDateBeforeNow("17 JUN 2029"), False)
		self.assertTrue(checkIfDateBeforeNow(datetime.today().strftime('%d %b %Y')))
		self.assertEqual(checkIfDateBeforeNow("123 JUN 2020"), False)
		self.assertEqual(checkIfDateBeforeNow("31 FEB 2011"), False)

		#US14
		checkLessThan5SharedSiblingBdays(fam, ind)
		self.assertFalse("I19" in ind)
		self.assertFalse("I32" in ind)
		self.assertFalse("I43" in ind)
		self.assertTrue("I01" in ind)
		self.assertTrue(len(fam["F23"]["CHIL"])==0)

		#US04
		self.assertFalse(marrBeforeDivorce(fam))
		self.assertTrue(marrBeforeDivorce(fam2))
		


		
if __name__ == '__main__':
    unittest.main()

