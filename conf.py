# -*- coding: utf-8 -*-

import sys, os
import sphinx_rtd_theme

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig']

source_suffix = '.rst'
master_doc = 'index'

project = 'Netgen Docs'
copyright = '2017, Netgen'
author = 'Netgen'

version = ''
release = ''

exclude_patterns = ['_build']

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# html_static_path = ['_static']
# templates_path = ['_templates']

html_theme_options = {
    'collapse_navigation': True,
    'display_version': True,
    'navigation_depth': 2,
}
