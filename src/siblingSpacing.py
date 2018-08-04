'''
US13: Birth dates of siblings should be more than 8 months apart or less than 2 days apart
(twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)

'''

#get the siblings
#get their birthdates 
#make sure months are more than 8  months apart OR less than 2 days apart (twinz)

import unittest
from datetime import datetime

chilAndBirth = []

def safe_open(file,mode):
    try:
        return open(file, mode)
    except IOError:
        raise IOError("Can't open '{}' for '{}'".format(file, mode))

def siblingSpacing(fam, ind, file): 
    for f in fam:
        if "CHIL" in fam[f]: #if person is a child
            for c in fam[f]["CHIL"]:
                chil = ind[c]["id"]
                b_date = ind[c]["BIRT"]
                b_month = getMonth(b_date)
                b_day = getDay(b_date)
                chilAndBirth.append(chil, b_month, b_day) #child's siblings 
            for i in range(len(chilAndBirth)):
                for j in range(i + 1, len(chilAndBirth)):
                    if not (chilAndBirth[i][b_month] - chilAndBirth[j][b_month] > 8) or not (chilAndBirth[j][b_month] - chilAndBirth[i][b_month] > 8):
                        file.write("ERROR US13: Birth dates of siblings should be more than 8 months apart\n")                    
                    if chilAndBirth[i][b_month] != chilAndBirth[j][b_month]:
                        if not (chilAndBirth[i][b_day] - chilAndBirth[j][b_day] < 2) or not (chilAndBirth[j][b_day] - chilAndBirth[i][b_day] < 2):
                            file.write("ERROR US13: Birth dates of siblings should be less than 2 days apart\n")                    

def getMonth(born):
  born = datetime.strptime(born, '%d %b %Y')
  return born.month

def getDay(born):
  born = datetime.strptime(born, '%d %b %Y')
  return born.day


fam = {'F23': 
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': '16'}}


class MyTest(unittest.TestCase):
  def test(self):
      f= open("../test/ruthyOutput.txt","a+")
      siblingSpacing(fam, ind, f)
      self.assertTrue(('I01' in ind))
      self.assertTrue(('I01' == fam['F23']['HUSB']))
      siblingSpacing(fam2, ind2, f)
      self.assertFalse(('I19' in ind2))
      self.assertFalse(('I19' in fam2['F23']['WIFE']))
      siblingSpacing(fam3, ind3, f)
      self.assertFalse(('I30' in ind3))
      self.assertFalse(('WIFE' in fam3['F23']))
      f.close()

def main():
  safe_open("acceptanceTestOutput.txt", 'a+')

if __name__ == "__main__":
    unittest.main()
