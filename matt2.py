import os
import filecmp
import argparse
from pathlib import Path
import datetime
import sys

def print_diffs(dcmp, ofile):
    print(f"Comparing {dcmp.left} and {dcmp.right}", file=ofile)
    print('-' * 10, file=ofile)
    if dcmp.common_dirs:
        print("Subdirectories appearing in both locations:", file=ofile)
        for x in dcmp.common_dirs:
            print(f"-> {x}", file=ofile)
        print(" ", file=ofile)
    if dcmp.left_only or dcmp.right_only:
        if dcmp.left_only:
            print(f"Files/Subdirs ONLY in {dcmp.left}:", file=ofile)
            for x in dcmp.left_only:
                #end_char = os.sep if os.path.isdir(x) else ' '
                print(f"-> {x}", file=ofile)
            print(" ", file=ofile)
        if dcmp.right_only:
            print(f"Files/Subdirs ONLY in {dcmp.right}:", file=ofile)
            for x in dcmp.right_only:
                #end_char = os.sep if os.path.isdir(x) else ' '
                print(f"-> {x}", file=ofile)
            print(" ", file=ofile)
    else:
        print("** Directory contents are the same for both locations! **", file=ofile)
    print(" ", file=ofile)

    for sub_dcmp in dcmp.subdirs.values():
        print_diffs(sub_dcmp, ofile)

parser = argparse.ArgumentParser(description='Recursively compare filenames between two provided filepaths')
parser.add_argument('first_dir', help='Filepath of the first directory to compare')
parser.add_argument('second_dir', help='Filepath of the second directory to compare')
parser.add_argument('-o', '--out', action='store_true', dest='to_out', help='Output to stdout instead of log file')
args = parser.parse_args()

#first_dir = str(input("Enter first directory path: "))
#second_dir = str(input("Enter second directory path: "))
#print(" ")

diffs = filecmp.dircmp(args.first_dir, args.second_dir)

if args.to_out:
    #out_filename = sys.stdout
    ofile = sys.stdout
else:
    out_filename = "compare_results_{0:%Y-%m-%d_%H:%M:%S}.txt".format(datetime.datetime.now())
    ofile = open(out_filename, 'w')

print_diffs(diffs, ofile)

if ofile != sys.stdout:
    ofile.close()
