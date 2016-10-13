from bs4 import BeautifulSoup as BS

soup = BS(open('Fname'))

for tag in soup.findAll(True):
	if tag.findAll('notes'):
		print(tag.text)

