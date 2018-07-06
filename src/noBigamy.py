import unittest 


def safe_open(file,mode):
    try:
        return open(file, mode)
    except IOError:
        raise IOError("Can't open '{}' for '{}'".format(file, mode))


"""Marriage should not occur during marriage to another spouse"""
def checkBigamy(fam,ind):
    #if the value of husb or the value of husb in one family is equal to the value of husb or the value of wife of another fam
    for f in fam:
        hus_id = fam[f]['HUSB']
        wife_id = fam[f]['WIFE']

    for f in fam2:
        hus_id2 = fam2[f]['HUSB']
        wife_id2 = fam2[f]['WIFE']

    if hus_id2 == hus_id or if wife_id == wife_id2:
        print("US11 ERROR: Marriage should not occur during marriage to another spouse")


fam = {'F23': 
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
fam2 = {'F24': 
  {'fam': 'F24', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I10', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F24'}}
ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F24', 'DEAT': '31 DEC 2013'},
 'I10': {'id': 'I10', 'name': 'Julie /Brown/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F24'},
 'I19': {'id': 'I19', 'name': 'Whitney /Brown/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F24'},
  'I26': {'id': 'I26', 'name': 'Laura /Brown/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F24'},
  'I30': {'id': 'I30', 'name': 'Julia /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F24'},
  'I32': {'id': 'I32', 'name': 'Eliza /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F24'},
  'I44': {'id': 'I44', 'name': 'Alex /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F24'}}

fam3 = {'F23': #dad and son have same name and bday
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind3 = {'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}


class MyTest(unittest.TestCase):
  def test(self):
      checkIndividual(fam, ind)
      self.assertTrue(('I01' in ind))
      self.assertTrue(('I01' == fam['F23']['HUSB']))
      checkIndividual(fam2, ind2)
      self.assertTrue(('I01' in ind2))
      self.assertTrue(('I01' in fam2['F23']['HUSB']))
      checkIndividual(fam3, ind3)
      self.assertFalse(('I01' in ind3))
      self.assertFalse(('HUSB' in fam3['F23']))

def main():
  safe_open("acceptanceTestOutput.txt", 'a+')

if __name__ == "__main__":
    unittest.main()