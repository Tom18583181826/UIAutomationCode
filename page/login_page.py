# Page Object的设计思想是把元素定位与元素操作进行分层
from time import sleep
from common.base import Base
from common.read_ini import ReadIni
from common.read_yaml import ReadYaml


class LoginPage(Base):
    read_ini = ReadIni()
    read_path = read_ini.get_yaml_file_path()
    read_yaml = ReadYaml()
    yaml_data = read_yaml.read_yaml_data(read_path)

    def login(self, username, password, verify_code):
        # 点击账号登录
        self.click(self.yaml_data["Login"]["ACCOUNTLOGIN"])
        # 输入用户名
        self.send_keys(self.yaml_data["Login"]["USERNAME"], username)
        # 输入密码
        self.send_keys(self.yaml_data["Login"]["PWD"], password)
        # 输入验证码
        self.send_keys(self.yaml_data["Login"]["VERIFY"], verify_code)
        # 点击登录按钮
        self.click(self.yaml_data["Login"]["SUBMIT"])
        sleep(10)

    # 登录成功后的操作
    def get_success(self):
        # # 点击个人中心
        # self.click(self.yamldata["Login"]["USERBUTTON"])
        # # 获取当前所有句柄
        # handles = self.wd.window_handles
        # # 进入第二个窗口句柄
        # self.wd.switch_to.window(handles[1])
        # 获取成功文本
        success_text = self.get_text(self.yaml_data["Login"]["SUCCESSTEXT"])
        return success_text

    # 获取登录失败后的文本提示
    def get_failed_text(self):
        return self.get_text(self.yaml_data["Login"]["FAILED"])


if __name__ == '__main__':
    logintest = LoginPage('Chrome', "https://vmall.vmall888.com")
    logintest.login("9527", "a123456", "1111")
