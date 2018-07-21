import unittest
from prettytable import PrettyTable
from datetime import datetime, timedelta

#I am going to redo this how it should be with our project, 
#and then you should try to follow it to complete the other user story
def us36_print_recent_deaths(ind, file):
    """" US36 Print deaths in the last 30 days in pretty table
        """
    table = PrettyTable(["ID", "Name", "Deathdate"])

    for person_id in ind:
        person = ind[person_id]
        recent_date = datetime.today() - timedelta(days=30)

        if "DEAT" in person:
            death_date = datetime.strptime(person["DEAT"], '%d %b %Y') #this is converting the type of person["DEAT"] from string to date so it can be compared to the other dates
            if recent_date < death_date and death_date < datetime.now():
                table.add_row([person["id"], person["name"], person["DEAT"]])

    file.write("Recent Deaths\n") #this \n adds a new line to keep the output pretty
    file.write(str(table) + "\n")

ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '18 JUL 2018'},
        'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 SEP 1960', 'sex': 'F', 'family': 'F23'},
        'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
        'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F23'},
        'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1981', 'sex': 'F', 'family': 'F12'},
        'I32': {'id': 'I32', 'name': 'Nick /Tary/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F12'},
        'I43': {'id': 'I43', 'name': 'Extra /Person/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F23'},
        'I44': {'id': 'I44', 'name': 'Extra /Person2/', 'BIRT': '13 FEB 1981','sex': 'F', 'family': 'F16'},
        'I45': {'id': 'I44', 'name': 'Extra /Person3/', 'BIRT': '13 FEB 1981','sex': 'M', 'family': 'F16'}}
#these two functions are the two you need for testing
class MyTest(unittest.TestCase):
    def test(self):
        f=open("../test/jeneleeOutput.txt","a+")
        us36_print_recent_deaths(ind, f)
        f.close()

if __name__ == '__main__':
    unittest.main()