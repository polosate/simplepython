from nose import *
from hamcrest import assert_that, equal_to

x = 0


def setup_func():
    global x
    x += 3


def test_3():
    assert_that(x, equal_to(0))


@with_setup(setup_func)
def test_4():
    assert_that(x, equal_to(3))


class TestX:

    def setup(self):
        global x
        x += 5

    def teardown(self):
        global x
        x = 0

    def test_1(self):
        assert_that(x, equal_to(5))

    def test_2(self):
        assert_that(x, equal_to(5))
