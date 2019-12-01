sequence = {'AA': 'A', 'AG': 'C', 'AC': 'A', 'AT': 'G',
            'GA': 'C', 'GG': 'G', 'GC': 'T', 'GT': 'A',
            'CA': 'A', 'CG': 'T', 'CC': 'C', 'CT': 'G',
            'TA': 'G', 'TG': 'A', 'TC': 'G', 'TT': 'T'
            }

N = int(input())
dna = input()

def get_sequence(dna):
    if len(dna) < 2:
        return dna
    base = dna[-1] + dna[-2] 
    dna = dna[:-2] + sequence[base]
    return get_sequence(dna)

print(get_sequence(dna))

