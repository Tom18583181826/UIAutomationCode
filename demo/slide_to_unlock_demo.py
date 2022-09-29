from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
# 在WebDriver中，与鼠标操作相关的方法都封装在ActionChains中
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException


class SlideToUnlock:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("")

    def slide_to_unlock(self):
        slider = self.driver.find_element(By.ID, "")
        # 定位滑动块
        action = ActionChains(self.driver)
        # 调用ActionChains类，把浏览器驱动作为参数传入
        action.click_and_hold(slider).perform()
        # click_and_hold()：单击并按下鼠标左键
        # perform()：提交所有ActionChains类中存储的行为，鼠标的动作都要用perform()方法来调用才会被执行

        for index in range(200):
            try:
                action.move_by_offset(2, 0).perform()
                # move_by_offset():移动鼠标，第一个参数为x坐标距离，第二个参数为y坐标距离

                # action = webdriver.TouchActions(self.driver)
                # action.scroll_from_element(on_element, xoffset, yoffset)
                # TouchActions类中的scroll_from_element()方法也可以实现滑动元素
                # on_element：滑动的元素
                # xoffset：x坐标距离
                # yoffset：y坐标距离
            except UnexpectedAlertPresentException:
                break
            action.reset_actions()
            # reset_actions()：重置action
            sleep(0.1)

# 鼠标操作常用方法
# context_click():右击
# double_click():双击
# drag_and_drop():拖动
# move_to_element():鼠标悬停
