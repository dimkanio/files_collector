# -*- coding: UTF-8 -*-
import os
import sys
import fnmatch
import shutil
import argparse

"""  Class to copy all files in sub-directories to one single directory """
class FileCollector():
    #define variables
    _copy_or_move = 'c'
    _root_dir = ''
    _out_dir = ''
    _ext_pattern = ''
    _files = {}
    _quantity = 20

    """ Constructor """
    def __init__(self, root_dir, out_dir=None, ext_pattern='*.*', copy_or_move='c'):
        #set variable
        self._root_dir = root_dir
        self._copy_or_move = copy_or_move
        self._ext_pattern = ext_pattern
        if out_dir is None:
            self._out_dir = os.path.join(self._out_dir, 'out')
        else:
            self._out_dir = out_dir
        #remove if exists
        if (os.path.exists(self._out_dir)):
            shutil.rmtree(self._out_dir)
        #create out dir
        os.mkdir(self._out_dir)

    """ Update progress bar"""
    def progress(self, cnt, suffix=' completed!'):
        bar_len = 100
        filled_len = int(round(bar_len * cnt / float(self._quantity)))
        percents = round(100.0 * cnt / float(self._quantity), 1)
        bar = '=' * filled_len + '-' * (bar_len - filled_len)
        sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
        sys.stdout.flush()
        if (cnt == self._quantity):
            print ("Processed " + str(cnt) + " files!\r\n")

    """ Get files list """
    def get_files_list(self):
        #walk throw dirs
        for path, subdirs, files in os.walk(self._root_dir):
            for name in fnmatch.filter(files, self._ext_pattern):
                self._files[os.path.join(path, name)] = os.path.join(self._out_dir, name)
        #get percengage
        self._quantity = len(self._files)

    """ Copy files to out dir"""
    def collect_files_to_out(self):
        #get files list
        self.get_files_list()

        #set progress counter
        progress_cnt = 1

        #for each file
        for src, dst in self._files.items():
            if (self._copy_or_move == 'c'):
                shutil.copy(src, dst)
            elif (self._copy_or_move == 'm'):
                shutil.move(src, dst)
            else:
                raise ValueError('Incorrect argument copy_or_move. Should be -c or -m or blank (by default -c)')

            #print percentage
            self.progress(progress_cnt)

            #update counter
            progress_cnt = progress_cnt + 1

""" Create CL args parser"""
def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--root_dir', help="input directory (root)")
    parser.add_argument('-out', '--out_dir', default=None, help="output directory")
    parser.add_argument('-ext', '--ext_pattern', default='*.*', help="files extension (by default *.*)")
    parser.add_argument('-act', '--copy_or_move', default='c', help="type of action: c - copy, m - move")
    return parser

####################################################################################
######################## Run class methods #########################################
####################################################################################
if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])

    result = FileCollector(root_dir=args.root_dir, out_dir=args.out_dir, ext_pattern=args.ext_pattern, copy_or_move=args.copy_or_move)
    result.collect_files_to_out()

print("")
os.system("pause")
