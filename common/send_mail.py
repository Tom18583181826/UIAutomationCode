import smtplib
import yagmail
# yagmail是python的一个第三方库，可以让我们以非常简单的方式实现发送邮件功能
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from common.read_ini import ReadIni


class SendMail(object):
    def send_mail(self, path):
        try:
            # 1.配置邮箱服务器信息
            host = "smtp.qq.com"  # 配置邮箱SMTP服务器的主机地址，将来使用这个服务器收发邮件
            # port = "465"  # 配置端口,默认的邮件端口是25，QQ邮箱的端口为465
            sender = ""  # 配置发件人
            auth_code = ""  # 配置邮箱的授权码
            receivers = ""  # 配置收件人，多个收件人可以使用分号或逗号隔开

            # 2.创建邮件对象
            message = MIMEMultipart()  # 实例化邮箱对象，用来设置邮箱的发送信息
            # 设置邮件的抬头信息
            message["from"] = sender  # 发件人
            message["to"] = receivers  # 收件人
            message["subject"] = "测试报告"  # 邮件主题
            # 读取报告内容
            with open(path, mode="rb") as report:
                # r: 以只读方式打开文件。文件的指针将会放在文件的开头。这是 ** 默认模式 **。
                # rb: 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
                # r +: 打开一个文件用于读写。文件指针将会放在文件的开头。
                # rb +: 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
                # w: 打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
                # wb: 以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
                # w +: 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
                # wb +: 以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
                # a: 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
                # ab: 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
                # a +: 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
                # ab +: 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
                mail_body = report.read().decode(encoding="utf8")
                # decode()方法以encoding指定的编码格式解码字符串。默认编码为字符串编码。该方法返回解码后的字符串

            # 3.编写正文
            text = MIMEText(mail_body, "html", "utf8")  # 将测试报告添加到邮件正文中
            message.attach(text)  # 添加正文到邮件对象

            # 4.添加附件
            attachment = MIMEText(mail_body, "base64", "utf8")
            attachment["Content-Type"] = "application/octet-stream"
            # Content-Type：说明内容类型---txt/plain是纯文本类型;Application/octet-stream是添加附件类型.
            attachment["Content-Disposition"] = 'attachment;filename = %s' % path
            message.attach(attachment)  # 添加附件到邮件对象

            # 5.发送邮件
            smtpobj = smtplib.SMTP()  # 通过smtplib模块实例化SMTP对象
            smtpobj.connect(host)  # 连接服务器
            # 邮箱设置时勾选了SSL加密连接，进行防垃圾邮件，SSL协议端口号需要使用465端口号
            smtpobj.login(sender, auth_code)  # 通过账号和授权码登录服务器
            smtpobj.sendmail(sender, receivers.split(";"), message.as_string())
            print("邮件发送成功！！！")
        except smtplib.SMTPException:
            print("邮件发送失败！！！")

    def send_yagmail(self, path):
        yag = yagmail.SMTP(user="发件人邮箱地址", password="", host="")
        subject = "主题"
        contents = "正文"
        yag.send("收件人邮箱地址", subject, contents, path)
        # 如果想给多个人发送邮件，只需把收件人放入一个list
        # path：为本地测试报告的路径（可以通过list写入多个测试报告的路径发送多个附件）


if __name__ == '__main__':
    read = ReadIni()
    report_file_path = read.get_report_file_path()
    test_send = SendMail()
    test_send.send_mail(report_file_path)
