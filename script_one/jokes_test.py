import pytest
from . import jokes

def test_fetchJoke():
    assert type(jokes.fetchJoke()) is str