# 这是版本2号。ini和方法工具类都是在一个文件夹下的
# 先导包。os路径和 configparser读取ini文件的包
from configparser import ConfigParser
import os
class ParserConf():
    # 定义一个int私有方法。供内部默认调用。
    def __int__(self, filename):
        self.conf = ConfigParser(allow_no_value=True, delimiters='=')
        self.confile = os.path.join(os.getcwd(), filename)
        if os.path.exists(self.confile):
            self.conf.read(self.confile, encoding='utf-8')
        else:
            print('不存在' + filename + '文件')

    def get_config_value_by_key(self, section, key):

        if self.conf.has_option(section, key):
            return self.conf.get(section, key)

    def get_all_sections_from_config_file(self):
        print(self.conf.sections())

    def update_value_by_section_and_key(
            self, section_name, key, key_value):
        self.conf.set(section_name, key, key_value)
        self.conf.write(open(self.confile, "w"))

    def get_section_value(self, section):
        value = self.conf.items(section)
        return value


if __name__ == '__main__':
    ParserConf("D:\demo\env\dev\config.ini").get_all_sections_from_config_file()
