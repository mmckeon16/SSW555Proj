import unittest
import sys
sys.path.insert(0, '../src')
import project

theVars = project.gedComProj()

class MyTest(unittest.TestCase):
	def test(self):
		self.assertFalse("I25" in theVars["ind"])
		self.assertFalse("I24" in theVars["ind"])
		self.assertFalse("I23" in theVars["ind"])
		self.assertFalse("I22" in theVars["ind"])
		self.assertFalse("I21" in theVars["ind"])
		
if __name__ == '__main__':
    unittest.main()