valid = {'0':('INDI','FAM','HEAD','TRLR','NOTE'), '1':('NAME','SEX','BIRT','DEAT','FAMC', 'FAMS'), '2':('DATE')}         

file_name = input("Give me a file name to parse (in single quotes): ")

try:
    file = open(file_name)
except IOError:
    raise IOError("Can't open '{}'".format(file_name))

for line in file:
    print("--> {}".format(line.strip()))
    
    word_list = line.strip().split()
    isValid = 'N'
    level = "NA"
    tag = "NA"
    arguments = " ".join(word_list[2:])

    if len(word_list) == 1:
        level = word_list[0]

    elif len(word_list) > 1:
        level = word_list[0]
        tag = word_list[1]

        if len(word_list) == 3 and word_list[0] == '0' and word_list[2] in ('INDI', 'FAM'):
            isValid = 'Y'
            tag = word_list[2]

        elif len(word_list) > 1 and level in valid and tag in valid[level]:
            isValid = 'Y'
            
    print('<-- ' + level + '|' + tag + '|' + isValid + '|' + arguments)