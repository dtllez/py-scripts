import pytest
from . import sum

def test_sumAdd():
    assert sum.add(4, 8) == 12

