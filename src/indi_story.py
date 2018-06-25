import unittest

def checkIndividual(fam,ind):

    #No more than one individual with the same name and birth date should appear in a GEDCOM file
    print(fam)
    for f in fam:
        if "HUSB" or "WIFE" in fam[f]:
            hus = fam[f]["HUSB"] #get ID
            husName = ind[hus]["name"] #get name
            husBDate = ind[hus]["BIRT"] #get bday
            wife = fam[f]["WIFE"]
            wifeName = ind[hus]["name"]
            wifeBDate = ind[hus]["BIRT"]
        if "CHIL" in fam[f]:
            for c in fam[f]["CHIL"]:
                chilName = ind[c]["name"]
                chilBDate = ind[c]["BIRT"]
                for i in ind:
                    if husName == chilName or husName == wifeName or chilName == wifeName:
                        if husBDate == wifeBDate:
                          print("Can't have duplicate entries.")
                          ind.pop(fam[f]["HUSB"], None)
                          fam[f].pop("HUSB", None)
                          
                        if husBDate == chilBDate:
                            print("Can't have duplicate entries.")
                            fam[f]["CHIL"].pop(fam[f]["CHIL"].index(c))
                            ind.pop(c, None)
                        if chilBDate == wifeBDate:
                            print("Can't have duplicate entries.")
                            fam[f]["CHIL"].pop(fam[f]["CHIL"].index(c))
                            ind.pop(c, None)
                        else:
                            print("Valid family tree.")

    


fam = {'F23': #normal
	{'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
	 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

fam2 = {'F23': #dad and son have same name
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Joe /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

fam3 = {'F23':
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind3 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}


class MyTest(unittest.TestCase):
  def test(self):
    checkIndividual(fam, ind)
    self.assertTrue(('I01' in ind))
    self.assertTrue(('IO1' in fam['F23']['HUSB']))
    checkIndividual(fam2, ind2)
    self.assertTrue(('I01' in ind))
    self.assertTrue(('IO1' in fam['F23']['HUSB']))
    checkIndividual(fam3, ind3)
    self.assertFalse(('I01' in ind))
    self.assertFalse(('IO1' in fam['F23']['HUSB']))

    
if __name__ == '__main__':
        unittest.main()


