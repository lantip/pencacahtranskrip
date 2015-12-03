#!/usr/bin/python

import sys, getopt
from collections import Counter
import re

def main(argv):
    findtext = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["text="])
    except getopt.GetoptError:
        print 'counter.py -i <findtext>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'counter.py -i <findtext>'
            sys.exit()
        elif opt in ("-i", "--text"):
            findtext = arg
    words = re.findall(r'\w+', open('transkrip.txt').read().replace('\n',' ').lower())
    counts = Counter()
    for word in words:
        if findtext.lower() in word:
            counts[word] += 1
    print counts

if __name__ == "__main__":
   main(sys.argv[1:])