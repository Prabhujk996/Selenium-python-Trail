import pytest


@pytest.mark.parametrize("username,password",[("prabhu","1234"),("prabha","12344"),("babji","11234")])
def test_sample_one(username,password):
    print(username+"-"+password)


