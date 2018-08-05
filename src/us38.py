import unittest
    
def us_38_print_upcoming_birthdays(name, individuals, id, birthdate,):
        """"US38
        Prints birthdays within the next 30 days
        """
        people = self.individuals
        table = PrettyTable(["ID", "Name", "Birthday"])

        for person_id in people:
            # type: Person
            individual = self.individuals[individual_id]
            today = datetime.today()
            individual_birthday = individual.get_birth_date()
            if individual_birthday is not None and individual.get_is_alive():
                individual_current_birthday = datetime(today.year, individual_birthday.month, individual_birthday.day)
                if 0 <= (individual_current_birthday - today).days <= 30:
                    table.add_row([individual.get_person_id(), individual.get_name(), individual_birthday])

        print("Upcoming Birthdays")
        print(table)
        
class MyTest(unittest.TestCase):
    def test(self): 
        f=open("../test/jeneleeOutput.txt","a+")
        self.assertTrue(us38_print_upcoming_birthdays(ind,f))
        f.close()
        
if __name__ == '__main__':
    unittest.main()