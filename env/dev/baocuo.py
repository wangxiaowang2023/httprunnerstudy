# 这是版本2号。ini和方法工具类都是在一个文件夹下的
# 先导包。os路径和 configparser读取ini文件的包
from configparser import ConfigParser
import os


class ParserConf():  # 创建一个类，名字和configparser重复，注意大小写。这个类是来读取ini配置文件的
    # 定义一个int私有方法。供内部默认调用。
    def __init__(self, filename):
        self.conf = ConfigParser(allow_no_value=True, delimiters='=')
        # self.confile = os.path.join(os.getcwd(), config_path)
        self.confile = os.path.join(os.getcwd(), filename)
        if os.path.exists(self.confile):
            self.conf.read(self.confile, encoding='utf-8')
        else:
            print('不存在' + filename + '文件')
        # 先调出configparser里面的ConfigParser类用config去接收它，创建类config，前面加self表示自己的
        # 定位文件的位置，用os的path的dirname,dirname就是打印当前文件夹名称
        # os.path.realpath(__file__)获取当前执行脚本的绝对路径，os的sep表示是‘/’  file_name需要传参进来，表示文件名
        # config_path = os.path.dirname(
        #     os.path.realpath(__file__)) + os.sep + "config.ini"  # os.path.realpath当前目录，os.sep是斜杠\ file_name是传进来的文件名，
        # self.config.read(self.confile, encoding="utf-8")  # 调用自己的config方法去read读取config_path路径文件 中文编码

    def get_config_value_by_key(self, section, key):
        # self.conf.read(self.confile, encoding="utf-8")
        # 获取指定的section, 指定的option的值
        if self.conf.has_option(section, key):
            return self.conf.get(section, key)
        # print('获取%s 节点，%s 的值为 %s' % (section, key, key_value)))

    def get_all_sections_from_config_file(self):  # 读取所获得的sections列表节点
        print(self.conf.sections())

    def update_value_by_section_and_key(
            self, section_name, key, key_value):
        self.conf.set(section_name, key, key_value)
        self.conf.write(open(self.confile, "w"))

    def get_section_value(self, section):
        value = self.conf.items(section)
        return value

    # def get_option(self, _option=None):  # 获取选项
    #     sections = self.config.sections(0)  # 创建sections类。等下获取所有sections
    #     for i in sections:
    #         if self.config.has_option(i, _option):
    #             return self.config.get(i, _option)

    # def get_specified_option(self, section, option=None):
    #     return self.config.get(section, option)


# class DB:  # 创建数据库的类
#     def __int__(self):   # 创建私有属性
#         cf = configparser.ConfigRead


if __name__ == '__main__':
    ParserConf("D:\demo\env\dev\config.ini").get_all_sections_from_config_file()
