import unittest
import PrettyTable
import datetime, timedelta

def get_is_alive(individual):
    if "DEAT" in individual:
        death = datetime.strptime(individual["DEAT"], '%d %b %Y')
        return False
    else:
        return True


def get_birth_date(individual):
    if "BIRT" in individual:
        birth = datetime.strptime(individual["BIRT"], '%d %b %Y')
        return birth
    else:
        return 0
    
def us_38_print_upcoming_birthdays(individuals, file): #why did you have so many inputs in the method?
        """"US38
        Prints birthdays within the next 30 days
        """
        people = individuals
        table = PrettyTable(["ID", "Name", "Birthday"])

        result = False

        for person_id in people:
            individual = individuals[person_id]
            #also, no self reference and use people if you made that assignment
            individual = people[person_id] 
            today = datetime.today()
            #individual_birthday = individual.get_birth_date() 
            #Again, like last time, we do not have this function, you need to make this function if you want to use it
            #I added the function for you so you can copy it into files if you need to use it
            individual_birthday = get_birth_date(individual)
            if individual_birthday is not 0 and get_is_alive(individual):
                individual_current_birthday = datetime(today.year, individual_birthday.month, individual_birthday.day)
                print(str(individual_current_birthday))
                if 0 <= (abs(individual_current_birthday - today)).days <= 30:
                    #table.add_row([individual.get_person_id(), individual.get_name(), individual_birthday])
                    #the id is just the individual["id"].
                    #the name is individual["name"]
                    #so the real result should look like:
                    table.add_row([individual["id"], individual["name"], individual_birthday])
                    result = True
        file.write("Upcoming Birthdays\n")
        file.write(str(table) + "\n") #you cannot just print the stories, you have to write them to our test file
        return result

ind = {'I01': {'id': 'I01', 'name': 'Joe /Smith/', 'BIRT': '15 JUL 1960', 'sex': 'M', 'family': 'F23', 'DEAT': '31 DEC 2013'},
 'I07': {'id': 'I07', 'name': 'Jennifer /Smith/', 'BIRT': '23 JUL 1960', 'sex': 'F', 'family': 'F23'},
 'I19': {'id': 'I19', 'name': 'Dick /Smith/', 'BIRT': '13 FEB 1981', 'sex': 'M', 'family': 'F23'},
  'I26': {'id': 'I26', 'name': 'Jane /Smith/', 'BIRT': '13 FEB 1982', 'sex': 'F', 'family': 'F23'},
  'I30': {'id': 'I30', 'name': 'Mary /Test/', 'BIRT': '13 FEB 1987', 'sex': 'F', 'family': 'F23'},
}

class MyTest(unittest.TestCase):
    def test(self): 

        #you are trying to check if something is true but the function is not returning anything
        f=open("../test/jeneleeOutput.txt","a+")
        self.assertTrue(us_38_print_upcoming_birthdays(ind,f))
        #you did not copy over the ind dictionary...
        f.close()
        
if __name__ == '__main__':
    unittest.main()
