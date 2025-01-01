#!/usr/bin/env python

from datetime import datetime

# -- Project information -----------------------------------------------------
project = 'idsc-suite'
author = 'Mingze Dong'
copyright = f"{datetime.now():%Y}, {author}."

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosummary",
    "sphinx_copybutton",
    "sphinx_design",
]

# Basic settings
templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
]

# Notebook execution settings
nbsphinx_execute = "never"

# Language settings
language = "en"

# -- Options for HTML output -------------------------------------------
html_theme = "furo"
html_title = "idsc-suite"

# Theme options
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#003262",
        "color-brand-content": "#003262",
    },
}

html_static_path = ["_static"]
html_show_sphinx = False
