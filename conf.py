# -*- coding: utf-8 -*-
#
# Your project name
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import os
import sys

# You may need to adjust this path depending on your project structure.
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------
project = 'Tusk Courses'
copyright = 'Copyright © 2023, kobowork.com'
author = "Ifiok Tha'SnrDev"

# The version info for your project, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# You can define it as you like, but it's typically in the format "X.Y.Z".
version = '0.1'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',  # Include documentation from docstrings
    'sphinx.ext.napoleon',  # Support for NumPy-style docstrings
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Use the Read the Docs theme (install it if needed)
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------
latex_engine = 'xelatex'
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

# -- Options for manual page output ------------------------------------------
man_pages = [
    (master_doc, 'yourprojectname', 'Tusk Courses Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (master_doc, 'Tusk Courses', 'Tusk Courses Documentation',
     author, 'Tusk Courses', 'One line description of project.',
     'Miscellaneous'),
]

# -- Extension configuration -------------------------------------------------
