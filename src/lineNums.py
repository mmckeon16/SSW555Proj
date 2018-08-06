'''
US40: List line numbers from GEDCOM source file when reporting errors
'''

import unittest 
import sys
import fileinput

def lineNums(file):
  file.seek(0)
  count = 0
  oline=file.readlines()
  size = len(oline)

  #delete copied file
  file.seek(0)
  file.truncate()


  for line in oline:
    if(count >=size):
      break
    nline = oline[count+count]
    oline.insert(count, str(count) + " "+ nline)
    count = count +1

  oline = oline[0:count]
  file.writelines(oline)
  

class MyTest(unittest.TestCase):
  def test(self):
      f=open("../test/ruthyOutput.txt","a+")
      print("hi")
      lineNums(f)
      print("after")
      #self.assertTrue("Error US15: There are more than 15 siblings for family F36.", line_num = 1)
      # self.assertTrue("Error US18: Siblings Cersi /Lanister/ and Julie /Lee/ cannot be married.", line_num = 17)
      # self.assertTrue("Error US08: Birthdate of child Bryan /Rad/ (I53) is before their parents' marriage.", line_num = 20)
      f.close()

if __name__ == "__main__":
    unittest.main()

