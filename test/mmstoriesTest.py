import unittest
import sys
sys.path.insert(0, '../src')
import mmstories
from datetime import datetime

ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
		'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
		'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F12'},
		'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F12'},
		'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
		'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 1981','sex': 'F', 'family': 'F16'},
		'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'}}

ind2 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 2005', 'sex': 'F', 'family': 'F23'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
		'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
		'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F12'},
		'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F12'},
		'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
		'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 1981','sex': 'F', 'family': 'F16'},
		'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'}}

ind3 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1999','sex': 'M', 'family': 'F23'},
		'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1998', 'sex': 'F', 'family': 'F23'},
		'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 2000', 'sex': 'F', 'family': 'F12'},
		'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 2010','sex': 'M', 'family': 'F12'},
		'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1997','sex': 'M', 'family': 'F23'},
		'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 2005','sex': 'F', 'family': 'F16'},
		'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 2003','sex': 'M', 'family': 'F16'}}

ind4 = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
		'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23', 'DEAT': '31 DEC 2013'},
		'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1999','sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
		'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1998', 'sex': 'F', 'family': 'F23'},
		'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 2000', 'sex': 'F', 'family': 'F12'},
		'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 2010','sex': 'M', 'family': 'F12'},
		'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1997','sex': 'M', 'family': 'F23'},
		'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 2005','sex': 'F', 'family': 'F16'},
		'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 2003','sex': 'M', 'family': 'F16'}}

fam = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
		 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','HUSB': 'I45', 'WIFE': 'I44'},
		 'F12': {'fam': 'F12', 'MARR': '12 DEC 2008','DIV':'12 DEC 2001','HUSB': 'I32', 'WIFE': 'I30'}}

fam2 = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
		 'F16': {'fam': 'F16', 'MARR': '12 DEC 1990','HUSB': 'I45', 'WIFE': 'I44'},
		 'F12': {'fam': 'F12', 'MARR': '12 DEC 2008','DIV':'12 DEC 2019','HUSB': 'I32', 'WIFE': 'I30'}}

fam3 = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
		 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','HUSB': 'I45', 'WIFE': 'I44'},
		 'F12': {'fam': 'F12', 'MARR': '12 DEC 2008','DIV':'12 DEC 2001','HUSB': 'I32', 'WIFE': 'I30'}}

fam4 = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07'},
		 'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','HUSB': 'I45', 'WIFE': 'I44'},
		 'F12': {'fam': 'F12', 'MARR': '12 DEC 2008','DIV':'12 DEC 2001','HUSB': 'I32', 'WIFE': 'I30'}}
class MyTest(unittest.TestCase):
	def test(self):
		#US01
		f= open("../test/mmOutput.txt","a+")
		self.assertTrue(mmstories.checkIfDateBeforeNow("23 SEP 1960", f))
		self.assertEqual(mmstories.checkIfDateBeforeNow("17 JUN 2029", f), False)
		self.assertTrue(mmstories.checkIfDateBeforeNow(datetime.today().strftime('%d %b %Y'), f))
		self.assertEqual(mmstories.checkIfDateBeforeNow("123 JUN 2020", f), False)
		self.assertEqual(mmstories.checkIfDateBeforeNow("31 FEB 2011", f), False)

		#US14
		mmstories.checkLessThan5SharedSiblingBdays(fam, ind, f)
		self.assertFalse("I19" in ind)
		self.assertFalse("I32" in ind)
		self.assertFalse("I43" in ind)
		self.assertTrue("I01" in ind)
		self.assertTrue(len(fam["F23"]["CHIL"])==0)

		#getAge
		self.assertTrue(mmstories.getAge("3 MAR 1998") == 20)
		self.assertTrue(mmstories.getAge("1 APR 1999") == 19)
		self.assertTrue(mmstories.getAge("21 NOV 2000") == 17)

		#US10
		self.assertTrue(mmstories.marrAfter14(fam, ind, f))
		self.assertFalse(mmstories.marrAfter14(fam2, ind, f))
		
		#US34
		self.assertTrue(mmstories.logLargeAgeDif(fam, ind, f))
		self.assertFalse(mmstories.logLargeAgeDif(fam, ind2, f))

		#US28
		self.assertTrue(mmstories.orderChildrenByAge(fam3, ind3, f))
		self.assertFalse(mmstories.orderChildrenByAge(fam4, ind3, f))
		
		#US29
		self.assertEqual(mmstories.listDeceased(ind3, f), 1)
		self.assertEqual(mmstories.listDeceased(ind4, f), 3)
		
		f.close()


if __name__ == '__main__':
    unittest.main()