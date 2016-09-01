#BT3051 Assignment 1a
#Roll Number: ED13B045
#Time: 0:25

import sys
from itertools import groupby
def read_fasta(fname):
	""" (str) -> list of tuples
	sequences = Stores list of tuples
	fo = file open function
	This function converts the text from file to list of tuples
	"""
	sequences = []
	index = 0
	fo = open(fname)
	for line in fo:
		if line.startswith(">"):
			if index >= 1:
				sequences.append(seq_pair)
			index += 1
			seq_name = line[:-1]
			seq = ''
			seq_pair = seq_name, seq
		else :
			seq += line[:-1]
			seq_pair = seq_name, seq
		sequences.append(seq_pair)

	return sequences # a list of (sequence_name, sequence) tuples

def compute_protien_mass(protien_str):
	"""
	Computes the protien mass of a particular sequence
	>>> compute_protien_mass('SKADYEK')
	821.392
	"""
	pm = {}
	with open('PROT_MASS.txt') as f:
		for line in f:
			(key, val) = line.split("   ")
			pm[key] = float(val)
	mass = 0.0
	for c in protien_str:
		mass += pm.get(str(c), 0.0)
	return mass

if __name__ == '__main__':
	for seq_name, seq in read_fasta("hw1_keratin.fasta"):
		print(seq_name, compute_protien_mass(seq))