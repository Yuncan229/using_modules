# 练习：用Python完成自动群发邮件

# smtplib模块 - 发邮件需要用到的功能
# import smtplib
#
# server = smtplib.SMTP()
# server.connect(host, port)
# server.login(username, password)
# server.sendmail(from_addr, to_addr, msg.as_string())
# server.quit()

# 版本1.0: 找到并学习发邮件的模块，给自己发一封一句话的简单邮件
# 引入smtplib模块
import smtplib as s
# 引入email包中构建文本内容的方法
from email.mime.text import MIMEText
from email.header import Header

# 1.定义一些需要用到的变量
username = '359570622@qq.com'
password = 'vazledraxtywbige'
rev_address = '359570622@qq.com'


# 2.实例化类，实例为smtp；因为QQ邮箱的端口是加密的方式，所以要用类：SMTP_SSL
smtp = s.SMTP_SSL(host='smtp.qq.com')

# 开始调用类SMTP的方法
# 连接到QQ邮箱的服务器
smtp.connect(host='smtp.qq.com',port = 465)


# 登录发信邮箱
smtp.login(username,password)

# 确定邮件的正文内容(第一个参数为内容，第二个参数为格式(plain为纯文本),第三个参数为编码)
msg = MIMEText('send by python','plain','utf-8')


# 发送邮件
smtp.sendmail(username, rev_address,msg.as_string())

# 关闭服务器
smtp.quit()


# 版本2.0: 给自己发一封有完整邮件头，完整正文内容的邮件

# 版本3.0：群发完整邮件
