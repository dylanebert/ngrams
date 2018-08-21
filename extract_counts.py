import re
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='input file', type=str, required=True)
args = parser.parse_args()

with open('words.txt') as f:
    words = f.read().splitlines()

counts = {}
with open(args.input) as f:
    for line in f:
        ngram, year, match_count, volume_count = line.split('\t')
        ngram = ngram.lower()
        if ngram.split('_')[0] in words:
            if ngram in counts:
                counts[ngram] += int(match_count)
            else:
                counts[ngram] = int(match_count)

with open('{0}_counts'.format(args.input), 'w+') as f:
    for k, v in counts.items():
        f.write('{0}\t{1}\n'.format(k, v))
