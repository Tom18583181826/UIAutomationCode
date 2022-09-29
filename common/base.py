import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Base:
    def __init__(self, browser_type, url):
        # 方法与函数的区别是，方法的第一个参数必须声明，一般习惯是命名为“self”，
        # 但在调用这个方法时并不需要为该函数设置数值00
        if browser_type == "Chrome":
            self.wd = webdriver.Chrome()
        elif browser_type == "Firefox":
            self.wd = webdriver.Firefox()
        elif browser_type == "Edge":
            self.wd = webdriver.Edge()
        elif browser_type == "Opera":
            self.wd = webdriver.Opera()
        else:
            # Python可以使用raise抛出一个指定的异常
            raise TypeError("浏览器类型错误，请输入正确的浏览器类型！！！")
        # 进入网址
        self.wd.get(url)
        # 最大化窗口
        self.wd.maximize_window()

    # 进入网址
    def get(self, url):
        self.wd.get(url)

    # 最大化窗口
    def maximize_window(self):
        self.wd.maximize_window()

    # 元素定位，判断使用何种元素定位方法
    # 找不到元素的可能原因：
    # 1.登录前后，定位路径不一样
    # 2.元素值底层和看到的不一样
    # 3.页面是否有数据加载（等待）
    # 4.是否有窗口切换（句柄）
    # 5.iframe框架
    def selector_to_locator(self, selector):
        # selector:选择器        locator:定位器
        selector_type = selector.split(",")[0].strip()
        # 以逗号切割字符并将新切割得到的第一个字符赋值给选择器类型变量
        # strip()方法用于移除字符串头尾指定的字符(默认为空格或换行符)或字符序列
        selector_value = selector.split(",")[1].strip()
        if selector_type == "i" or selector_type == "ID":
            # HTML规定，id在HTML文档中必须是唯一的
            # 如果包含可变数字，就不要用id定位
            locator = (By.ID, selector_value)
        elif selector_type == "n" or selector_type == "NAME":
            # HTML规定，name用来指定元素名称
            # 如果包含可变数字，就不要使用name定位
            locator = (By.NAME, selector_value)
        elif selector_type == "tag" or selector_type == "TAG_NAME":
            # 通过元素的标签名来定位元素
            locator = (By.TAG_NAME, selector_value)
        elif selector_type == "class" or selector_type == "CLASS_NAME":
            # HTML规定，class用来指定元素的类名，class属性值如果有由空格隔开的多部分内容值，定位时可以选择其中的一部分值，也可以用点号或者逗号替代空格进行连接
            locator = (By.CLASS_NAME, selector_value)
        elif selector_type == "link" or selector_type == "LINK_TEXT":
            # 通过元素标签对之间的文字信息来定位元素
            locator = (By.LINK_TEXT, selector_value)
        elif selector_type == "plt" or selector_type == "PARTIAL_LINK_TEXT":
            # 通过元素标签对之间的部分文字（这部分文字需要唯一标识这个链接）定位元素
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_type == "x" or selector_type == "XPATH":
            locator = (By.XPATH, selector_value)
        elif selector_type == "css" or selector_type == "CSS_SELECTOR":
            locator = (By.CSS_SELECTOR, selector_value)
        else:
            raise TypeError(selector_type + "是无效的，请输入正确的定位方式！！！")
        return locator

    # 设置显式等待控制查找元素的时间---单个元素
    def locator_element(self, selector):
        locator = self.selector_to_locator(selector)
        # 调用元素定位方法，判断使用何种方法查找元素
        if locator is not None:
            element = WebDriverWait(self.wd, 10).until(EC.visibility_of_element_located(locator),
                                                       message="元素查找超时！！！")
        # WebDriverWait类是WebDriver提供的等待方法。WebDriverWait具体格式如下：
        # WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
        # 参数说明如下：
        #           driver:浏览器驱动
        #           timeout:最长超时时间，默认以秒为单位
        #           poll_frequency:检测的间隔(步长)时间，默认为0.5秒
        #           ignored_exceptions:超时后的异常信息，默认情况下抛出NoSuchElementException异常

        # until(method, message="")
        #           调用该方法提供的驱动程序作为一个参数，直到返回值为True。
        # 此处通过as关键字将expected_conditions重命名为EC，
        # 并调用expected_conditions类提供的visibility_of_element_located()方法判断元素是否可见
        # (可见代表元素非隐藏，并且长和宽都不等于0)
        else:
            raise ValueError("请输入有效的选择器选择目标元素！！！")
        return element

    # 设置显示等待来控制查找元素的时间---多个元素
    def locator_elements(self, selector):
        locator = self.selector_to_locator(selector)
        if locator is not None:
            elements = self.wd.find_elements(*locator)
            # 位置参数---在参数名之前使用1个星号，让函数接受任意多的位置参数
            # 关键字参数---在参数名之前使用2个星号，让函数支持任意多的关键字参数
        else:
            raise NameError("请输入有效的选择器选择目标元素！！！")
        return elements

    # 模拟按键输入
    def send_keys(self, selector, value):
        input_value = self.locator_element(selector)
        input_value.clear()
        # 清除文本
        input_value.send_keys(value)
        # 输入文本

    # 单击元素
    def click(self, selector):
        self.locator_element(selector).click()

    # 提交表单,有些搜索框不提供搜索按钮，而是通过键盘上的回车键完成搜索内容的提交。
    def submit(self, selector):
        self.locator_element(selector).submit()

    # 进入iframe框架
    def switch_to_frame(self, selector):
        frame_ele = self.locator_element(selector)
        self.wd.switch_to.frame(frame_ele)

    # 退到iframe框架的上一层
    def switch_to_parent_frame(self):
        self.wd.switch_to.parent_frame()

    # 退到iframe框架的最外层
    def switch_to_default_content(self):
        self.wd.switch_to.default_content()

    # 通过文本定位select下拉框选项
    def select_by_visible_text(self, selector, text):
        Select(self.locator_element(selector)).select_by_visible_text(text)

    # 通过下标索引定位select下拉框选项
    def select_by_index(self, selector, num):
        Select(self.locator_element(selector)).select_by_index(num)

    # 通过value值定位select下拉框选项
    def select_by_value(self, selector, value):
        Select(self.locator_element(selector)).select_by_value(value)

    # 二次定位，适用于有按钮选择的情况
    def second_locator_element(self, selector1, selector2):
        locator1 = self.selector_to_locator(selector1)
        locator2 = self.selector_to_locator(selector2)
        eles = self.wd.find_element(*locator1).find_elements(*locator2)
        random.choice(eles).click()

    # 获取元素的尺寸
    def get_element_size(self, selector):
        return self.locator_element(selector).size

    # 获取单个元素文本，可以用于断言
    def get_text(self, selector):
        return self.locator_element(selector).text

    # 获取多个元素文本
    def get_texts(self, selector):
        eles = self.locator_elements(selector)
        text_list = []
        # 存放文本数据的空列表
        for ele in eles:
            # 遍历元素每遍历出一个元素就获取它的文本并追加到列表中
            text = ele.text
            text_list.append(text)
        return text_list

    # 警告框处理
    def switch_to_alert(self, method):
        alert = self.wd.switch_to.alert
        # 使用switch_to.alert()方法定位警告框
        if method == "text":
            return alert.text
            # 返回alert,confirm,prompt中的文本信息
        if method == "accept":
            return alert.accept()
            # 接受现有警告框
        if method == "dismiss":
            return alert.dismiss()
            # 关闭现有警告框

    # 窗口截图
    def get_screenshot(self, filename):
        self.wd.save_screenshot(filename)

    # 退出浏览器进程
    def quit(self):
        self.wd.quit()

    # 关闭浏览器的某个窗口
    def close(self):
        self.wd.close()

    # 返回元素的属性值，可以是id,name等任意属性
    def get_attribute(self, selector, type_name):
        return self.locator_element(selector).get_attribute(type_name)

    # 返回元素是否可见，可见为True
    def get_is_displayed(self, selector):
        return self.locator_element(selector).is_displayed()

    # 获取当前页面的标题,可以用于断言
    def get_page_title(self):
        return self.wd.title

    # 获取当前页面的URL，可以用于断言
    def get_page_url(self):
        return self.wd.current_url

    # 普通文件上传：将本地文件路径作为一个值放在input标签中，通过form表单将值提交给服务器，
    #             对于通过input标签实现上传的情况，可以将其看作一个输入框，即通过send_key()指定本地文件路径的方式实现文件的上传；
    # 插件上传：基于Flash,JavaSeript,Ajax等技术实现文件的上传,
    #          可以使用AutoIt实现。
    def up_file(self, selector, up_file_path):
        return self.locator_element(selector).send_keys(up_file_path)

    # 文件下载,WebDriver允许我们设置默认的文件下载路径，不同的浏览器设置方式不同
    def download_file(self, browser_type, selector):
        if browser_type == "Chrome":
            chrome = webdriver.ChromeOptions
            # ChromeOptions是chromedriver支持的浏览器启动选项
            prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd()}
            # profile.default_content_settings.popups：设置为0表示禁止弹出下载窗口
            # download.default_directory：设置下载路径，使用os.getcwd()方法获取当前脚本的目录作为下载文件的保存位置
            chrome.add_experimental_option('prefs', prefs)
            # add_experimental_option：添加实验选项
            self.wd = webdriver.Chrome(chrome_options=chrome)
            self.locator_element(selector).click()
            # 定位文件下载按钮并点击
        elif browser_type == "Firefox":
            firefox = webdriver.FirefoxProfile()
            firefox.set_preference('browser.download.folderList', 2)
            # browser.download.folderList:设置为0，表示文件会下载到默认路径，设置为2，表示文件会下载到指定目录
            firefox.set_preference('browser.download.dir', os.getcwd())
            firefox.set_preference('browser.helperApps.neverAsk.saveToDisk', 'binary/octet-stream')
            # browser.helperApps.neverAsk.saveToDisk：指定要下载文件的类型，即Content-type值，
            # binary/octet-stream：表示二进制文件
            self.wd = webdriver.Firefox(firefox_profile=firefox)
            self.locator_element(selector).click()

    # 调用JavaScript，可以实现浏览器滚动条的拖动和textarea文本框的输入等操作
    def transfer_js(self, js, args=None):
        self.wd.execute_script(js, args)

    # 处理H5视频播放
    def video(self, selector, type):
        video = self.locator_element(selector)
        # 定位视频元素
        if type == "play":
            # 控制视频播放
            self.wd.execute_script("arguments[0].play()", video)
            # JavaScript有一个内置对象arguments包含了函数调用的参数数组，[0]表示取对象的第一个值
        elif type == "pause":
            # 控制视频暂停
            self.wd.execute_script("arguments[0].pause()", video)
        elif type == "load":
            # 控制视频加载
            self.wd.execute_script("arguments[0].load()", video)
        else:
            self.wd.execute_script("return arguments[0].currentSrc;", video)
            # currentSrc返回当前音频/视频的url,如果未设置音频/视频则返回空字符串
