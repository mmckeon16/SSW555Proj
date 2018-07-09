import unittest

def unique_ids(individuals, families, file):
    """ US22 - All individual IDs and Family IDs should be unique """
    error_type = "US22"
    return_flag = True

    individual_list = []
    family_list = []
    for individual in individuals:
        print(individual_list)
        print(individual)
        if individual in individual_list:
            error_descrip = "Individual ID already exists"
            error_location = [individual]
            file.write("ERROR US22: Individual ID already exists\n")
            return_flag = False
        else:
            individual_list.append(individual)
    for family in families:
        if family in family_list:
            error_descrip = "Family ID already exists"
            error_location = [family]
            file.write("ERROR US22 Family ID already exists\n")
            return_flag = False
        else:
            family_list.append(family)
    print(individual_list)
    return return_flag

fam = {'F23':
  {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30']},
   'F23': {'fam': 'F16', 'MARR': '12 DEC 2007'}}
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I01': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
  'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I44': {'id': 'I44', 'name': 'Cersi /Lanister/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'}}

class MyTest(unittest.TestCase):
  def test(self):
      f=open("../test/jeneleeOutput.txt","a+")
      self.assertTrue(unique_ids(ind, fam, f))
      
      f.close()


def main():
  safe_open("acceptanceTestOutput.txt", 'a+')

if __name__ == "__main__":
    unittest.main()
