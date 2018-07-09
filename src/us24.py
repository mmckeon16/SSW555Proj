import unittest

def unique_families_by_spouses(ind, fam, file):
    """ US24 - No more than one individual with the same name and birth
        date should appear in a GEDCOM file - ANOMALY """
    anom_type = "US24"
    return_flag = True

    for f in fam:

        count = 0
        if "HUSB" in fam[f]:
          husb1 = fam[f]["HUSB"]
        else:
          husb1 = "h1"
        if "WIFE" in fam[f]:
          wife1 = fam[f]["WIFE"]
        else:
          wife1 = "w1"
        for f2 in fam:
            if "HUSB" in fam[f2]:
              husb2 = fam[f2]["HUSB"]
            else:
              husb2 = "h2"
            if "WIFE" in fam[f2]:
              wife2 = fam[f2]["WIFE"]
            else:
              wife2 = "w2"
            if husb2 == husb1 and wife2 == wife1 and "MARR" in fam[f2] and "MARR" in fam[f] and fam[f2]["MARR"] == fam[f]["MARR"]:
                count = count +1
                if count > 1:
                    file.write("ERROR US24: Two families share the same wife of "+wife1+" and the same husband of "+husb1+" and marriage date of "+fam[f2]["MARR"]+"\n")
                    return False
    return return_flag

fam = {'F23': 
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']}}
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}
fam2 = {'F23': 
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}


class MyTest(unittest.TestCase):
  def test(self):
      f= open("../test/jeneleeOutput.txt","a+")
      self.assertFalse(unique_families_by_spouses( ind,fam, f))
     # self.assertTrue(unique_families_by_spouses( ind,fam2, f))
      f.close()

if __name__ == "__main__":
    unittest.main()