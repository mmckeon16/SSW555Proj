'''
US40: List line numbers from GEDCOM source file when reporting errors
'''

import unittest 
import sys
import fileinput

def lineNums(file):
  result = False
  file.seek(0)
  count = 0
  oline=file.readlines()
  size = len(oline)

  #delete copied file
  file.seek(0)
  file.truncate()


  for line in oline:
    if(count >=size):
      result = True
      break
    nline = oline[count+count]
    oline.insert(count, str(count) + " "+ nline)
    count = count +1

  oline = oline[0:count]
  file.writelines(oline)
  return result
  
class MyTest(unittest.TestCase):
  def test(self):
      f=open("../test/ruthyOutput.txt","a+")
      self.assertTrue(lineNums)
      f.close()

if __name__ == "__main__":
    unittest.main()

