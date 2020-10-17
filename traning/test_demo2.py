import pytest


def setup_module():
    print("模块级别的的setup")
def teardown_module():
    print("模块级别的teardown")

def setup_function():
    print("方法级别的setup")
def teardown_function():
    print("方法级别的teardown")

def test_case1():
    print("外部函数1")

class Testclass:
    # @pytest.mark.parametrize("env", yaml.safe_load(open('mydata.yaml')))
    # def test_env(self, env):
    #     if "test" in env:
    #         print("这是测试环境")
    #         print(f'测试环境的ip是：{env["test"]}')
    def setup(self):
        print("默认是函数内部的")
    def teardown(self):
        print("这是内部函数的teardown")
    def setup_class(self):
        print("这是一个class级别的setup")
    def teardown_class(self):
        print("这是一个class级别的teardown")

    def setup_method(self):
        print("这是一个method  setup")
    def teardown_method(self):
        print("这是一个method  teardown")

    def test_case2(self):
        print("这是一个内部方法")

    @pytest.mark.add


     
