from ged4py import GedcomReader


ind = {}
fam = {}

path = "../files/test1.ged"
with GedcomReader(path) as detail:
	for record in detail.records0("INDI"):
		ind[record.xref_id] = {"Name":record.name, "Sex":record.sex}

		#print(record.first)

		if record.mother:
			print(record.mother.xref_id)
	for record in detail.records0("FAM") or record in parser.records0("FAMS") or record in parser.records0("FAMC"):
		fam[record.xref_id] = {"Name":"hi" }

		#print(record.name)
print(ind)