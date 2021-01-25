#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup


version = "1.0.0"


setup(
    name="gkeys",
    version=version,
    description="Logitech gaming keyboard extended keys redirector",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Daniel Monteiro Basso",
    author_email="daniel@basso.inf.br",
    url="https://github.com/dmbasso/gkeys",
    license="GPLv3+",
    py_modules=["gkeys"],
    entry_points={
        'console_scripts': [
            'gkeys=gkeys:main',
        ],
    },
    install_requires=["evdev", "docopt"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: '
        'GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3.9'
    ]
)
