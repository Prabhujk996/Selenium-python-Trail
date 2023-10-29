import pytest


@pytest.mark.smoke
def test_sample_one():
    print("inside sample_one")


@pytest.mark.regression
def test_sample_two():
    print("inside sample_two")
    assert False


@pytest.mark.regression
def test_sample_three():
    print("inside sample_three")
