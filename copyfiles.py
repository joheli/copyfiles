#!/usr/bin/python
import argparse
import os.path
import re
import glob
from shutil import copy2
from shutil import move


def file_exists(parser, arg):
    if not os.path.isfile(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


def pathToFile(path):
    h, t = os.path.split(path)
    return t


def filenameToDir(filename):
    p = os.path.abspath(filename)
    return os.path.dirname(p)


parser = argparse.ArgumentParser(description="copies files to target directories specified in a text file",
                                 epilog="author: Johannes Elias (joheli@gmx.net)")
parser.add_argument("file", help="text file listing files to be copied with target directories",
                    type=lambda x: file_exists(parser, x))
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-m", "--move", help="move instead of copy files", action="store_true")
parser.add_argument("-c", "--comment", help="character indicating comment in 'file' (default '#')", default="#")
parser.add_argument("-r", "--reverse", help="create file specifying reverse operation (default '')", default="")
parser.add_argument("-d", "--delimiter", help="delimiter character used in 'file' (default '\s+')", default="\s+")
args = parser.parse_args()

d = {}
with open(args.file) as o:
    if args.verbose:
        print "accessing text file {}".format(args.file)
    for l in o:
        if not l.startswith(args.comment):
            (k, v) = re.split(args.delimiter, l.rstrip())
            if "*" in k:
                for filename in glob.glob(k):
                    d[filename] = v
            else:
                d[k] = v
for k in d:
    t = "copying"
    if args.move:
        t = "moving"
        move(k, d[k])
    else:
        copy2(k, d[k])
    if args.verbose:
        print "{} file {} to {}".format(t, k, d[k])

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

print "Done!"
