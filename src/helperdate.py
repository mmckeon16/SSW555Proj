# formats dates and compares them; returns 1 if the first date is earlier and 2 otherwise -RS
def form_d (date1, date2):
  year1 = date1[-4:]
  mon1 = date1[-8:-5]
  year2 = date2[-4:]
  mon2 = date2[-8:-5]
  if date1[1] == " ":
    dayn1 = date1[0]
  else:
	  dayn1 = date1[0:1]

  if date2[1] == " ":
	  dayn2 = date2[0]
  else:
	  dayn2 = date2[0:1]

  if mon1 == "JAN":
	  mon1 = 1
  elif mon1 == "FEB":
	  mon1 = 2
  elif mon1 == "MAR":
	  mon1 = 3
  elif mon1 == "APR":
	  mon1 = 4
  elif mon1 == "MAY":
    mon1 = 5
  elif mon1 == "JUN":
	  mon1 = 6
  elif mon1 == "JUL":
	  mon1 = 7
  elif mon1 == "AUG":
	  mon1 = 8
  elif mon1 == "SEP":
	  mon1 = 9
  elif mon1 == "OCT":
	  mon1 = 10
  elif mon1 == "NOV":
	  mon1 = 11
  else:
	  mon1 = 12

  if mon2 == "JAN":
	  mon2 = 1
  elif mon2 == "FEB":
	  mon2 = 2
  elif mon2 == "MAR":
	  mon2 = 3
  elif mon2 == "APR":
	  mon2 = 4
  elif mon2 == "MAY":
	  mon2 = 5
  elif mon2 == "JUN":
	  mon2 = 6
  elif mon2 == "JUL":
	  mon2 = 7
  elif mon2 == "AUG":
	  mon2 = 8
  elif mon2 == "SEP":
	  mon2 = 9
  elif mon2 == "OCT":
	  mon2 = 10
  elif mon2 == "NOV":
	  mon2 = 11
  else:
	  mon2 = 12

  if (year1 < year2):
    return 1
  elif ((year1 == year2) and (mon1 < mon2)):
    return 1
  elif (year1 == year2 and mon1 == mon2 and dayn1 < dayn2):
    return 1
  else:
    return 2