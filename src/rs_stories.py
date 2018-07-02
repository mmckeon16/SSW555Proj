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
    return error_wifeus02
  if ((datetime.strptime(birthdate, '%d %b %Y')) > (datetime.strptime(mardate, '%d %b %Y')) and gen == "his"):
    error_husbus02 = "Error US02: Marriage of " + name + " (" + id + ") occurs before his birthday.\n"
    f=open("../test/acceptanceTestOutput.txt","a+")
    f.write(error_husbus02)
    f.close()
    return error_husbus02

# code for us04
def us04(marrdate, divdate, hubname, wifename):
  if ((datetime.strptime(marrdate, '%d %b %Y')) > (datetime.strptime(divdate, '%d %b %Y'))):
      error_us04 = "Error US04: Divorce of " + hubname + " and " + wifename + " happens before their marriage date."
      f=open("../test/acceptanceTestOutput.txt","a+")
      f.write(error_us04)
      f.close()
      return error_us04

# code for us06
def us06(wifeName, wifedeathdate, hubname, hubdeathdate, divdate):
  if ((datetime.strptime(wifedeathdate, '%d %b %Y')) < (datetime.strptime(divdate, '%d %b %Y')) or (datetime.strptime(hubdeathdate, '%d %b %Y')) < (datetime.strptime(divdate, '%d %b %Y'))):
    error_us06 = "Error US06: Divorce of " + wifeName + " and " + hubname + " occurs after one or both of them have died."
    f=open("../test/acceptanceTestOutput.txt","a+")
    f.write(error_us06)
    f.close()
    return error_us06

class MyTest(unittest.TestCase):
  def test(self):
    #these test us02
    us02("I07", "Joe /Smith/", "19 JUL 1990", "20 JUN 1880", "his")
    self.assertEqual(us02("I07", "Joe /Smith/", "19 JUL 1990", "20 JUN 1880", "his"), "Error US02: Marriage of Joe /Smith/ (I07) occurs before his birthday.\n")
    self.assertEqual(us02("I08", "Jane /Doe/", "20 JUN 1923", "12 FEB 2000", "her"), None)
    # these test us04
    self.assertEqual(us04("19 JUL 1990", "18 JUL 1990", "Joe /Smith/", "Jane /Doe/"), "Error US04: Divorce of Joe /Smith/ and Jane /Doe/ happens before their marriage date.")
    self.assertEqual(us04("19 JUL 1990", "18 JUL 1995", "Joe /Smith/", "Jane /Doe/"), None)
    # these test us06
    self.assertEqual(us06("Jane /Doe/", "20 DEC 2030", "Joe /Smith/", "12 OCT 2015", "21 NOV 2029"), "Error US06: Divorce of Jane /Doe/ and Joe /Smith/ occurs after one or both of them have died.")
    self.assertEqual(us06("Jane /Doe/", "20 DEC 2010", "Joe /Smith/", "12 OCT 2015", "21 NOV 2009"), None)
    

if __name__ == '__main__': unittest.main()
