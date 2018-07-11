import unittest

def logAliveMarried(fam, ind):
    result = True
    for f in fam:
        if 'MARR' in fam[f]:
            hus_id = fam[f]['HUSB']
            wife_id = fam[f]['WIFE']
        for i in ind:
            if i == hus_id:
                if 'DEAT' not in ind[hus_id]:
                    print('{} is alive and married!'.format(hus_id))
            elif i == wife_id:
                if 'DEAT' not in ind[wife_id]:
                    print('{} is alive and married!'.format(wife_id))
            else: 
            	result = False
        break

fam = {'F23': #one dead hus one alive wife 
	{'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
	 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

fam2 = {'F23': #both living and married spouses
	{'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
	 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}


fam3 = {'F23': #not married
	{'fam': 'F23', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
	 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind3 = {'I01': {'id': 'I01', 'name': 'Joe /Brown/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

class MyTest(unittest.TestCase):
  def test(self):
      f=open("../test/ruthyOutput.txt","a+")
      self.assertTrue(logAliveMarried(fam, ind, f))
      self.assertTrue(logAliveMarried(fam2, ind2, f))
      self.assertFalse(logAliveMarried(fam3, ind3, f))

      f.close()


def main():
  safe_open("acceptanceTestOutput.txt", 'a+')

if __name__ == "__main__":
    unittest.main()
