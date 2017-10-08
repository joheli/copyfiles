# copyfiles
Copies files to directories specified in a text file

# Usage

Checkout the help message to get aquainted with the usage of copyfiles:

`johannes@blausturm:~/Lernen/Python/copyfiles$ python copyfiles.py -h
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

author: Johannes Elias (joheli@gmx.net)`

