import os
from configparser import ConfigParser


# ConfigParser：是用来读取配置文件的的类库，配置文件的格式跟window下的ini配置文件类似，可以包含一个或多个节(section)
#               每个节可以有多个参数或称为选项(键=值)。使用配置文件的好处是不用把程序写死，可以使程序更加灵活。
# 常用函数方法：1.read(文件名)---读取配置文件，直接读取ini文件内容
#             2.sections()---读取ini文件内的所有节（section）,以列表形式返回
#             3.options(section)---获取指定节点下的所有选项（option）,以列表形式返回
class ReadIni:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # os.path.abspath(__file__):获取当前路径的绝对路径(包含文件名)，
        # os.path.abspath取决于os.getcwd, 如果是一个绝对路径，就返回，
        #                                如果不是绝对路径，根据编码执行 getcwd / getcwdu.
        #                                然后把path和当前工作路径连接起来
        # os.getcwdu() 方法用于返回一个当前工作目录的Unicode对象

        # Unicode对象(可以理解为一个python字符串)并没有编码。
        # 它们使用Unicode，一个一致的，通用的字符编码集。
        # 当你在Python中处理Unicode对象的时候，你可以直接将它们混合使用和互相匹配而不必去考虑编码细节。

        # os.path.dirname():获取当前文件的父目录名称

        self.config = ConfigParser()
        # 实例化一个config对象，使用该对象读取配置文件
        ini_file_path = os.path.join(self.base_path, r"data\read_ini.ini")
        # os.path.join():将多个路径组合后返回
        self.config.read(ini_file_path, encoding="utf-8")
        # 通过config对象使用read()方法直接读取ini文件对象

    # 获取日志文件路径
    def get_log_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "log_path"))
        # get(section,option):获取section(节)中option的值。返回为string类型

    # 获取测试报告路径
    def get_report_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "report_path"))

    # 获取截图路径
    def get_screenshot_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "screenshot_path"))

    # 获取csv文件路径
    def get_csv_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "csv_path"))

    # 获取excel文件路径
    def get_excel_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "excel_path"))

    # 获取sheet页名称
    def get_sheet_name(self):
        return self.config.get("Path", "sheet_name")

    # 获取json文件路径
    def get_json_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "json_path"))

    # 获取txt文件路径
    def get_txt_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "txt_path"))

    # 获取xml文件路径
    def get_xml_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "xml_path"))

    # 获取yaml文件路径
    def get_yaml_file_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "yaml_path"))

    # 保存登录页面截屏图片的路径
    def save_login_screenshot_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "login_screenshot_path"))

    # 保存登录的验证码图片的路径
    def save_verify_img_path(self):
        return os.path.join(self.base_path, self.config.get("Path", "verify_img_path"))


if __name__ == '__main__':
    read = ReadIni()
    print(read.get_log_file_path())
    print(read.get_report_file_path())
    print(read.get_screenshot_file_path())
    print(read.get_csv_file_path())
    print(read.get_excel_file_path())
    print(read.get_json_file_path())
    print(read.get_txt_file_path())
    print(read.get_xml_file_path())
    print(read.get_yaml_file_path())
    print(read.get_sheet_name())
    print(read.save_login_screenshot_path())
    print(read.save_verify_img_path())
