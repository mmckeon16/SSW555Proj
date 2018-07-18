import unittest
from datetime import datetime

# rachel stern's user stories

# code for us02
def us02(id, name, birthdate, mardate, gen):
  if ((datetime.strptime(birthdate, '%d %b %Y')) > (datetime.strptime(mardate, '%d %b %Y')) and gen == "her"):
    error_wifeus02 = "Error US02: Marriage of " + name + " (" + id + ") occurs before her birthday.\n"
    f=open("../test/acceptanceTestOutput.txt","a+")
    f.write(error_wifeus02)
    f.close();
    return error_wifeus02
  if ((datetime.strptime(birthdate, '%d %b %Y')) > (datetime.strptime(mardate, '%d %b %Y')) and gen == "his"):
    error_husbus02 = "Error US02: Marriage of " + name + " (" + id + ") occurs before his birthday.\n"
    f=open("../test/acceptanceTestOutput.txt","a+")
    f.write(error_husbus02)
    f.close()
    return error_husbus02

# code for us04
def us04(marrdate, divdate, hubname, wifename):
  if ((datetime.strptime(marrdate, '%d %b %Y')) > (datetime.strptime(divdate, '%d %b %Y'))):
      error_us04 = "Error US04: Divorce of " + hubname + " and " + wifename + " happens before their marriage date.\n"
      f=open("../test/acceptanceTestOutput.txt","a+")
      f.write(error_us04)
      f.close()
      return error_us04

# code for us06
def us06(wifeName, hubName, deathdate, divdate):
  error_us06 = "-"
  if ((datetime.strptime(deathdate, '%d %b %Y')) < (datetime.strptime(divdate, '%d %b %Y'))):
    error_us06 = "Error US06: Divorce of " + wifeName + " and " + hubName + " occurs after one or both of them have died.\n"
  elif ((datetime.strptime(deathdate, '%d %b %Y')) < (datetime.strptime(divdate, '%d %b %Y'))):
    error_us06 = "Error US06: Divorce of " + wifeName + " and " + hubName + " occurs after one or both of them have died.\n"
  
  if error_us06 != "-":
    f=open("../test/acceptanceTestOutput.txt","a+")
    f.write(error_us06)
    f.close()
    return error_us06

# code for us18
def us18(wifeName, wifeID, hubName, hubID, fam_dict):
  for key in fam_dict:
    if 'CHIL' in fam_dict[key]:
        if (wifeID in fam_dict[key]['CHIL'] and hubID in fam_dict[key]['CHIL']):
          error_us18 = "Error US18: Siblings " + wifeName + " and " + hubName + " cannot be married.\n" 
          f=open("../test/acceptanceTestOutput.txt","a+")
          f.write(error_us18)
          f.close()
          return error_us18

# code for us15
def us15(fam):
  for key in fam:
    if 'CHIL' in fam[key]:
      if (len(fam[key]['CHIL']) > 14):
        error_us15 = "Error US15: There are more than 15 siblings for family " + key + ".\n"
        f=open("../test/acceptanceTestOutput.txt","a+")
        f.write(error_us15)
        f.close()
        return error_us15

# code for us27
def us27(birthday):
  birthdate = datetime.strptime(birthday, '%d %b %Y')
  current = datetime.today()
  return current.year - birthdate.year - ((current.month, current.day) < (birthdate.month, birthdate.day))

# code for us21: commented out until next sprint; took about 40 min
#def us21(name, gender, role):
#  if (gender == "F" and role != "wife"):
#    error_us21 = "Error US21: Role of " + name + " does not match her gender."
#    f=open("../test/acceptanceTestOutput.txt","a+")
#    f.write(error_us21)
#    f.close()
#    return error_us21
#  if (gender == "M" and role != "husband"):
#    error_us21 = "Error US21: Role of " + name + " does not match his gender."
#    f=open("../test/acceptanceTestOutput.txt","a+")
#    f.write(error_us21)
#    f.close()
#    return error_us21

class MyTest(unittest.TestCase):
  def test(self):
    #these test us02
    us02("I07", "Joe /Smith/", "19 JUL 1990", "20 JUN 1880", "his")
    self.assertEqual(us02("I07", "Joe /Smith/", "19 JUL 1990", "20 JUN 1880", "his"), "Error US02: Marriage of Joe /Smith/ (I07) occurs before his birthday.\n")
    self.assertEqual(us02("I08", "Jane /Doe/", "20 JUN 1923", "12 FEB 2000", "her"), None)
    # these test us04
    self.assertEqual(us04("19 JUL 1990", "18 JUL 1990", "Joe /Smith/", "Jane /Doe/"), "Error US04: Divorce of Joe /Smith/ and Jane /Doe/ happens before their marriage date.\n")
    self.assertEqual(us04("19 JUL 1990", "18 JUL 1995", "Joe /Smith/", "Jane /Doe/"), None)
    # these test us06
    self.assertEqual(us06("Jane /Doe/", "Joe /Smith/", "12 OCT 2015", "21 NOV 2029"), "Error US06: Divorce of Jane /Doe/ and Joe /Smith/ occurs after one or both of them have died.\n")
    self.assertEqual(us06("Jane /Doe/", "Joe /Smith/", "12 OCT 2015", "21 NOV 2009"), None)
    # these test us18
    fam = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']}, 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007', 'HUSB': "I19", 'WIFE': 'I26'}}
    self.assertEqual(us18("Jane /Doe/", "I26", "Josh /Doe/", "I19", fam), "Error US18: Siblings Jane /Doe/ and Josh /Doe/ cannot be married.\n")
    fam2 = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']}, 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
    self.assertEqual(us18("Jane /Doe/", "I07", "Josh /Doe/", "I01", fam2), None)
    # these test us15
    fam3 = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I01', 'I09', 'I22', 'I12', 'I03', 'I05', 'I07', 'I08', 'I11', 'I14', 'I99', 'I98', 'I97']}, 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
    self.assertEqual(us15(fam3), "Error US15: There are more than 15 siblings for family F23.\n")
    self.assertEqual(us15(fam2), None)
    # these test us27
    self.assertEqual(us27("14 MAY 2099"), -81)
    self.assertEqual(us27("25 JUN 2017"), 1)
    self.assertEqual(us27("23 APR 1998"), 20)
    # these test us21
#    self.assertEqual(us21("Joe Smith", "M", "husband"), None)
#    self.assertEqual(us21("Joe Smith", "M", "wife"), "Error US21: Role of Joe Smith does not match his gender.")
#    self.assertEqual(us21("Jane Smith", "F", "husband"), "Error US21: Role of Jane Smith does not match her gender.")
#    self.assertEqual(us21("Jane Smith", "F", "wife"), None)
    
if __name__ == '__main__': unittest.main()
