python-make
===========

[![Build Status](https://travis-ci.org/ltn100/python-make.svg?branch=master)](https://travis-ci.org/ltn100/python-make)

A simple python [Makefile](http://en.wikipedia.org/wiki/Makefile) wrapper to map [`make`](http://www.gnu.org/software/make/)\*
utility targets to python [setup.py](https://docs.python.org/2/distutils/setupscript.html) commands.

With the Makefile in the same directory as your setup.py file, you can build/test/install/distribute your python packages
in the following way:

    make
    make check
    make install
    make clean
    make sdist


Installation
------------

    cd /path/to/your/project/
    wget https://raw.githubusercontent.com/ltn100/python-make/master/Makefile
    # run all the make commands!


\* I am aware that GNU make is not the only flavour of make!
