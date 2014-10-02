python-make
===========

[![Build Status](https://travis-ci.org/ltn100/python-make.svg?branch=master)](https://travis-ci.org/ltn100/python-make)

A simple python [Makefile](http://en.wikipedia.org/wiki/Makefile) wrapper to map [`make`](http://www.gnu.org/software/make/)\*
utility targets to python [setup.py](https://docs.python.org/2/distutils/setupscript.html) commands.

With the Makefile in the same directory as your setup.py file, you can build/test/install/distribute your python packages
in the following way:

    make                ->      python setup.py build
    make check          ->      python setup.py test
    make install        ->      python setup.py install
    make clean          ->      python setup.py clean
    make sdist          ->      python setup.py sdist


Installation
------------

    cd /path/to/your/project/
    wget https://raw.githubusercontent.com/ltn100/python-make/master/Makefile
    # run all the make commands!


Targets
-------

python-make currently supports the following targets:

* ` ` (no target - alias of `build`)
* `all` (alias of `build`)
* `build`
* `bdist`
* `check` (alias of `test`)
* `clean`
* `install`
* `rpm`
* `sdist`
* `test`


Acknowledgements
----------------

This project was inspired by various works, not least C. Titus Brown and Alexandra Pawlik's
[guide to Python packages and installs](http://2013-norwich-bioinfo.readthedocs.org/en/latest/session3-install.html#building-a-default-basic-makefile),
and [Eric Blake](https://www.redhat.com/archives/libvir-list/2014-June/msg00841.html), a
contributor to the [libvert-python](http://libvirt.org/python.html) project, which uses a
[similar shim](http://libvirt.org/git/?p=libvirt-python.git;a=blob;f=Makefile;h=6c8da0a8763a59f5e18fb0fcf726676407eb8d95;hb=HEAD).


\* I am aware that GNU make is not the only flavour of make!
