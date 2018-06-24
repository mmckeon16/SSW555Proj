import unittest
import rs_stories
from datetime import datetime

def birthbeforemarri(childsname, childsid, childsbirthday, marrdate, divdate, divBool):
	#print(childsname + " / " + childsbirthday + " / " + marrdate + " / " + divdate)
	#print(rs_stories.form_d(childsbirthday, divdate))
	#print
	if ((rs_stories.form_d(childsbirthday, divdate) == 2) and (divBool == True)):
		#print(childsbirthday)
		#print(marriagedate)
		date_birth = datetime.strptime(childsbirthday, '%d %b %Y')
		date_div = datetime_object = datetime.strptime(divdate, '%d %b %Y')
		dif_time = ((date_birth-date_div).days/365.25) * 12
		if (dif_time > 9):
			print("Error US08: Birthdate of child " + childsname + " (" + childsid + ") is >9 months after their parents' divorce.")
	#print(rs_stories.form_d(childsbirthday, marriagedate)) == 1 every time
	#print(childsbirthday + " // " + marriagedate)
	elif (rs_stories.form_d(marrdate, childsbirthday) == 2):
		print("Error US08: Birthdate of child " + childsname + " (" + childsid + ") is before their parents' marriage.")
