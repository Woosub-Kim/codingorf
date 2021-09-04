from Bio.Seq import Seq
import re
import sys
# ATTATGGCCCTTGGGAATTCCTAACTTTTCCGGG
# CCTAAATGCATGCTATCATGGGCATGG
# ATGAAAAAAAAATAATTTATGCCCCCCCCCTAA

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


class OrfParser:
    
    def __init__(self, sequence):
        seq = Seq(sequence)
        rcSeq = seq.reverse_complement()
        self.ORFs = [seq[0:] ,seq[1:] ,seq[2:] ,rcSeq[0:] ,rcSeq[1:] ,rcSeq[2:]]

    def getCodingorf(self):
        for ORF in self.ORFs:
            orf = multiple3(ORF)
            aaSeq = orf.translate()
            p = re.compile("M[ACDEFGHIKLMNPQRSTVWY]*\*")
            pCDS = p.findall(str(aaSeq))
            if pCDS != []:
                print(orf + '  ' + '  '.join(pCDS))




def main():
    input = sys.argv[1]
    if input in ('-h', '--help'):
        usage()
    orfParser = OrfParser(input)
    orfParser.getCodingorf()
    

if __name__ == '__main__':
    main()
