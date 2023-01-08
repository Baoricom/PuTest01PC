import pytest


@pytest.fixture(scope="class")
def setup():
    print("I'l be running first")
#this part for open browser etc
    yield
    print("I'l be running last")