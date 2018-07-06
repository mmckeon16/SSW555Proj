import unittest
from datetime import datetime

def birthbeforedeath(childsname, childsID, childsbirthday, parentsdeathdate, deathBool):
	
	if ((datetime.strptime(childsbirthday, '%d %b %Y')) > (datetime.strptime(parentsdeathdate, '%d %b %Y')) and (deathBool == False)):
		date_birth = datetime.strptime(childsbirthday, '%d %b %Y')
		parentsdeath = datetime_object = datetime.strptime(parentsdeathdate, '%d %b %Y')
		dif_time = ((childsbirthday-parentsdeathdate).days/365.25) * 12
		if (dif_time > 9):
			error_us09 = "Error US09: Birthdate of child " + childsname + " (" + childID + ") is >9 months after father's death .\n"
			f=open("../test/acceptanceTestOutput.txt","a+")
			f.write(error_us09)
			f.close()
			return error_us09
	
	elif ((datetime.strptime(childsbirthday, '%d %b %Y')) > (datetime.strptime(parentsdeathdate, '%d %b %Y'))):
		error_us09 = "Error US09: Birthdate of child " + childsname + " (" + childsID + ") is after mother's death.\n"
		f=open("../test/acceptanceTestOutput.txt","a+")
		f.write(error_us09)
		f.close()
		return error_us09

class MyTest(unittest.TestCase):
  def test(self):
    #these test us09
    self.assertEqual(birthbeforedeath("Ralph /Doe/", "I01", "20 JUN 1993", "20 JUL 1985", True), "Error US09: Birthdate of child Ralph /Doe/ (I01) is after mother's death.\n")
    self.assertEqual(birthbeforedeath("Ralph /Doe/", "I01", "20 JUN 1993", "20 JUL 2030", False), None)

if __name__ == '__main__': unittest.main()
