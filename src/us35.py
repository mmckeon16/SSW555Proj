import unittest
from prettytable import PrettyTable # <-- if you want to use prettytable to print this 
from datetime import datetime, timedelta # <-- you need this import for that datetime i have an example of in you other user story

#there is no self going into the function, going into every function should be the 
# fam and/or ind dictionaries, like in your other functions, and the file writer

#so the "people" object would just be ind in this case
def us35_print_recent_births(ind, file):
    """" US35 Print births in the last 30 days in pretty table
    """
    people = ind #<-- this is just ind
    table = PrettyTable(["ID", "Name", "Birthdate"])
    isThereRecentBirth = False

    for person_id in ind: #this would be "for person_id in ind"
        person = ind[person_id] # to get person, you can say ind[person_id]
        recent_date = datetime.today() - timedelta(days=30)
        
        if "BIRT" in person:
            birth_date = datetime.strptime(person["BIRT"], '%d %b %Y')
            if recent_date < birth_date and birth_date < datetime.now():
               table.add_row([person["id"], person["name"], person["BIRT"]])
               isThereRecentBirth = True 
  
    file.write("Recent Births\n") #this \n adds a new line to keep the output pretty
    file.write(str(table) + "\n")
    return isThereRecentBirth #this boolean does not affect the outcome of the function, but it makes it testable


#these fam and ind objects you can just copy from me, ruthy, 
#or rachel's tests, they will be going into your function as I mentioned above
ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
        'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '21 JUL 2018', 'sex': 'F', 'family': 'F23'},
        'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
        'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F12'},
        'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F12'},
        'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
        'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 1981','sex': 'F', 'family': 'F16'},
        'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'}}
fam = {'F23': {'fam': 'F23', 'MARR': '14 FEB 1980', 'HUSB': 'I01', 'WIFE': 'I07', 'CHIL': ['I19', 'I26', 'I30', 'I32', 'I43']},
         'F16': {'fam': 'F16', 'MARR': '12 DEC 2007','HUSB': 'I45', 'WIFE': 'I44'},
         'F12': {'fam': 'F12', 'MARR': '12 DEC 2008','DIV':'12 DEC 2001','HUSB': 'I32', 'WIFE': 'I30'}}

#these two functions are the two you need for testing
class MyTest(unittest.TestCase):
    def test(self):
        f=open("../test/jeneleeOutput.txt","a+")
        self.assertTrue(us35_print_recent_births(ind, f))
        f.close()

if __name__ == '__main__':
    unittest.main()
