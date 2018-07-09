import unittest 

""" open the file and return the file pointer or raise an IOERROR exception """
def safe_open(file,mode):
    try:
        return open(file, mode)
    except IOError:
        raise IOError("Can't open '{}' for '{}'".format(file, mode))


""" No more than one individual with the same name and birth date should appear in a GEDCOM file """
def checkIndividual(fam,ind, file):
    husName = ''
    wifeName = ''

    for f in fam:
        if "HUSB" in fam[f]:
            hus = fam[f]["HUSB"] #get ID
            husName = ind[hus]["name"] #get name
            husBDate = ind[hus]["BIRT"] #get bday

            if "WIFE" in fam[f]:
                wife = fam[f]["WIFE"] 
                wifeName = ind[wife]["name"]
                wifeBDate = ind[wife]["BIRT"]

        if "CHIL" in fam[f]:
            for c in fam[f]["CHIL"]:
                chilName = ind[c]["name"]
                chilBDate = ind[c]["BIRT"]
                for i in ind:
                    if husName == chilName or husName == wifeName or chilName == wifeName: #if any of the names match
                        if "HUSB" in fam[f]:
                            if husBDate == wifeBDate:
                                file.write("ERROR US23: There is a shared Name and Birthdate in family "+f+"\n")
                                popped(hus)
                            if husBDate == chilBDate:
                                file.write("ERROR US23: There is a shared Name and Birthdate in family "+f+"\n")
                                popped(hus)
                            if chilBDate == wifeBDate:
                                file.write("ERROR US23: There is a shared Name and Birthdate in family "+f+"\n")
                                popped(wife)
                    else:
                        continue

def popped(any_list):
    fam.pop(any_list, None)
    ind.pop(any_list, None)
    #break
   
fam = {'F23': 
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
ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Joe /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

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
      f= open("../test/ruthyOutput.txt","a+")
      checkIndividual(fam, ind, f)
      self.assertTrue(('I01' in ind))
      self.assertTrue(('I01' == fam['F23']['HUSB']))
      checkIndividual(fam2, ind2, f)
      self.assertTrue(('I01' in ind2))
      self.assertTrue(('I01' in fam2['F23']['HUSB']))
      checkIndividual(fam3, ind3, f)
      self.assertFalse(('I01' in ind3))
      self.assertFalse(('HUSB' in fam3['F23']))
      f.close()

def main():
  safe_open("acceptanceTestOutput.txt", 'a+')

if __name__ == "__main__":
    unittest.main()
