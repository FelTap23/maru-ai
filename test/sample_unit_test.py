import pytest

@pytest.fixture
def name():
    return "Luis"

@pytest.fixture
def last_name():
    return "Tapia"

def test_one(name, last_name):
    assert 1 == 1

def test_two():
    assert 1 == 1


def test_three():
    assert 1 == 1