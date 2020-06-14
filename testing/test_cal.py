from testing.cal import Cal


class TestCal:
    def test_add1(self):
        cal = Cal()
        assert 3 == cal.add(1, 2)

    def test_add2(self):
        cal = Cal()
        assert 300 == cal.add(100, 200)

    def test_div(self):
        cal = Cal()
        assert 1 == cal.div(1, 1)


