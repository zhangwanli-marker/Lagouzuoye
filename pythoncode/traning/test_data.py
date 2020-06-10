import pytest
import yaml


class TestData:
    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open()))
    def test_data(self, a, b):
        print(a + b)
