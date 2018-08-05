import unittest 

descendants = [] 

def safe_open(file,mode):
    try:
        return open(file, mode)
    except IOError:
        raise IOError("Can't open '{}' for '{}'".format(file, mode))

"""Parents should not marry any of their descendants"""
def checkMarr(fam,ind, file):
    for f in fam:
        if 'WIFE' in fam[f]: 
            wife = fam[f]["WIFE"] 

            if 'HUSB' in fam[f]:
                hus = fam[f]["HUSB"] #get ID

        if "CHIL" in fam[f]:
            for c in fam[f]["CHIL"]:
                chil = ind[c]["id"]
                break

        for i in ind: #for all individuals
            if ind[i] != ind[wife] and ind[i] != ind[hus]: #if individual is a parent, they aren't a descendant 
                descendants.append(i)

        for desc in descendants: #if desc is a wife or husband, that means they married a descendant
            if desc == wife:
                file.write("ERROR US17: For family "+f+", "+desc+" is married to "+wife+". Parents should not marry any of their descendants\n")
                break
            if chil == wife:
                file.write("ERROR US17: For family "+f+", "+chil+" is married to "+wife+". Parents should not marry any of their descendants\n")
                break
            if desc == hus: 
                file.write("ERROR US17: For family "+f+", "+(desc)+" is married to "+hus+". Parents should not marry any of their descendants\n")
                break
            if chil == hus: 
                file.write("ERROR US17: For family "+f+", "+chil+" is married to "+hus+". Parents should not marry any of their descendants\n")
                break

def popped(any_list, file):
    file.write("ERROR US17: Parents should not marry any of their descendants\n")
    # fam.pop(any_list, None)
    # ind.pop(any_list, None)
   
   
fam = {'F23': #no errors
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

fam2 = {'F23': #child is husband
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I19', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind2 = {
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Joe /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

fam3 = {'F23': #descendant is wife
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I30', 'CHIL': ['I19', 'I26', 'I30']},
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
      f= open("../test/ruthyOutput.txt","a+")
      checkMarr(fam, ind, f)
      self.assertTrue(('I01' in ind))
      self.assertTrue(('I01' == fam['F23']['HUSB']))
      checkMarr(fam2, ind2, f)
      self.assertFalse(('I19' in ind2))
      self.assertFalse(('I19' in fam2['F23']['WIFE']))
      checkMarr(fam3, ind3, f)
      self.assertFalse(('I30' in ind3))
      self.assertFalse(('WIFE' in fam3['F23']))
      f.close()

def main():
  safe_open("acceptanceTestOutput.txt", 'a+')

if __name__ == "__main__":
    unittest.main()
