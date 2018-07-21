import unittest
from datetime import datetime

def birthbeforemarri(childsname, childsid, childsbirthday, marrdate, divdate, divBool):
	error_div = False
	error_bir = False
	if ((datetime.strptime(marrdate, '%d %b %Y')) < (datetime.strptime(childsbirthday, '%d %b %Y')) and (divBool == True)):
		date_birth = datetime.strptime(childsbirthday, '%d %b %Y')
		date_div = datetime_object = datetime.strptime(divdate, '%d %b %Y')
		dif_time = ((date_birth-date_div).days/365.25) * 12
		if (dif_time > 9):
			f=open("../test/acceptanceTestOutput.txt","a+")
			f.write("Error US08: Birthdate of child " + childsname + " (" + childsid + ") is >9 months after their parents' divorce.\n")
			f.close()
			error_div = True
	elif ((datetime.strptime(marrdate, '%d %b %Y')) > (datetime.strptime(childsbirthday, '%d %b %Y'))):
		f=open("../test/acceptanceTestOutput.txt","a+")
		f.write("Error US08: Birthdate of child " + childsname + " (" + childsid + ") is before their parents' marriage.\n")
		f.close()
		error_bir = True

class MyTest(unittest.TestCase):
 def test(self):
   childsname = "idk"
   childsid = "I30"
   childsbirthday = "15 JUN 1980"
   marrdate = "15 JUL 1980"
   divdate = "----"
   divBool = False
   birthbeforemarri(childsname, childsid, childsbirthday, marrdate, divdate, divBool)
   self.assertEqual(error_bir, True)
   self.assertEqual(error_div, False)
   childsbirthday = "15 JUN 1985"
   birthbeforemarri(childsname, childsid, childsbirthday, marrdate, divdate, divBool)
   self.assertEqual(error_bir, False)
  divdate = "14 JUN 1983"
   childsbirthday = "15 JUN 1985"
  birthbeforemarri(childsname, childsid, childsbirthday, marrdate, divdate, divBool)
   self.assertEqual(error_div, True)
   birthbeforemarri(childsname, childsid, childsbirthday, marrdate, divdate, divBool)
   self.assertEqual(error_bir, False)

if __name__ == '__main__':
 unittest.main()
