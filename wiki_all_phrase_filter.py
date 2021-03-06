import sys
import codecs
from mafan import simplify, split_text
from textblob import TextBlob
import pdb

LANGUAGE = 'en'

def Load(filename, output_filename):
    candidate = set()
    for line in codecs.open(filename, 'r', 'utf-8'):
        tokens = line.strip().split('\t')
        for token in tokens[2:]:
            name = ':'.join(token.split(':')[:-2])

            if LANGUAGE == 'zh':
                name = simplify(''.join(name.split()))
            candidate.add(name.lower())

        name = tokens[0]
        name = simplify(''.join(name.split()))
        if LANGUAGE == 'zh':
            name = simplify(''.join(name.split()))

        #candidate.add(name.lower())
    print len(candidate)
    
    out = codecs.open(output_filename, 'w', 'utf-8')
    for name in candidate:
        if ':' in name: out.write(name.split(':')[1] + '\n')
    out.close()
    
def main(argv):
    global LANGUAGE
    i = 0
    while i < len(argv):
        if argv[i] == '-lang':
            LANGUAGE = argv[i + 1]
            i += 1
        else:
            print 'Unknown Parameter =', argv[i]
        i += 1

    INPUT_FILENAME = 'data/' + LANGUAGE.upper() + '/entities'
    OUTPUT_FILENAME = 'data/'+ LANGUAGE.upper() + '/wiki_all.txt'

    Load(INPUT_FILENAME, OUTPUT_FILENAME)

if __name__ == '__main__':
    main(sys.argv[1:])