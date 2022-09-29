import sys
# logging(日志)模块是python内置的标准模块，主要用于输出运行日志，可以设置输出日志的等级，日志保存路径，日志文件回滚等

# 日志与print相比的优点：
# 1.可以通过设置不同的日志等级只输出重要的信息，而不必显示大量的调试信息；
# 2.print将所有的信息都输出到标准输出中，严重影响编程人员从标准输出中查看其他数据，logging则可以由编程人员决定将信息输出到什么地方，以及怎么输出。

# 日志级别：
# OFF 关闭，不打印日志
# FATAL   致命，指明非常严重的可能会导致应用终止执行错误事件
# ERROR   错误，指明错误事件，但应用可能还能运行
# WARN    警告，指明可能潜在的危险状况
# INFO    信息，指明描述信息，从颗粒度上描述了应用运行过程
# DEBUG   调试，指明细致的事件信息，对调试应用最有用
# TRACE   跟踪，指明程序运行轨迹，比debug级别颗粒度更细
# ALL 所有，所有日志级别，包括定制级别
from logging import Logger
from logging import Formatter
from logging import FileHandler
from logging import StreamHandler


# logging框架主要由四部分组成：
# 1.logging(记录器对象):可供程序直接调用的接口
# 2.Handlers（处理器对象）:决定将日志记录分配至正确的目的地
# 3.Filters(过滤器对象):提供更细粒度的日志是否输出的判断
# 4.Formatters(格式器对象):制定最终记录打印的格式布局


class GetLog:
    def get_log(self, log_path):
        # 实例化Logger类
        log_obj = Logger("test.log")
        # 设置日志格式
        logformat = Formatter("[%(asctime)s]:%(message)s")
        # 日志格式：
        # %(levelno)s:打印日志级别的数值
        # %(levelname)s:打印日志级别的名称
        # %(pathname)s:打印当前执行程序的路径
        # %(filename)s:打印当前执行程序名
        # %(funcName)s:打印日志的当前函数
        # %(lineo)d:打印日志的当前行号
        # %(asctime)s:打印日志的时间
        # %(thread)d:打印线程ID
        # %(threadName)s:打印线程名称
        # %(precess)d:打印进程ID
        # %(message)s:打印日志信息

        # 实例化把日志输出到指定位置对象
        filepath = FileHandler(log_path)
        # FileHandler(filename[,mode])---用于向一个文件输出日志信息。
        #                             不过FileHandler会帮你打开这个文件。
        # 参数: mode是文件的打开方式,默认是’a'，即添加到文件末尾。

        # 把读取出来的内容设置为事先设置好的日志格式
        filepath.setFormatter(logformat)
        # 输出日志
        log_obj.addHandler(filepath)

        # 实例化把日志输出到控制台对象
        console = StreamHandler(sys.stdout)
        # StreamHandler(stream=None)---流handler
        # ---日志信息会输出到指定的stream中,如果stream为空则默认输出到sys.stderr
        # 能够将日志信息输出到sys.stdout,sys.stderr或者类文件对象
        # (更确切点，就是能够支持write()和flush()方法的对象)

        # stdin,stdout以及stderr变量包含与标准 I/O 流对应的流对象,是内建在每一个UNIX系统中的管道,
        # 当我们打印print的时候就是往stdout里面管道里面塞进去打印的数据,stderr就是错误信息的打印,和stdout一样

        # stdout就像是一个类文件对象, 因为你可以将他赋值给任意的一个文件对象, 重定向输出
        # stdin标准化输入, 可以理解为input

        # 把读取出来的内容设置为事先设置好的日志格式
        console.setFormatter(logformat)
        # 输出日志
        log_obj.addHandler(console)

        return log_obj
