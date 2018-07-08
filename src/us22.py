def unique_ids(individuals, families):
    """ US22 - All individual IDs and Family IDs should be unique """
    error_type = "US22"
    return_flag = True

    individual_list = []
    family_list = []

    for individual in individuals:
        if individual.uid in individual_list:
            error_descrip = "Individual ID already exists"
            error_location = [individual.uid]
            report_error(error_type, error_descrip, error_location)
            return_flag = False
        else:
            individual_list.append(individual.uid)
    for family in families:
        if family.uid in family_list:
            error_descrip = "Family ID already exists"
            error_location = [family.uid]
            report_error(error_type, error_descrip, error_location)
            return_flag = False
        else:
            family_list.append(family.uid)
    return return_flag