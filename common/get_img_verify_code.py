import json
import requests
import pytesseract
from PIL import Image
from time import sleep
# from jsonpath_ng import parse
from selenium import webdriver
from common.read_ini import ReadIni


class GetImgVerifyCode:
    def __init__(self):
        # 登录页面图片保存路径
        self.login_screenshot_path = ReadIni().save_login_screenshot_path()
        # 保存验证码截图路径
        self.verify_img_path = ReadIni().save_verify_img_path()

    def get_verify_img(self):
        driver = webdriver.Chrome()
        driver.get("https://vmall.vmall888.com")
        driver.maximize_window()
        sleep(3)

        # 保存登录页面截图
        driver.save_screenshot(self.login_screenshot_path)
        # 定位验证码图片
        location_img = driver.find_element_by_class_name("yanmimg").location
        # 获取图片上边的坐标
        top = location_img["y"]
        # 获取图片元素，用于获取图片的高和宽数据
        img = driver.find_element_by_class_name("yanmimg")
        # 获取图片下边的坐标
        down = top + img.size["height"]
        # 获取图片左边的坐标
        left = location_img["x"]
        # 获取图片右边的坐标
        right = left + img.size["width"]
        # 打开登录页面截图
        openimg = Image.open(self.login_screenshot_path)
        # 获取验证码图片截图
        verify_img = openimg.crop((left, top, right, down))
        # 保存验证码图片
        verify_img.save(self.verify_img_path)
        driver.quit()

    # 通过接口获取验证码图片并识别验证码
    def get_verify_code(self):
        img_url = "http://fmcontrolcenter.sclonsee.com/backendapi/v1/site/img-verify"
        result = requests.get(url=img_url)
        verify_img_path = ReadIni().save_verify_img_path()
        with open(verify_img_path, "wb") as img_file:
            img_file.write(result.content)
        text = pytesseract.image_to_string(Image.open(verify_img_path))
        return text.strip()

    def write_verify_to_params(self, file_path):
        with open(file_path, encoding="utf8") as file:
            json_data = json.loads(file.read())
        # 构造指定jsonpath模式对应的解析器
        # parser = parse("ParamsSuccess[*].verify_code")
        verify_code = self.get_verify_code()
        # parser.update(json_data, verify_code)
        # return json_data


if __name__ == '__main__':
    read_ini = ReadIni()
    json_path = read_ini.get_json_file_path()
    test = GetImgVerifyCode().write_verify_to_params(json_path)
    print(test)
