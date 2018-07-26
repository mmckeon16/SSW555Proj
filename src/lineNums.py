'''
US40: List line numbers from GEDCOM source file when reporting errors
'''

import unittest 

def safe_open(file, mode):
    try:
        return open(file, mode)
    except IOError:
        raise IOError("Can't open '{}' for '{}'".format(file, mode))

def lineNums(file):
    for line_num, line in enumerate(file): 
        file.write("Here is a list of line numbers from the GEDCOM source file when reporting errors:'{}\t{}'.format(line_num, line)\n")

class MyTest(unittest.TestCase):
  def test(self):
      f= open("../test/ruthyOutput.txt","a+")
      lineNums(f)
      self.assertTrue("Error US15: There are more than 15 siblings for family F36.", line_num = 1)
      self.assertTrue("Error US18: Siblings Cersi /Lanister/ and Julie /Lee/ cannot be married.", line_num = 17)
      self.assertTrue("Error US08: Birthdate of child Bryan /Rad/ (I53) is before their parents' marriage.", line_num = 20)
      f.close()


def main():
  safe_open("acceptanceTestOutput.txt", 'a+')

if __name__ == "__main__":
    unittest.main()

