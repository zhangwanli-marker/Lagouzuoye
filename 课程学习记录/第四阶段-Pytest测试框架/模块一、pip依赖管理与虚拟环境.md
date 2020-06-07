#模块一、pip依赖管理与虚拟环境
 ##1.pip介绍
pypi托管了大量非常流行的库（www.py/pi.org）
###.pip命令
    .pip help 帮助
	.pip install 安装 pip install 包名==版本号
	    实例：pip install selenium==3.8.0
	.pip install -U 包名 升级包
	.pip uninstall 卸载
	.pip list 列出所有的包文件
	.pipdownload下载包，手动安装
	.pip search requests 搜索包
	.pip install -i 镜像地址 --trusted-host 镜像地址对应的host
	    .举例：pip2 install jupter -i http:pypi.douban.com/simple/ --trusted-host pypi.douban.com
	国内的pip源
	    .阿里云：http://mirrors.aliyun.com/pypi/simple
	    .清华：http://pypi.tuna.tstinghua.edu.cn/simple
	    .豆瓣:：http://pypi.douban.com/simple
###虚拟环境创建
    .创建虚拟环境：python -m venv 虚拟环境名称
    .激活虚拟环境：tutorail-env\Scripts\activate.bat 激活
    .退出虚拟环境：deactivate.bat
    .删除虚拟环境 rm-rf 虚拟环境名
    .pycharm创建虚拟环境
        继承全局包
		