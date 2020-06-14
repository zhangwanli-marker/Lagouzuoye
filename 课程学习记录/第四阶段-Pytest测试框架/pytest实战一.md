参考链接
https://docs.pytest.org/en/stable/ 3

注意
起名字，类，包或者方法，都最好不要起关键字的名字，比如 os,sys, http , appium, selenium

自动化测试用例的设计基本原则
变动小，尽量页面不要经常变动
每条测试用例尽量简单，尽量去覆盖一个基本的功能
尽量不要有关联关系
pytest介绍
pytest测试用例的识别、运行
pytest 框架结构
import pytest 类似的setup,teardown同样更灵活，
模块级(setup_module/teardown_module)模块始末，全局的（ 优先最高 ）
函数级(setup_function/teardown_function)只对函数用例生效(不在类中)
类级(setup_class/teardown_class)只在类中前后运行一次（在类中）
方法级(setup_method/teardown_methond)开始于方法始末（在类中）
类里面的（setup/teardown）运行在调用方法的前后
Pytest 常用参数解析
pytest/py.test [包名] 执行包下所有的用例
pytest -v 打印详细运行日志信息
pytest -s s是带控制台输出结果，也是输出详细
pytest -k "add” 匹配所有名称中包含add的用例，可以使用 and ,or , not等逻辑运算
pytest -m [标记名] @pytest.mark.[标记名] 将运行有这个标记的测试用例
pytest -x 文件名 一旦运行到报错就停止 运行
pytest - -maxfail=[num] 当运行错误达到num的时候就停止 运行
pytest 文件名.py 执行单独一个pytest模块
pytest 文件名.py::类名 运行某个模块里面某个类
pytest 文件名.py::类名::方法名 运行某个模块里面某个类里面的方法
–collect-only 给定配置下显示那些用例会运行只收集用例，而不执行
–junitxml=path 生成执行结果xml文件
–setup-show 回溯fixture的执行过程

Pytest fixture 用法
fixture 用法
Fixture 是为了测试⽤例的执⾏，初始化⼀些数据和⽅法
实现了 unittest ⾥面的 setUp, tearDown 功能，但⽐ setUp, tearDown 更灵活
直接通过函数名字调⽤或usefixtures
允许使用多个fixture
使用 autouse，如果要返回值，需要传fixture函数名
-setup-show 回溯 fixture 的执行过程
fixture 作用域
fixture 里面有一个参数 scope，通过 scope 可以控制 fixture 的作用范围，根据作用范围大小划分：session> module> class> function，具体作用范围如下：
function 函数或者方法级别都会被调用
class 类级别调用一次
module 模块级别调用一次
session 是多个文件调用一次(可以跨.py文件调用，每个.py文件就是module)
conftest.py 用法
conftest.py配置需要注意:
conftest.py文件名是不能换的
conftest.py与运行的用例要在同一个package下，并且有__init__.py文件
不需要import导入conftest.py，pytest用例会自动查找
所有同目录测试文件运行前都会执行conftest.py文件
全局的配置和前期工作都可以写在这里，放在某个包下，就是这 个包数据共享的地方。
如果不同层级的包下都有conftest.py文件，那么内层目录的conftest.py文件中的方法会覆盖外部的conftest.py文件中的方法（重名的方法）