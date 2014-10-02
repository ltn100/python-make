#!/usr/bin/env python
# vim:set softtabstop=4 shiftwidth=4 tabstop=4 expandtab:

from setuptools import setup


setup(name='test-python-make',
    # Must comply with http://legacy.python.org/dev/peps/pep-0440/#version-scheme
    version='0.1',

    description='A test package',

    url='https://github.com/ltn100/python-make',
    license='MIT licence, see LICENCE',

    packages=['project'],

    test_suite="project.tests",
)

