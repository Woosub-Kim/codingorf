from .funcmodule import multiple3
from Bio.Seq import Seq
import re

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
