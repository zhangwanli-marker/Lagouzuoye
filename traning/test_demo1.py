import pytest
import yaml


class TestData:
    # with open('listdata.yaml', 'rb') as f:
    #     data = yaml.safe_load(f)

    @pytest.mark.parametrize("a, b", yaml.safe_load(open("./listdata.yaml")))
    def test_data(self, a, b):
        c = a + b
        print(c)
