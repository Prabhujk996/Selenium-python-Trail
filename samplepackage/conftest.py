import pytest


@pytest.fixture(autouse=True,scope="function")
def setup_and_teardown():
    print("launch browser")
    print("open application URL in browser")
    yield
    print("logout from application")
    print("close browser")