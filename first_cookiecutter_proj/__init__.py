"""
amirayu_temp
This is a f first cookiecutter test
"""

# Add imports here
from .first_cookiecutter_proj import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
