import unittest
from datetime import datetime

# rachel stern's user stories

# code for us02
def us02(id, name, birthdate, mardate, gen):
  if ((datetime.strptime(birthdate, '%d %b %Y')) > (datetime.strptime(mardate, '%d %b %Y')) and gen == "her"):
    error_wifeus02 = "Error US02: Marriage of " + name + " (" + id + ") occurs before her birthday.\n"
    f=open("../test/acceptanceTestOutput.txt","a+")
    f.write(error_wifeus02)
    f.close();
  if ((datetime.strptime(birthdate, '%d %b %Y')) > (datetime.strptime(mardate, '%d %b %Y')) and gen == "his"):
    error_husbus02 = "Error US02: Marriage of " + name + " (" + id + ") occurs before his birthday.\n"
    f=open("../test/acceptanceTestOutput.txt","a+")
    f.write(error_husbus02)
    f.close()

# code for us04
def us04(marrdate, divdate, hubname, wifename):
  if ((datetime.strptime(marrdate, '%d %b %Y')) > (datetime.strptime(divdate, '%d %b %Y'))):
      error_us04 = "Error US04: Divorce of " + hubname + " and " + wifename + " happens before their marriage date."
      f=open("../test/acceptanceTestOutput.txt","a+")
      f.write(error_us04)
      f.close()

# test for us02 - need to fix
#class MyTest(unittest.TestCase):
#  def test(self):
    #these three test the date function
#    self.assertEqual(form_d("15 JUL 1960", "16 JUL 1960"), 2)
#    self.assertEqual(form_d("15 JUN 1960", "15 JUL 1960"), 1)
#    self.assertEqual(form_d("12 DEC 1880", "12 DEC 1881"), 1)
    #these test us02
#    self.assertEqual(error_husbus02, us02("I07", "Joe /Smith/", "19 JUL 1990", "20 JUN 1880", "his"))
#    self.assertEqual(error_wifeus02, us02("I08", "Jane /Doe", "20 JUN 1923", "12 FEB 2000", "her"))
    #these test us04

# if __name__ == '__main__':
#   unittest.main()
