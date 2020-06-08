#模块三、Pytest测试框架

##1.pytest介绍
###1.1pytest是一个非常承受的全功能的Python测试框架
        .简单灵活，容易上手；
        .支持参数化
        .测试用例的skip和xfail,字段失败充实等处理
        .能够支持简单的单元测试好复杂的功能测试，还可以用来做selenium/appium等自动化测试和接口自动化测试（Pytest+Requests）
        .Pytest有很多第三方插件、并且可以自定义扩展，比较耗油的如pytest-allure(完美测试报告生成)、pytest-xdist(多CPU分发)等
        .可以很好的和jenkins集成
###1.2.文档：https//docs.pytest.org/en/lastest/contents.html#toc
###1.3.第三方库：https://pypi.org/search/?q=pytest

##2.pytest对测试用例的识别与运行
###2.1.测试文件
    .test_*.py  以test_开头的py文件
    .*_test.py  以_test.py结尾的py文件
###2.2.对测试用例识别
    .Test*类包含的缩影test_*的方法（测试类不能带有__init__()方法)
    .不在class中的缩影的test_*方法
 
###2.3.pytest也可以执行unittest框架写的用例和方法

##3.p###ytest的安装
    .pip install pytest
    .pip install -U pytest
##unittest框架介绍
##3.pytest实战
    测试用例的运行方式
        3.1.pytest解释器
        3.2.Python解释器---增加一个入口函数，或者定义一个class类（）不带__init__()方法
        if __name__=="main":
            pytest.main(['test_a.py])'
            pytest.main(['test_a.py::TestDemo','-v'])
         3.pytest -k '表达式' -v
            pytest -k 'test_a or test_b' -v
##4.参数化
    @pytest.mark.parametriz('a,b',[(10,20),(1,1),(1,2)])

