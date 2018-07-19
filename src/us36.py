import unittest

def us36_print_recent_deaths(self):
    """" US36 Print deaths in the last 30 days in pretty table
        """
        people = self.individuals
        table = PrettyTable(["ID", "Name", "Deathdate"])

        for person_id in people:
            person = self.individuals[person_id]
            recent_date = self._current_time - timedelta(days=30)

            if person.get_death_date() is None:
                pass
            if person.get_death_date() is not None:
                if recent_date < person.get_death_date() and person.get_death_date() < self._current_time:
                    table.add_row([person.get_person_id(), person.get_name(), person.get_death_date()])

        print("Recent Deaths")
        print(table)
