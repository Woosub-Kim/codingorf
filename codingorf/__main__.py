from .classmodule import OrfParser
from .funcmodule import usage
import sys

def main():
    input = sys.argv[1]
    if input in ('-h', '--help'):
        usage()
    orfParser = OrfParser(input)
    orfParser.getCodingorf()
    return 0
    

if __name__ == '__main__':
    main()
