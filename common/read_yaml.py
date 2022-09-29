# YAML是专门用来写配置文件的语言，是一种比XML和JSON更轻的文件格式，
# 也更简单和强大，它可以通过缩进来表示结构；
# PyYaml是Python的一个专门针对YAML文件操作的模块
import yaml

from common.read_ini import ReadIni


class ReadYaml:
    def read_yaml_data(self, file_path):
        with open(file_path, encoding="utf8") as file:
            # 1.使用open()方法打开文件，必须要使用close()方法关闭文件
            # 2.使用with open()方法可以不用close()方法关闭文件，无论在文件使用中遇到什么问题都能安全的退出，
            #   即使发生错误，退出运行环境时也能安全退出文件并给出报错信息。
            return yaml.safe_load(file)
            # load()可以轻易的调用任何python函数，可能会从yaml文件中读取到一些恶意代码，从而使程序变得不安全，
            # 为了保证程序的安全性，所以使用safe_load()来安全的加载子集


if __name__ == '__main__':
    read_ini = ReadIni()
    yamlpath = read_ini.get_yaml_file_path()
    read_yaml = ReadYaml()
    yaml_data = read_yaml.read_yaml_data(yamlpath)
    print(yaml_data)
