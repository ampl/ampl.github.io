# -*- coding: utf-8 -*-
"""
AMPL Sphinx Theme
-----------------

Sphinx Theme based on `pydata-sphinx-theme <https://github.com/pydata/pydata-sphinx-theme/>`_.

"""
from setuptools import setup
import os


def ls_dir(base_dir):
    """List files recursively."""
    return [
        os.path.join(dirpath.replace(base_dir, "", 1), f)
        for (dirpath, dirnames, files) in os.walk(base_dir)
        for f in files
    ]


setup(
    name="ampl_sphinx_theme",
    version="0.0.0a29",
    description="AMPL Sphinx Theme",
    long_description=__doc__,
    license="BSD-3",
    platforms="any",
    author="AMPL Development Team",
    author_email="devteam@ampl.com",
    maintainer="AMPL Development Team",
    maintainer_email="devteam@ampl.com",
    url="https://ampl.com/",
    download_url="https://github.com/ampl/ampl.github.io/ampl-sphinx-theme",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    entry_points={
        "sphinx.html_themes": [
            "ampl_sphinx_theme = ampl_sphinx_theme",
        ]
    },
    install_requires=[
        "pydata-sphinx-theme==0.16.0",
        "sphinx==8.1.3",
        "myst_parser==4.0.0",
        "myst-nb==1.1.2",
        "sphinx-reredirects==0.1.5",
        "sphinx_design==0.6.1",
        "sphinx-copybutton==0.5.2",
        "sphinx-autobuild==2024.10.3",
        "sphinxcontrib-googleanalytics==0.4",
        "breathe==4.35.0",
        "sphinx-sitemap==2.6.0",
    ],
    packages=["ampl_sphinx_theme"],
    package_data={"": ls_dir("ampl_sphinx_theme/")},
)
