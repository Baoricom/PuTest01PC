import pytest

@pytest.mark.usefixtures("setup")
class Testexample:

    def test_fixturedemo(self):
        print("Hello middle")


    def test_fixturedemo1(self):
        print("Hello middle1")


    def test_fixturedemo2(self):
        print("Hello middle2")


    def test_fixturedemo3(self):
        print("Hello middle3")
