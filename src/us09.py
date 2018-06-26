import unittest
import rs_stories
from datetime import datetime

def birthbeforedeath(childsname, childID, childsbirthday, parentsdeath, deathBool):
	
	if ((rs_stories.form_d(childsbirthday, parentsdeath) == 2) and (deathBool == False)):
		date_birth = datetime.strptime(childsbirthday, '%d %b %Y')
		parentsdeath = datetime_object = datetime.strptime(parentsdeath, '%d %b %Y')
		dif_time = ((childsbirthday-parentsdeath).days/365.25) * 12
		if (dif_time > 9):
			print("Error US09: Birthdate of child " + childsname + " (" + childID + ") is >9 months after father's death .")
	
	elif (rs_stories.form_d(childsbirthday, parentsdeath) == 2):
		print("Error US09: Birthdate of child " + childsname + " (" + childID + ") is after mother's death.")
