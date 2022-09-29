import json

from common.read_ini import ReadIni


class ReadJson:
    def read_json_data(self, file_path):
        with open(file_path, encoding="utf8") as file:
            return json.load(file)
            # 1.loads()方法的参数为字符串，可将参数转换成json对象；在使用loads的时候json字符串必须要用双引号，否则会报错；
            # 2.load()方法的参数为文件对象；
            # 3.dumps()方法将json转换成字符串；
            # 4.dump()方法将json数据写入到文件中。


if __name__ == '__main__':
    read_ini = ReadIni()
    json_path = read_ini.get_json_file_path()
    read_json = ReadJson()
    json_data = read_json.read_json_data(json_path)
    print(json_data)
