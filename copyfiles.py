#!/usr/bin/python
import argparse
import os.path
import re
import glob
import sys
from shutil import copy2
from shutil import move

# Version no.
version = "0.5"


# function to check if file exists
def file_exists(parser, arg):
    if not os.path.isfile(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


# function returning the filename only given the path
def pathToFile(path):
    h, t = os.path.split(path)
    return t


# function returning the directory in which a given file resides
def filenameToDir(filename):
    p = os.path.abspath(filename)
    return os.path.dirname(p)


# create an argument parser and add positional (=mandatory) and optional arguments
parser = argparse.ArgumentParser(description="copies files to target directories specified in a text file",
                                 epilog="version: {}, author: Johannes Elias (joheli@gmx.net)".format(version))
parser.add_argument("file", help="text file listing files to be copied with target directories",
                    type=lambda x: file_exists(parser, x))
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-m", "--move", help="move instead of copy files", action="store_true")
parser.add_argument("-c", "--comment", help="character indicating comment in 'file' (default '#')", default="#")
parser.add_argument("-r", "--reverse", help="create file specifying reverse operation (default '')", default="")
parser.add_argument("-d", "--delimiter", help="delimiter character used in 'file' (default '\s+')", default="\s+")
args = parser.parse_args()

# start with an empty dictionary d that is to contain the contents of 'file'
d = {}

# dirOfFile stores the directory in which 'file' resides; this value is needed, if source paths are not absolute
dirOfFile = filenameToDir(args.file)

# read file
with open(args.file) as o:
    if args.verbose:
        print "accessing text file {}".format(args.file)
    for l in o:
        # leave out lines starting with args.comment AND empty lines
        if not l.startswith(args.comment) and l.rstrip().strip() != "":
            (k, v) = re.split(args.delimiter, l.rstrip())
            # prepend dirOfFile, if k (first column) is not an absolute path
            if not os.path.isabs(k):
                k = "{}{}{}".format(dirOfFile, os.sep, k)
            # treat asterisks (*) as a wildcard
            if "*" in k:
                for filename in glob.glob(k):
                    d[filename] = v
            else:
                d[k] = v

# the default action is copying; this can be changed with the -m flag
action = "copying"
for k in d:
    if args.move:
        action = "moving"
        move(k, d[k])
    else:
        copy2(k, d[k])
    if args.verbose:
        print "{} file {} to {}".format(action, k, d[k])

# reverse file is generated, if the -r flag is specified
if args.reverse != "":
    dr = {}
    for k in d:
        newFilePath = d[k] + os.sep + pathToFile(k)
        dirname = filenameToDir(k)
        dr[newFilePath] = dirname
    rfile = open(args.reverse, "w")
    for k2 in dr:
        rfile.write("{}\t{}\n".format(k2, dr[k2]))
    rfile.close()
    if args.verbose:
        print "reverse file saved at {}".format(args.reverse)

# wrap it up with a final message, if args.verbose was chosen
if args.verbose:
    print "{} finished {} files specified in {}".format(sys.argv[0], action, args.file)
