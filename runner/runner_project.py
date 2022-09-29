import time
import unittest
from common.send_mail import SendMail
from common.read_ini import ReadIni
from BeautifulReport import BeautifulReport


class RunnerProject:
    def runner(self):
        # 测试用例目录
        test_dir = r"J:\代码示例\UIAutomationCode\UIAutomationTest\case"
        # 加载测试用例
        discover = unittest.defaultTestLoader.discover(test_dir, "login_test.py")
        # discover()可以从多个文件中查找测试用例.
        # discover(start_dir, pattern="test*.py", top_level_dir=None)
        # 参数说明:
        #           start_dir:待测试的模块名或测试用例目录
        #           pattern = "test*.py":测试用例文件名的匹配原则
        #           top_level_dir = None:测试模块的顶层目录,如果没有顶层目录默认为空
        # 注:1.discover()方法和main()方法执行测试用例的顺序默认根据ASCII码的顺序进行.对于测试目录和测试文件同样适用
        #             在声明测试套件TestSuite类,可以通过addTest()方法按照一定顺序来加载测试用例
        #    2.查找多级目录的测试用例:可以在每个子目录下放一个__init__.py文件
        #         __init__.py的作用:将一个目录标记成一个标准的Python模块

        # 获取系统当前时间
        nowtime = time.strftime("%Y_%m_%d_%H_%M")
        # time.strftime():用于获取当前时间，可以将时间格式化为字符串
        # time.time():获取当前时间戳
        # time.ctime():当前时间的字符串形式
        # time.localtime():当前时间的struct_time形式

        # 设置测试报告路径
        report_path = ReadIni().get_report_file_path()

        report = BeautifulReport(discover)
        report.report(filename="report{}".format(nowtime),
                      description="使用BeautifulReport模板生成测试报告",
                      report_dir=report_path,
                      theme="theme_memories")

        # 发送测试报告至邮箱
        sendmail = SendMail()
        sendmail.send_mail(report_path + "report{}.html".format(nowtime))


if __name__ == '__main__':
    runner = RunnerProject()
    runner.runner()
