# 这个文件用来封装类方法名来运行httprunner
# 先导包
from httprunner.api import HttpRunner

# 继承运行的类， 设置runner变量用等号接收
runner = HttpRunner(failfast=False)

# 用类runner点run（"yml路径"）运行对应的yml文件测试套件或者测试用例
# 测试一下webhook有没有用啊

runner.run('testsuites/demo_testsuite_c.yml')
