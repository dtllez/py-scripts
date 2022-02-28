import pytest
from . import wiki

def test_printDefinition():
    assert (wiki.printDefinition()) is str