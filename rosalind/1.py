s = 'CTCGCTGTCTTCCCGTATTATAATGCATGGCCCGCACGGAAGTGGCGTATATGTTGTAATTCGCCGATTCCCAGTAGCCAGCCACCGCTCATTATGGGTATGGCGGCTCAGCCACACCTTGTAGTGCTTCGGGAGGGCAGAGCCTTTGGACGCATGAAAAACTGCCCTTCCTGCCACTCACAATGAACATATTAAACCTTAATACACTGCGAAAACTAGCTGAACGGGAGTACTGCGTGTCTTTTTGTGTGAGCAGAGGATAACGTCTCCTACTCGGCCAGTTCGCTGTTAGCGACCGGGCAGTTTCCTGGGTACGGCAAATTAATCATCTACTTGCGCAATAACGCGGCCTCGCTGCTAGAAGGATTGAGCACGGCACGGTGGTTCGGAGCTGTTAGTTGCCCCTAGCACACCTGAAGCTCTTGGTGGTTTTAACTAACCTGTTCGTCGCGGAATGGATCAATTGGGATTAATAACTGGAGGGAATCTTTTAACGCCAACTTCCAATGGTAAATCACGCCGTTTTCCCCCTATAGCAATGAGCAGGTGGCATCTGGTTCTGTAAGTTCAGGATCCCTCGTAGAACAGTGTGTCCCATGCAAAGCGACACGTGAAGTTTCAGCCACTTGATTGAGCGCATGGCGTTACGCTCCTCCTATCTGTTGGCCCGACCGCTGACGCAGAACGCATTTACGATCAGAAGATGCGGAGAGTGGAAGGACAATGTATACAACACTGTGTTCCGGTCGCCGCTCACTCTCCTCGCATCAGGGGGCCTCAGAATCTGCTATGAGTCTCCAGCCA'

def count(st, c):
    return len(filter(lambda x: x == c, st))

print count(s, 'A'), count(s, 'C'), count(s, 'G'), count(s, 'T')
