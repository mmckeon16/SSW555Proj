"""
US 33: List all orphaned children (both parents dead and child < 18 years old) in a GEDCOM file
"""

import unittest
from datetime import datetime

today = datetime.today()

def logOrphans(fam, ind, file):
  result = True
  for f in fam:
      if 'HUSB' in fam[f]:
          hus_id = fam[f]['HUSB']
          if 'WIFE' in fam[f]:
              wife_id = fam[f]['WIFE']
      if "CHIL" in fam[f]:
          for c in fam[f]["CHIL"]:
              c_born = ind[c]["BIRT"]
              age = getAge(c_born) # I looked at the logic and it looked right, but it seemed easier to just add in my function
              if age < 18: #i put this inside of the for f in fam since this needs to be done for every family and every child
                if "DEAT" in ind[hus_id] and "DEAT" in ind[wife_id]:
                  file.write("US 33 : The chil of "+hus_id+" and "+wife_id+" are dead, making "+c+" an orphan because they are younger than 18\n")
                  result = False
  return result #I added this return for testing, now the result is false if there are orphans which will help with testing
#Get Age
def getAge(born):
  born = datetime.strptime(born, '%d %b %Y')
  today = datetime.today()
  return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

fam = {'F23': #all orphans
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 2005', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 2005', 'sex': 'F', 'family': 'F23','DEAT': '31 DEC 2013'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 2006', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 2007', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 2008', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 2009', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 2004', 'sex': 'F', 'family': 'F23'}}

fam2 = {'F23': #no orphans
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

fam3 = {'F23': #no wife
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind3 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

class MyTest(unittest.TestCase):
  def test(self):
      f=open("../test/ruthyOutput.txt","a+")
      self.assertTrue(logOrphans(fam, ind, f))
      self.assertTrue(logOrphans(fam2, ind2, f))
      self.assertFalse(logOrphans(fam3, ind3, f))
      f.close()

if __name__ == "__main__":
    unittest.main()
