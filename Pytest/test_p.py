# Any pytest file should start from test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method name execution, -s logs in output, -v stands for more info metadata
# you can run specific file with py.test <filename>
# you can mark (tag) tests @pytest.mark.smoke and then run this with -m key
# you can skip test by @pytest.mark.skip
# @pytest.mark.xfail
# fixtures are used as setup and tear down methods for test cases - conftest.py file to generalize fixtures
# and make it available to all test cases


import pytest


@pytest.mark.sector
def test_first():
    print("Hello")


# assert "Hi" == test_first


# this part for close browser etc
def test_fixture(setup):
    print("I'l be running second")
