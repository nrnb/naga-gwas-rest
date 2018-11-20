#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'argparse',
    'requests',
    'networkx==1.11', #ndex2 requires networks 1.11
    'pandas',
    'ndex2',
    'flask',
    'flask-restplus',
    'numpy',
    'matplotlib',
    'pandas',
    'scipy',
    'seaborn',
    'tables', #For hdf5 reads
    'python-igraph',
    'py2cytoscape'
]

setup_requirements = [ ]

test_requirements = [
    'argparse',
    'requests',
    'networkx==1.11', #ndex2 requires networks 1.11
    'pandas',
    'ndex2',
    'flask',
    'flask-restplus',
    'numpy',
    'matplotlib',
    'pandas',
    'scipy',
    'seaborn',
    'tables',  # For hdf5 reads
    'python-igraph',
    'py2cytoscape',
    'unittest2'
]

setup(
    author="Chris Churas",
    author_email='churas.camera@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="REST service for Network Boosted GWAS",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='nbgwas_rest',
    name='nbgwas_rest',
    packages=find_packages(include=['nbgwas_rest']),
    scripts=['nbgwas_rest/nbgwas_taskrunner.py'],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/coleslaw481/nbgwas_rest',
    version='0.1.0',
    zip_safe=False,
)
