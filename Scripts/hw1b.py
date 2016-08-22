#BT3051 Assignment 1b
#Roll Number: ED13B045
#Time: 0:45

import doctest

def translate_DNA(mrna, translation_table = 'RNA_TABLE.txt'):
	"""
	Returns the translated sequence of the given mRNA sequence
	>>> translate_DNA('AUGUAUGAUGCGACCGCGAGCACCCGCUGCACCCGCGAAAGCUGA')
	'MYDATASTRCTRES'
	"""
	rna_map = {}
	with open(translation_table) as f:
		for line in f:
			line = line.replace('      ',',')
			line = line.replace('   ',',')
			for c in line.split(','):
				(key, val) = c.split()
				rna_map[key] = val
	trans_dna = ''
	for i in range(0, len(mrna)-2, 3):
		if rna_map.get(str(mrna[i:i+3])) != "Stop":
			trans_dna += rna_map.get(str(mrna[i:i+3]))

	return trans_dna

if __name__ == '__main__':
	doctest.testmod(verbose = True)
	print(translate_DNA('AUGUAUGAUGCGACCGCGAGCACCCGCUGCACCCGCGAAAGCUGA'))