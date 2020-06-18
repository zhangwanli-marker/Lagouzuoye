import pytest

from page import firtpage


class TestPage():
    testcase1 = firtpage.MainA()
    testcase1.gettext()


if __name__ == '__main__':
    pytest.mian(['-v', '-s', 'test_page.py'])
