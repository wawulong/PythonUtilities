#!/usr/bin/env python

import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

# absolute import, relative import
from package.hello import say

def hello():
    say("Hello")

def _test():
    hello(__file__)

if __name__ == "__main__":
    hello()