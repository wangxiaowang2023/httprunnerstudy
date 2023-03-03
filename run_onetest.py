# 这是对某一个接口的调试，右键就可以快速运行。
# 先导包
from httprunner.api import HttpRunner

# 再用等号继承封装的类

runner = HttpRunner(failfast=False)

# 再用继承的类用点去调用方法去运行,括号里面直接放运行文件的路径就可以

# runner.run('testsuites/demo_testsuite_onetest.yml')
runner.run('testsuites/demo_testsuite_onetest.yml')