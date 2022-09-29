from common.read_ini import ReadIni


class ReadTxt:
    def read_txt_data(self, file_path):
        with open(file_path, "r") as file:
            # 读取文件，“r”表示以读的方式打开文件
            data = file.readlines()
            # read():读取整个文件
            # readline():读取一行数据
            # readlines():读取所有行的数据
            databases = []
            # 创建一个总列表用于存放从txt文件中读取的数据
            header = True
            # 设置表头变量并将其值设置为True
            for row in data:
                # 循环遍历每一行的数据
                if header:
                    # 丢弃表头
                    header = False
                    continue
                row_data_list = row[:-1].split(":")
                # 因为读取的每一行数据结尾都有一个换行符“\n”,所以使用row[:-1]（左闭右开）对字符串进行切片，以去掉换行符
                row_data_tuple = tuple(row_data_list)
                # 将临时的行数据列表转换成元组
                row_data_list.clear()
                # 清空临时的行数据列表
                databases.append(row_data_tuple)
                # 将行数据元组添加到总列表中
            return databases


if __name__ == '__main__':
    readini = ReadIni()
    txtpath = readini.get_txt_file_path()
    readtxt = ReadTxt()
    txtdata = readtxt.read_txt_data(txtpath)
    print(txtdata)
