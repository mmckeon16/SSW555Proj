import unittest

def us35_print_recent_births(self):
    """" US35 Print births in the last 30 days in pretty table
        """
        people = self.individuals
        table = PrettyTable(["ID", "Name", "Birthdate"])

        for person_id in people:
            person = self.individuals[person_id]
            recent_date = self._current_time - timedelta(days=30)
            if person.get_birth_date() is None:
                pass
            if person.get_birth_date() is not None:
                if recent_date < person.get_birth_date() and person.get_birth_date() < self._current_time:
                    table.add_row([person.get_person_id(), person.get_name(), person.get_birth_date()])

        print("Recent Births")
        print(table)
