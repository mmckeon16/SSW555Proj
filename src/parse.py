import sys, re

tree = {}

def parse(line):
    # setup static variables
    if 'person' not in parse.__dict__:
        parse.person = {}
    if 'parent' not in parse.__dict__:
        parse.parent = None

    m = re.match('^(\d+) (?:@(\w+)@ )?(\w+)(?: )?(.+)?$', line)
    if m != None:
        layer, id, type, data = m.group(1,2,3,4)

        # individual records
        if type == 'INDI':
            # new individual
            if 'id' in parse.person:
                tree[parse.person['id']] = parse.person
            parse.person = {}
            parse.parent = None
            parse.person['id'] = id
        elif type == 'NAME':
            parse.person['name'] = data
### SNIP
# open the file and read it line by line
with open("../files/test1.ged", 'r') as ged:
    for line in ged:
        parse(line.strip())

print(tree)
