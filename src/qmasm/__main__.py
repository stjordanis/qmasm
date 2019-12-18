#! /usr/bin/env python

###################################
# Quantum Macro Assembler         #
# By Scott Pakin <pakin@lanl.gov> #
###################################

import sys
from qmasm.cmdline import ParseCommandLine
from qmasm.parse import FileParser
from qmasm.assertions import AssertParser

class QMASM(ParseCommandLine, FileParser, AssertParser):
    "QMASM represents everything the program can do."

    def __init__(self):
        # List of Statement objects
        self.program = []

    def run(self):
        "Execute the entire QMASM processing sequence."

        # Parse the command line.
        cl_args = self.parse_command_line()
        self.report_command_line(cl_args)

        # Parse the original input file(s) into an internal representation.
        fparse = FileParser(self)

def main():
    "Run QMASM."
    q = QMASM()
    q.run()

if __name__ == "__main__":
    main()
