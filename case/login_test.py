import time
import unittest
# 1.unittest单元测试框架创建的测试类必须继承unittest.TestCase类
# 2.测试用例（方法）必须以“test”开头，后面可以跟字母、数字、下划线
from parameterized import parameterized
from common.get_log import GetLog
from common.read_excel import ReadExcel
from common.read_ini import ReadIni
from page.login_page import LoginPage


# 获取登录成功用例的数据
def get_success_data():
    read = ReadExcel()
    success_list = []
    for row in range(2, 3):
        case_id = read.get_case_id(row)
        case_name = read.get_case_name(row)
        params = read.get_case_params_value(row)
        expect = read.get_case_expect_value(row)
        success_list.append((case_id, case_name, params, expect))
    return success_list


# 获取登录失败用例的数据
def get_failed_data():
    read = ReadExcel()
    failed_list = []
    for row in range(3, read.get_row_count() + 1):
        case_id = read.get_case_id(row)
        case_name = read.get_case_name(row)
        params = read.get_case_params_value(row)
        expect = read.get_case_expect_value(row)
        failed_list.append((case_id, case_name, params, expect))
    return failed_list


# 在unittest单元测试框架，测试类必须继承unittest模块的TestCase类
class BaiDuLoginTest(unittest.TestCase):
    # 获取当前系统时间
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S")

    # 在每条测试用例之前执行
    def setUp(self):
        # setup()方法用于测试用例执行前的初始化工作，例如：初始化变量，生成数据库测试数据，打开浏览器等
        self.login_test = LoginPage("Chrome", "https://vmall.vmall888.com")

    # 在每条测试用例之后执行
    def tearDown(self):
        # tearDown()方法用于测试用例执行之后的善后工作，例如：清除数据库测试数据，关闭文件，关闭浏览器等
        self.login_test.quit()

    # 测试登录成功的用例
    @parameterized.expand(get_success_data())
    # @parameterized.expand:传入的参数为元组的列表
    # 在unittest单元测试框架，测试方法必须以“test”开头
    def test_success(self, case_id, case_name, params, expect):
        # try之后为执行的代码
        try:
            # 异常的抛出机制：
            # 1.如果在运行时发生异常，那么解释器会查找相应的处理语句(称为handler)
            # 2.如果在当前函数里没有找到相应的处理语句，那么解释器会将异常传递给上层的调用函数，看看哪里能不能处理
            # 3.如果在最外层函数(全局函数main())也没有找到，那么解释器会退出，同时打印Traceback(回溯)，以便用户找到错误产生的原因
            username = params["username"]
            password = params["password"]
            verify_code = params["verify_code"]
            self.login_test.login(username, password, verify_code)
            success_text = self.login_test.get_success()
            self.assertEqual(expect, success_text, "预期结果与实际结果不一致！")
        # except之后为发生异常时执行的代码
        except AssertionError:
            # 用例执行失败执行截图操作
            self.login_test.get_screenshot(
                ReadIni().get_screenshot_file_path() + "screenshot_{}.png".format(self.now_time))
            # 实例化打印日志对象
            log_obj = GetLog().get_log(ReadIni().get_log_file_path() + "login{}.log".format(self.now_time))
            # 打印日志
            log_obj.error("用例{}---{}---执行失败！".format(case_id, case_name))
            # 使用raise抛出一个指定异常
            # raise只能使用Python提供的异常类，如果想要raise使用自定义异常类，则自定义异常类需要继承Exception类
            raise AssertionError("用例{}---{}---执行失败！".format(case_id, case_name))
        # finally之后为不管有没有异常都会执行的代码
        finally:
            # pass为空语句，是为了保持程序结构的完整性，不做任何事情，一般用作占位语句
            pass

    # 测试登陆失败的用例
    @parameterized.expand(get_failed_data())
    # @unittest.skip("该装饰用于直接跳过测试")
    # @unittest.skipIf(3>2, "该装饰用于当条件为真时,跳过测试")
    # @unittest.skipUnless(3>2, "该装饰用于当条件为真时,执行测试")
    # @unittest.expectedFailure   该装饰用于不管执行结果是否失败,都将测试结果标记为失败,但不会抛出失败信息
    def test_fail(self, case_id, case_name, params, expect):
        try:
            username = params["username"]
            password = params["password"]
            verify_code = params["verify_code"]
            self.login_test.login(username, password, verify_code)
            fail_text = self.login_test.get_failed_text()
            self.assertEqual(expect, fail_text, "预期结果与实际结果不一致！")
        except AssertionError:
            # 用例执行失败执行截图操作
            self.login_test.get_screenshot(
                ReadIni().get_screenshot_file_path() + "screenshot_{}.png".format(self.now_time))
            # 实例化打印日志对象
            log_obj = GetLog().get_log(ReadIni().get_log_file_path() + "login{}.log".format(self.now_time))
            # 打印日志
            log_obj.error("用例{}---{}---执行失败！".format(case_id, case_name))
            # 使用raise抛出一个指定异常
            raise AssertionError("用例{}---{}---执行失败！".format(case_id, case_name))
        finally:
            # 有时候，我们希望不管是否出现异常，有些操作都会被执行，例如：文件的关闭，锁的释放，把数据库链接返回给连接池等
            # 这时，可以使用try...except...finally语句
            pass


if __name__ == '__main__':
    # "if __name__ == '__main__'："表示当模块被直接运行时，下面的代码块将被运行；
    # 当模块被其他程序文件调用时，下面的代码块不被运行
    unittest.main(verbosity=2)
    # verbosity = 2:输出更详细的执行日志

    # .:表示一条运行通过的测试用例
    # F:表示一条运行失败的测试用例
    # E:表示一条运行错误的测试用例
    # S:表示一条运行跳过的测试用例

    # unittest单元测试框架：
    # 1.Test Case(测试用例)是最小的测试单元，用于检查特定输入集合的特定返回值。
    #                       unittest提供了TestCase基类，自己创建的测试类必须继承该类，它可以用于创建新的测试类。
    # 2.Test Suite(测试套件)是测试用例，测试套件或两者的集合，用于组装一组要运行的测试。
    #                       unittest提供了TestSuite类来创建测试套件。
    #         注:测试用例的执行顺序可以由测试套件的添加顺序控制
    # 3.Test Runner(测试运行器)用于协调测试的执行并向用户提供结果。
    # 4.Test Fixture(测试固件)用于执行测试所需的环境准备，以及关联的清理动作.
    #                       例如:创建临时或代理数据库,目录或启动服务器进程等.
    #
    #           setUpModule/tearDownModule:在整个模块的开始与结束时被执行。
    #           setUpClass/tearDownClass:在测试类的开始与结束时被执行
    #           注：setUpClass/tearDownClass为类方法，需要通过@classmethod进行装饰。
    #               另外，方法的参数为cls.其实cls与self并没有什么本质区别，都只表示方法的第一个参数
    #           setUp/tearDown:在测试用例的开始与结束时被执行

    #           指定范围内共享：Fixture里面有一个参数scope,通过scope可以控制fixture的作用范围，
    #           根据作用大小划分：session>module>class>function
    #           function:函数或方法级别都会被调用一次
    #           class：类级别
    #           module:模块级别
    #           session:多个文件调用一次（可以跨.py文件调用，每个.py文件就是module）
