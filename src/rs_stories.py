import unittest

# rachel stern's user stories

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

# code for us02
def us02(id, name, birthdate, mardate, gen):
  if (form_d(birthdate, mardate) == 2) and gen == "her":
    error_wifeus02 = "Error US02: Marriage of " + name + " (" + id + ") occurs before her birthday.\n"
    print(error_wifeus02, end="")
  if (form_d(birthdate, mardate) == 2 and gen == "his"):
    error_husbus02 = "Error US02: Marriage of " + name + " (" + id + ") occurs before his birthday.\n"
    print(error_husbus02, end="")

# code for us04
def us04(marrdate, divdate, hubname, wifename):
  if (form_d(marrdate, divdate) == 2):
      error_us04 = "Error US04: Divorce of " + hubname + " and " + wifename + " happens before their marriage date."
      print(error_us04)

# test for us02
class MyTest(unittest.TestCase):
  def test(self):
    #these three test the date function
    self.assertEqual(form_d("15 JUL 1960", "16 JUL 1960"), 2)
    self.assertEqual(form_d("15 JUN 1960", "15 JUL 1960"), 1)
    self.assertEqual(form_d("12 DEC 1880", "12 DEC 1881"), 1)
    #these test us02
    self.assertEqual(error_husbus02, us02("I07", "Joe /Smith/", "19 JUL 1990", "20 JUN 1880", "his"))
    self.assertEqual(error_wifeus02, us02("I08", "Jane /Doe", "20 JUN 1923", "12 FEB 2000", "her"))
    #these test us04

if __name__ == '__main__':
  unittest.main()

ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
    'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
    'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
    'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
    'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F16'},
    'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'},
    'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'}}


fam = {'F23': 
    {'fam': 'F23', 'MARR': '14 FEB 1880', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
     'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','HUSB': 'I32', 'WIFE': 'I30'}}
