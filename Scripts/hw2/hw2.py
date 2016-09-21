#BT3051 Assignment 2
#Roll Number: ED13B045
#Time: 00:55

class DNA: 
	"""Class representing DNA as a string sequence.""" 
 
	basecomplement = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'} 
 
	def __init__(self, fname): 
		"""Create DNA instance initialized to string s.""" 
		self.seq = []
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
		self.seq.append(sequences)
	 
	def transcribe(self): 
		"""Return as rna string.""" 
		for seq_name, seq in self.seq:
			print(seq_name," Transcribed : ",seq.replace('T','U'))
		return 0
	 
	def reverse(self): 
		"""Return dna string in reverse order.""" 
		rev_DNA = []
		for seq_name, seq in self.seq:
			letters = list(seq)
			letters.reverse()
			r_seq = ''.join(letters)
			r_seq_pair = seq_name, r_seq
			rev_DNA.append(r_seq_pair)
		return rev_DNA

	def complement(self): 
		"""Return the complementary dna string.""" 
		comp_DNA = []
		for seq_name, seq in self.seq:
			letters = list(self.seq)
			letters = [self.basecomplement[base] for base in letters]
			comp_seq = ''.join(letters)
			comp_seq_pair = seq_name, comp_seq
			comp_DNA.append(comp_seq_pair)
		return comp_DNA

	def get_comple_strands(self): 
		"""Return the reverse complement of the dna string.""" 
		gcs_DNA = []
		for seq_name, seq in self.seq:
			letters = list(seq)
			letters.reverse()
			letters = [self.basecomplement[base] for base in letters]
			gcs_seq = ''.join(letters)
			gcs_seq_pair = seq_name, gcs_seq
			gcs_DNA.append(gcs_seq_pair)
		return gcs_DNA

	def get_GC(self): 
		"""Return the percentage of dna composed of G+C.""" 
		gc_DNA = []
		for seq_name, seq in self.seq:
			s = seq
			gc = s.count('G') + s.count('C')
			gc_seq = gc * 100.0 / len(s)
			gc_pair = seq_name, gc_seq
			gc_DNA.append(gc_pair)
		return gc_DNA

	def get_base_counts(self):
		"""Returns a dictionary with counts of A, T, G and C bases in the DNA strands"""
		gbc_DNA = []
		for seq_name, seq in self.seq:
			s = seq
			gbc_seq = s.count('A'), s.count('T'), s.count('G'), s.count('C')
			gbc_pair = seq_name, gbc_seq
			gbc_DNA.append(gbc_pair)
		return gbc_DNA

	def locate_restriction_sites(self):
		"""Returns the position and length of every reverse palindrome in the DNA strands"""
		lrs_DNA = []
		for seq_name, seq in self.seq:
			s = seq
			lrs_seq = []
			for i in range(len(s)-4):
				pos = i
				for j in range(4,12,1):
					if s[i:i+j] == s[i:i+j].get_comple_strands():
						lrs_seq_pair = pos, j
						lrs_seq.append(lrs_seq_pair)
			lrs_pair = seq_name, lrs_seq
			lrs_DNA.append(lrs_seq)
		return lrs_DNA