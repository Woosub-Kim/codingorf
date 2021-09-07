def multiple3(seq):
    residue = len(seq)%3
    if len(seq)%3 == 0:
        return seq
    else:
        return seq[:-residue]


def usage():
    print('codingorf: find translatable ORF from input sequence')
    print('codingorf [NT Sequence]')
    print('ORF_SEQ  AA_SEQ1  AA_SEQ2  ...  AA_SEQn')
    seqs = [
        'ATTATGGCCCTTGGGAATTCCTAACTTTTCCGGG',
        'CCTAAATGCATGCTATCATGGGCATGG',
        'ATGAAAAAAAAATAATTTATGCCCCCCCCCTAA',
        'ATGTTTAAAGGGTACCTATAATTATGATGGTAGTTTTTTAATT'
    ]
    for seq in seqs:
        print(f'codingorf {seq}')
