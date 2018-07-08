def unique_names_and_birth_dates(individuals, families):
    """ US23 - No more than one individual with the same name and birth
        date should appear in a GEDCOM file - ANOMALY """
    anom_type = "US23"
    return_flag = True

    for individual in individuals:
        for compare_indiv in individuals:
            if individual.name and compare_indiv.name \
                    and individual.name == compare_indiv.name:
                # same name, compare birthdate
                if compare_indiv.birthdate and individual.birthdate \
                        and compare_indiv.birthdate and individual.birthdate:

                    anom_descrip = "Two individuals share a name and birthdate"
                    anom_location = [individual.uid, compare_indiv.uid]
                    report_anomaly(anom_type, anom_descrip, anom_location)
                    return_flag = False

    return return_flag