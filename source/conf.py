# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'The Brasenose Wiki'
copyright = '2022, Brasenose Digital'
author = 'Brasenose Digital'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
html_logo = "_static/Brasenose.png"
html_title = "The Brasenose Wiki"
html_baseurl = "https://brasenose.college/wiki/"
html_css_files = [
    'font.css',
    'style.css',
]
html_theme_options = {
    "light_css_variables": {
        "font-stack": "'PT Serif', 'Merriweather', sans-serif",
        "font-stack--monospace": "Courier, monospace",
        "color-brand-primary": "#3277ae",
        "color-brand-content": "#3277ae",
    },
    "dark_css_variables": {
        "color-brand-primary": "#70a9d6",
        "color-brand-content": "#70a9d6",
    },
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
