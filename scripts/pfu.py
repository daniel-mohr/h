#!/usr/bin/env python2
"""
Author: Daniel Mohr.
Date: 2017-02-06 (last change).
License: GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007.
"""

import argparse
import logging
import logging.handlers
import os
import sys

import pfu_module.scripts

__pfu_date__ = "2017-02-06"

def main():
    """
    :Author: Daniel Mohr
    :Email: daniel.mohr@dlr.de
    :Date: 2017-02-06 (last change).
    :License: GNU GENERAL PUBLIC LICENSE, Version 3, 29 June 2007.
    """
    myhelp = ""
    myhelp += "Examples:\n\n"
    myhelp += " pfu.py -h\n"
    myhelp += " pfu.py simscrub -h\n"
    myhelp += " pfu.py -h\n"
    parser = argparse.ArgumentParser(
        description='pfu.py is a python script for'+
        ' simple file handling. Command line parameters can be shorten,'+
        ' as far as they are unique.',
        epilog=("Author: Daniel Mohr\n"+
                "Date: %s\n"+
                "License: GNU GENERAL PUBLIC LICENSE, "+
                "Version 3, 29 June 2007.\n\n%s") % (
                    __pfu_date__, myhelp),
        formatter_class=argparse.RawDescriptionHelpFormatter)
    # subparsers
    subparsers = parser.add_subparsers(
        help='There are different sub-commands with there own flags.')
    # subparser simscrub
    pfu_module.scripts.create_subparser_simscrub(subparsers)
    # subparser create_checksum
    pfu_module.scripts.create_subparser_create_checksum(subparsers)
    # parse arguments
    args = parser.parse_args()
    # create log
    log = logging.getLogger("pfu")
    log_console_handler = logging.StreamHandler()
    log_console_handler.setFormatter(
        logging.Formatter('%(asctime)s %(threadName)s %(levelname)s %(message)s',
                          datefmt='%Y-%m-%d %H:%M:%S'))
    log_console_handler.setLevel(args.loglevel[0])
    log.addHandler(log_console_handler)
    if args.logfile is not None:
        file_handler = logging.handlers.WatchedFileHandler(args.logfile[0]) # not thread safe
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)s %(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S'))
        file_handler.setLevel(args.logfilelevel[0])
        log.addHandler(file_handler)
    log.setLevel(min(args.loglevel[0], args.logfilelevel[0]))
    log.debug("running on %s", os.name)
    if os.name == "posix":
        log.debug("os.uname(): %s", " ".join(os.uname()))
    log.debug("sys.platform: %s", sys.platform)
    log.debug("sys.version: %s", sys.version.replace("\n", " "))
    # call the programs
    exit_status = args.func(args)
    # flush log and exit with result from program
    log_console_handler.flush()
    if args.logfile is not None:
        file_handler.flush()
    sys.exit(exit_status)

if __name__ == "__main__":
    main()
