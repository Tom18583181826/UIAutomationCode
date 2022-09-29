import csv
from itertools import islice
from common.read_ini import ReadIni


# 可以把Excel表格通过文件"另存为"保存为CSV格式的文件，但不要直接修改后缀名来创建CSV文件，因为这样的文件并非真正的CSV类型的文件

class ReadCsv:
    def read_csv_data(self, file_path):
        with open(file_path, "r", encoding="gbk") as file:
            data = csv.reader(file)
            # 使用csv标准库中的reader()方法读取文件
            databases = []
            # 创建一个总列表用于存放从csv文件中读取的数据
            for row in islice(data, 1, None):
                # Python的内建模块itertools提供了用于操作迭代对象的函数，即islice()函数，
                # 它可以返回一个迭代器第一个参数指定的迭代对象，
                # 第二个参数指定开始迭代的位置，第三个参数表示结束位
                # 迭代返回一个列表
                databases.append(row)
                # 将读取的每行数据添加到总列表中
            return databases


if __name__ == '__main__':
    readini = ReadIni()
    csvpath = readini.get_csv_file_path()
    readcsv = ReadCsv()
    csvdata = readcsv.read_csv_data(csvpath)
    print(csvdata)
