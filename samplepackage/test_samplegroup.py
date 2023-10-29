import pytest

@pytest.mark.smoke
def test_sample_one():
    print("inside sample one")


@pytest.mark.regression
def test_sample_two():
    print("inside sample two")


@pytest.mark.sanity
def test_sample_three():
    print("inside sample three")


@pytest.mark.smoke
def test_sample_four():
    print("inside sample four")

