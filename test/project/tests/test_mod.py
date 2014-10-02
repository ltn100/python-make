#!/usr/bin/env python
# vim:set softtabstop=4 shiftwidth=4 tabstop=4 expandtab:

# Import external modules
import sys
import os
import unittest

# Import project modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import mod


class SuperAwesomeClassTests(unittest.TestCase):
    def test_sum(self):
        sup = mod.SuperAwesomeClass(1, 1)
        self.assertEquals(2, sup.sum())


#---------------------------------------------------------------------------#
#                          End of functions                                 #
#---------------------------------------------------------------------------#
if __name__ == "__main__":
    sys.exit(unittest.main())
