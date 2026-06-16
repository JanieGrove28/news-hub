# Configuration file for the Sphinx documentation builder.

import os
import sys
import django

# -- Project information -----------------------------------------------------

project = 'News Hub'
copyright = '2026, Janie'
author = 'Janie'

# -- Add project to path -----------------------------------------------------

sys.path.insert(0, os.path.abspath('../../..'))

# Django setup
os.environ['DJANGO_SETTINGS_MODULE'] = 'news_project.settings'
django.setup()

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output -------------------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']