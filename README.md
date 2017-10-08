# copyfiles.py

This python script copies files to directories specified in a text file.

# Usage

Call the script with flag ```-h``` to display a help message:

```
$ python copyfiles.py -h
usage: copyfiles.py [-h] [-v] [-m] [-c COMMENT] [-r REVERSE] [-d DELIMITER]
                    file

copies files to target directories specified in a text file

positional arguments:
  file                  text file listing files to be copied with target
                        directories

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -m, --move            move instead of copy files
  -c COMMENT, --comment COMMENT
                        character indicating comment in 'file' (default '#')
  -r REVERSE, --reverse REVERSE
                        create file specifying reverse operation (default '')
  -d DELIMITER, --delimiter DELIMITER
                        delimiter character used in 'file' (default '\s+')

author: Johannes Elias (joheli@gmx.net)

```
# Arguments

## positional (mandatory) arguments

### file

Specify here the file that contains instructions for the copying or moving of files. Please refer to [files.txt](https://github.com/joheli/copyfiles/blob/master/files.txt "copyfiles file") for an example.

## optional arguments

### -h

This flag makes the script display a help message (see [Usage](#usage)).

### -v

Using this flag increases the verbosity of the script.

### -m

The default action is to copy files; if you wish to move them, use the ```-m``` flag. An error is generated if the files at the destination already exist.

### -c

As default, hash (#) is used to indicate lines that are ignored in 'file'. Use the ```-c``` flag to change it.

### -r

Use this flag to specify a file to which the "reverse" of file is to be written. This file can then be used to revert (undo) a previously executed copy/move operation.

### -d

Specify a delimiter differing from whitespace ('\s+') with this flag.