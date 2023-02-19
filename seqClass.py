#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser
from collections import Counter

# Handle command line arguments
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# If there are no arguments, print help message and exit the program
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the command line arguments
args = parser.parse_args()

# Classify the sequence
args.seq = args.seq.upper()
if re.search('^[ACGT]+$', args.seq):
    print ('The sequence is DNA')
elif re.search('^[ACGU]+$', args.seq):
    print ('The sequence is RNA')
else:
    print ('The sequence is not DNA nor RNA')

# Search for the motif in the sequence (if provided)
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")

# Calculate nucleotide frequencies and percentages
nucleotide_counts = Counter(args.seq)
nucleotide_percentages = {base: count/len(args.seq)*100 for base, count in nucleotide_counts.items()}
# Print the nucleotide percentages
print("Nucleotide percentages:")
for base, percentage in nucleotide_percentages.items():
    print(f"{base}: {percentage:.2f}%")
