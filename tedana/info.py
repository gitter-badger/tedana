# -*- coding: utf-8 -*-
# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
"""
Base module variables
"""

__version__ = ''
__author__ = 'tedana developers'
__copyright__ = 'Copyright 2017, tedana developers'
__credits__ = ['Elizabeth DuPre', 'Prantik Kundu', 'Ross Markello',
               'Taylor Salo', 'Kirstie Whitaker']
__license__ = 'LGPL 2.0'
__maintainer__ = 'Elizabeth DuPre'
__email__ = 'emd222@cornell.edu'
__status__ = 'Prototype'
__url__ = 'https://github.com/me-ica/tedana'
__packagename__ = 'tedana'
__description__ = ("TE-Dependent Analysis (tedana) of multi-echo functional "
                   "magnetic resonance imaging (fMRI) data.")
__longdesc__ = ("To do.")

DOWNLOAD_URL = (
    'https://github.com/ME-ICA/{name}/archive/{ver}.tar.gz'.format(
        name=__packagename__, ver=__version__))

REQUIRES = [
    'numpy',
    'scikit-learn',
    'mdp',
    'nilearn',
    'nibabel>=2.1.0',
    'pybids>=0.4.0',
    'nipype',
]

TESTS_REQUIRES = [
    "codecov",
    "pytest",
]

EXTRA_REQUIRES = {
    'doc': ['sphinx>=1.5.3', 'sphinx_rtd_theme', 'sphinx-argparse'],
    'tests': TESTS_REQUIRES,
    'duecredit': ['duecredit'],
}

# Enable a handle to install all extra dependencies at once
EXTRA_REQUIRES['all'] = [val for _, val in list(EXTRA_REQUIRES.items())]

# Package classifiers
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering :: Image Recognition',
    'License :: OSI Approved :: LGPL License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.6',
]
