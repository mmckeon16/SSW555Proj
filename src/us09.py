import unittest
import rs_stories
from datetime import datetime

def birthbeforedeath(childsname, childID, childsbirthday, parentsdeath, deathBool):
	
	if ((datetime.strptime(childsbirthday, '%d %b %Y')) > (datetime.strptime(parentsdeath, '%d %b %Y')) and (deathBool == False)):
		date_birth = datetime.strptime(childsbirthday, '%d %b %Y')
		parentsdeath = datetime_object = datetime.strptime(parentsdeath, '%d %b %Y')
		dif_time = ((childsbirthday-parentsdeath).days/365.25) * 12
		if (dif_time > 9):
			f=open("../test/acceptanceTestOutput.txt","a+")
			f.write("Error US09: Birthdate of child " + childsname + " (" + childID + ") is >9 months after father's death .\n")
			f.close()
	
	elif ((datetime.strptime(childsbirthday, '%d %b %Y')) > (datetime.strptime(parentsdeath, '%d %b %Y'))):
		f=open("../test/acceptanceTestOutput.txt","a+")
		f.write("Error US09: Birthdate of child " + childsname + " (" + childID + ") is after mother's death.\n")
		f.close()
