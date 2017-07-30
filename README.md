# files_collector
collect any files from one directory and subdirectories to one output directory (by extension)

python 2.7

How to use?

Run files_collector.py with args:
  
usage: files_collector.py [-h] [-in ROOT_DIR] [-out OUT_DIR]
                          [-ext EXT_PATTERN] [-act COPY_OR_MOVE]

optional arguments:
  -h, --help            show this help message and exit
  -in ROOT_DIR, --root_dir ROOT_DIR
                        input directory (root)
  -out OUT_DIR, --out_dir OUT_DIR
                        output directory
  -ext EXT_PATTERN, --ext_pattern EXT_PATTERN
                        files extension (by default *.*)
  -act COPY_OR_MOVE, --copy_or_move COPY_OR_MOVE
                        type of action: c - copy, m - move  
  
 --------------------------------------------------
  -in   - is argument for input directory path
  -out  - is argument for output directory path
  -ext  - is argument for files extension (by default *.*)
  -act  - is argument for type of action: c - copy, m - move (by default copy)
 
This script uses cmd progress bar:
[====================================================================================================] 100.0% ... completed! 
 
Examples (using cmd):

d:\files_collector>files_collector.py -in c:\tmp\ -out d:\collection -ext *.mp3 -act c
- this command copy all *mp3 files from "c:\tmp\" and subdirectories to "d:\collection"

d:\files_collector>files_collector.py -in c:\tmp\ -out d:\collection -ext *.mp3 -act m
- this command move all *mp3 files from "c:\tmp\" and subdirectories to "d:\collection"

d:\files_collector>files_collector.py -in c:\tmp\ -out d:\collection 
- this command copy all files from "c:\tmp\" and subdirectories to "d:\collection"