"""
Unit and regression test for the first_cookiecutter_proj package.
"""

# Import package, test suite, and other packages as needed
import first_cookiecutter_proj
import pytest
import sys

def test_first_cookiecutter_proj_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "first_cookiecutter_proj" in sys.modules
def test_one_plus_one():
    a = 1
    b = 1
    assert a+b==2
