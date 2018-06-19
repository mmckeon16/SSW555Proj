import unittest
from datetime import datetime

#takes date in form DD Mon YYYY

def checkIfDateBeforeNow(date):
	try:
		datetime_object = datetime.strptime(date, '%d %b %Y')
		currDate = datetime.today()
		if datetime_object <= currDate:
			return True
		else:
			return False
	except:
		return False

class MyTest(unittest.TestCase):
	def test(self):
		self.assertTrue(checkIfDateBeforeNow("23 SEP 1960"))
		self.assertEqual(checkIfDateBeforeNow("17 JUN 2029"), False)
		self.assertTrue(checkIfDateBeforeNow(datetime.today().strftime('%d %b %Y')))
		self.assertEqual(checkIfDateBeforeNow("123 JUN 2020"), False)
		self.assertEqual(checkIfDateBeforeNow("31 FEB 2011"), False)
		
if __name__ == '__main__':
    unittest.main()