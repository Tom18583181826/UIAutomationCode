from xml.dom.minidom import parse

from common.read_ini import ReadIni


class ReadXml:
    def read_xml_data(self, file_path):
        fileobject = parse(file_path).documentElement
        # parse():用于读取XML文件
        # documentElement():用于获取文档元素对象

        tag_name = fileobject.getElementsByTagName("platform")
        # getElementsByTagName()用于获取文件中的标签
        print(tag_name[0].firstChild.data)
        # firstChild属性返回被选节点的第一个子节点
        # data:获取该节点的数据

        login_info = fileobject.getElementsByTagName("login")
        print(login_info[0].getAttribute("username"))
        # getAttribute():获取元素的属性值
        print(login_info[0].getAttribute("password"))


if __name__ == '__main__':
    readini = ReadIni()
    xmlpath = readini.get_xml_file_path()
    readxml = ReadXml()
    readxml.read_xml_data(xmlpath)
