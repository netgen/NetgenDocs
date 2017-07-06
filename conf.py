# -*- coding: utf-8 -*-

import sys, os
import sphinx_rtd_theme

from datetime import datetime

extensions = ['sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig']

source_suffix = '.rst'
master_doc = 'index'

project = 'Netgen Docs'
copyright = 'Netgen'
author = 'Netgen'

version = ''
release = ''

exclude_patterns = ['_build']

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_static_path = ['_static']
templates_path = ['_templates']

html_theme_options = {
    'collapse_navigation': True,
    'display_version': True,
    'navigation_depth': 2,
}

html_context = {
    'copyright_url': 'http://www.netgenlabs.com',
    'current_year': datetime.utcnow().year
}

def setup(app):
    app.add_stylesheet("css/style.css")
