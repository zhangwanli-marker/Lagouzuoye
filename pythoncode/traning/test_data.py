import pytest
import yaml


class TestData:
    @pytest.mark.parametrize("a", yaml.safe_load(open("./huunn.yaml")))
    def test_data(self,  a):
        print(a)
