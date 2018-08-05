'''
US13: Birth dates of siblings should be more than 8 months apart or less than 2 days apart
(twins may be born one day apart, e.g. 11:59 PM and 12:02 AM the following calendar day)
'''

#get the siblings
#get their birthdates 
#make sure months are more than 8  months apart OR less than 2 days apart (twinz)

import unittest
from datetime import datetime
from dateutil import relativedelta

chil_list = []
month_values = {"JAN":1, "FEB":2, "MAR":3, "APR":4, "MAY":5, "JUN":6, "JUL":7, "AUG":8, "SEP":9, "OCT":10, "NOV":11, "DEC":12}

def safe_open(file,mode):
    try:
        return open(file, mode)
    except IOError:
        raise IOError("Can't open '{}' for '{}'".format(file, mode))
        
def siblingSpacing(fam, ind, file): 
    result = True 
    for f in fam:
        if "CHIL" in fam[f]: #if person is a child
            for c in fam[f]["CHIL"]:
                chil = ind[c]["id"]
                chil_list.append(chil) #child's siblings --> 'I19, I26, 130'
            for i in range(len(chil_list)): #(0,3) aka 0,2
                i_date_strip = i_date.strip().split()
                i_month = month_values[i_date_strip[1]]
                i_day = int(i_date_strip[0])
                for j in range(i + 1, len(chil_list)): #(1,3) aka (1,2)
                    j_date = ind[chil_list[j]]["BIRT"] #13 feb 1982, 13 feb 1987 
                    j_date_strip = j_date.strip().split()
                    j_month = month_values[j_date_strip[1]]
                    j_day = int(j_date_strip[0])
                    if not (i_month - j_month > 8) or not (j_month - i_month > 8):
                        print("ERROR US13: Birth dates of siblings should be more than 8 months apart\n")                    
                    elif i_month != j_month:
                        if not (i_day - j_day < 2) or not (j_day - i_day < 2):
                            print("ERROR US13: Birth dates of siblings should be less than 2 days apart\n")                    
                    else:
                        return False
def getMonth(born):
  born = datetime.strptime(born, '%d %b %Y')
  return born.month

def getDay(born):
  born = datetime.strptime(born, '%d %b %Y')
  return born.day

fam = {'F23': #birth date of Dick Smith and Jane Smith more than 8 months apart 
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1982', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1987', 'sex': 'F', 'family': 'F23'},
}

fam2 = {'F23': #birth date of Dick Smith and Jane Smith less than 2 days apart
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1987', 'sex': 'F', 'family': 'F23'},
  }

fam3 = {'F23': #birth date of Dick Smith and Jane Smith less than 8 months apart
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind3 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 APR 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1987', 'sex': 'F', 'family': 'F23'},
  }

class MyTest(unittest.TestCase):
  def test(self):
      f= open("../test/ruthyOutput.txt","a+")
      self.assertFalse(siblingSpacing(fam, ind, f))
      self.assertFalse(siblingSpacing(fam2, ind2, f))
      self.assertFalse(siblingSpacing(fam3, ind3, f))
      f.close()

def main():
  safe_open("acceptanceTestOutput.txt", 'a+')

if __name__ == "__main__":
    unittest.main()
