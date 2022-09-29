# poium是一个基于Selenium/appium的Page Object测试库，最大的特点是简化了Page层元素的定义
from poium import Page, PageElement, PageElements


# 创建的页面类必须继承poium库中的Page类
class SomePage(Page):
    # poium支持8种定位方式
    elem_id = PageElement(id="id", timeout=5)
    # 通过timeout参数设置元素超时时间，默认为10秒
    elem_name = PageElement(name="name", describe="poium支持的name定位元素的方式")
    # describe参数无实际意义，只是增强元素定义的可读性，相当于注释
    elem_class = PageElement(class_name="class")
    elem_tag = PageElement(tag="input")
    elem_link_text = PageElement(link_text="this_is_link")
    elem_partial_link_text = PageElement(partial_link_text="is_link")
    elem_xpath = PageElement(xpath="//*[@id='id']")
    elem_css = PageElement(css="#id")
    some_element = PageElements(xpath='//div/a')
    # 使用PageElements类定位一组元素
