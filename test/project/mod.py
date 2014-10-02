#!/usr/bin/env python
# vim:set softtabstop=4 shiftwidth=4 tabstop=4 expandtab:

import sys

class SuperAwesomeClass(object):
    """This is a super-awesome class with magical properties!
    """
    def __init__(self, a, b):
        """Epic constructor
        @param a: The first parameter
        @param b: The second parameter
        """
        self.a = a
        self.b = b

    def sum(self):
        """Implements a super-awesome +
        @rtype: int
        """
        return self.a + self.b

    def product(self):
        """Implements a super-awesome *
        @rtpye: int
        """
        return self.a * self.b

    def __repr__(self):
        """Get the super-awesomeness
        @rtype: str
        """
        return "Super Awesome Values: %d, %d"  % (self.a, self.b)



def main(argv=None):
        """Main function. This is the entry point for the program and is run when
        the script is executed stand-alone (i.e. not included as a module

        @param argv: A list of arguments that can over-rule the command line arguments.
        @return: Error status
        @rtype: int
        """
        # Use the command line (system) arguments if none were passed to main
        if argv is None:
            argv = sys.argv

        a,b = 42, 43
        if len(argv) > 1:
            a = int(argv[1])
        if len(argv) > 2:
            b = int(argv[2])

        sup = SuperAwesomeClass(a=a,b=b)

        print "A:\t%d" % sup.a
        print "B:\t%d" % sup.b
        print "Sum:\t%d" % sup.sum()
        print "Prod:\t%d" % sup.product()
        print str(sup)

#---------------------------------------------------------------------------#
#                          End of functions                                 #
#---------------------------------------------------------------------------#
# Run main if this file is not imported as a module
if __name__ == "__main__":
    sys.exit(main())
