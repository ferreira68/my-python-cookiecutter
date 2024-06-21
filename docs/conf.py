"""Sphinx configuration."""
from datetime import datetime
import sphinx_theme_pd


project = "Hypermodern Python Cookiecutter"
author = "Antonio M. Ferreira, Ph.D."
copyright = f"{datetime.now().year}, {author}"
extensions = ["sphinx.ext.intersphinx", "sphinx.ext.napoleon", "myst_parser", "sphinx.ext.autodoc"]
intersphinx_mapping = {"mypy": ("https://mypy.readthedocs.io/en/stable/", None)}
language = "en"
html_theme = "sphinx_theme_pd"
html_theme_path = [sphinx_theme_pd.get_html_theme_path()]
html_logo = "_static/logo.png"
linkcheck_ignore = [
    "codeofconduct.html",
    "https://github.com/PyCQA/flake8-bugbear#",
    "https://github.com/peterjc/flake8-rst-docstrings#",
    "https://github.com/pre-commit/pre-commit-hooks#",
    "https://github.com/pycqa/pep8-naming#",
    "https://github.com/terrencepreilly/darglint#",
    "https://github.com/PyCQA/mccabe#",
    "https://github.com/cjolowicz/cookiecutter-hypermodern-python/releases/tag/",
    "https://cookiecutter-hypermodern-python.readthedocs.io",
    "https://badgen.net/badge/status/alpha/d8624d",
]
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
]