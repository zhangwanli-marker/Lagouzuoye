import pytest
import yaml


class TestData:

    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("huunn.yaml")))
    def test_data(self, a, b):
        self.a = a
        self.b = b
        print(self.a + self.b)
