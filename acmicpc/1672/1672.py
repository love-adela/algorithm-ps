def convert_base(last_two_bases:list)->str:
    m, n = last_two_bases[0], last_two_bases[1]
    if m == 'A' and n == 'A': 
        return 'A'
    elif (m == 'A' and n == 'G') or (m == 'G' and n == 'A'):
        return 'C'
    elif (m == 'A' and n == 'C') or (m == 'C' and n == 'A'):
        return 'A'
    elif (m == 'A' and n == 'T') or (m == 'T' and n == 'A'):
        return 'G'
    elif m == 'G' and n == 'G':
        return 'G'
    elif (m == 'G' and n == 'C') or (m == 'C' and n == 'G'):
        return 'T'
    elif (m == 'G' and n == 'T') or (m == 'T' and n == 'G'):
        return 'A'
    elif m == 'C' and n == 'C':
        return 'C'
    elif (m == 'C' and n == 'T') or (m == 'T' and n == 'C'):
        return 'G'
    else:
        return 'T'

def main(base_list):
    if len(base_list) == 1:
        return ''.join(base_list)
    bases = base_list[:-2]
    bases += [convert_base(base_list[-2:])]
    return main(bases)

_ = int(input())
dna = list(input())
print(main(dna))
