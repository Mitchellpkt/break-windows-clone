"""
Tests can give a false sense of security. All of these tests will pass on any operating system (including Windows)
because none of them reference the file with the malformed name. In many repositories, the test only cover the code
within the repo, without checking whether the repo itself can be cloned (excluding DevOps / IaC repos)
"""

import pytest

def test_that_passes_on_any_os():
    assert True

def test_another():
    assert 1 == 1

def test_this_coverage_looks_great():
    assert not False