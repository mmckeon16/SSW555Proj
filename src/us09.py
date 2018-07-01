import unittest
from datetime import datetime

def birthbeforedeath(childsname, childsID, childsbirthday, parentsdeathdate, deathBool):
	
	if ((datetime.strptime(childsbirthday, '%d %b %Y')) > (datetime.strptime(parentsdeathdate, '%d %b %Y')) and (deathBool == False)):
		date_birth = datetime.strptime(childsbirthday, '%d %b %Y')
		parentsdeath = datetime_object = datetime.strptime(parentsdeathdate, '%d %b %Y')
		dif_time = ((childsbirthday-parentsdeathdate).days/365.25) * 12
		if (dif_time > 9):
			f=open("../test/acceptanceTestOutput.txt","a+")
			f.write("Error US09: Birthdate of child " + childsname + " (" + childsID + ") is >9 months after father's death .\n")
			f.close()
	
	elif ((datetime.strptime(childsbirthday, '%d %b %Y')) > (datetime.strptime(parentsdeathdate, '%d %b %Y'))):
		f=open("../test/acceptanceTestOutput.txt","a+")
		f.write("Error US09: Birthdate of child " + childsname + " (" + childsID + ") is after mother's death.\n")
		f.close()
