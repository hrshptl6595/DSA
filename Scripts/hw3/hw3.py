from bs4 import BeautifulSoup as BS

def sbml_parser(fname):
	soup = BS(open(fname))
	species_ref = soup.listofspecies
	for tag in soup.listofreactions.findAll('reaction'):
		print(tag['id']+":",end=" ")
		no_reactants = len(tag.listofreactants.findAll('speciesreference'))
		for reactant in tag.listofreactants.findAll('speciesreference'):
			print(reactant['stoichiometry'],species_ref.find(id = reactant['species'])['name'],end=" ")
			no_reactants -= 1
			if no_reactants == 0:
				print("",end=" ")
			else:
				print(" +",end=" ")
		if tag['reversible'] == 'false':
			print("=>",end=" ")
		elif tag['reversible'] == 'true':
			print("<=>",end=" ")
		no_products = len(tag.listofproducts.findAll('speciesreference'))
		for product in tag.listofproducts.findAll('speciesreference'):
			print(product['stoichiometry'],species_ref.find(id = product['species'])['name'],end=" ")
			no_products -= 1
			if no_products == 0:
				print(" ")
			else:
				print(" +",end=" ")
	return len(soup.listofreactions.findAll('reaction'))


if __name__ == '__main__':
	print("Total number of reactions is: ",sbml_parser('Ec_iAF1260_flux1.xml'))
