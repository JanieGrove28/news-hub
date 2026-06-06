# Configuration file for the Sphinx documentation builder.

import os
import sys
import django

# -- Project information -----------------------------------------------------

project = 'News Hub'
copyright = '2026, Janie'
author = 'Janie'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Django setup (IMPORTANT FOR CAPSTONE) ----------------------------------

sys.path.insert(0, os.path.abspath('..'))

# IMPORTANT: replace with your actual Django project name
os.environ['DJANGO_SETTINGS_MODULE'] = 'news_project.settings'

django.setup()