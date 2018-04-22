import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def simpleendail():
    '''
    发送简单的邮件（不包含html、附件等）
    :return:
    '''
    s = smtplib.SMTP('smtp_pop3_imap4.163.com')
    s.set_debuglevel(1)
    # 改成你自己的邮箱
    s.login('yourname', 'yourpass')
    # 第一个参数是发送者邮箱；第二个参数元组包含接收用户邮箱列表，第三个参数格式需要固定，即：From:....\r\nTo:....\r\nSubject:....\r\n\r\n.......
    # 第三个参数注意subject之后是两个\r\n,最后以点结束
    s.sendmail('frommailaddr', ('tomailaddr'),
               '''From:frommailaddr\r\nTo:tomailaddr\r\nSubject:mail test\r\n\r\ntesttest3\r\n.''')
    s.close()


def adjunctemail():
    '''
    生成复杂邮件（含有text/html和附件）
    :return:
    '''
    mail = MIMEMultipart('alternative')
    '''
    下面创建了两个MIMEText(text和html),多部分选择消息通常包含两部分，一是以纯文本表示的邮件消息正文，以及等价的 HTML
格式。由邮件客户端来决定显示哪一部分。例如，基于 Web 的电子邮件系统会显示 HTML
版本，而基于命令行的邮件阅读器只会显示纯文本版本。
    '''
    text = MIMEText('test adjunct mail-text\r\n', 'plain')
    html = MIMEText('<html><body>test adjunct mail-html</body></html>', 'html')
    image = adj_img('d:/testimg.jpg', 'testimg.jpg')
    mail.attach(text)
    mail.attach(html)
    mail.attach(image)
    return mail


def adj_img(path, imageName):
    image = open(path, 'rb')
    data = image.read()
    image.close()
    image = MIMEImage(data, imageName)
    image.add_header('Content-Disposition', 'attachment;filename=%s' % imageName)
    return image


def sendAdjunctMail(username, pwd, fr, to, msg):
    s = smtplib.SMTP('smtp_pop3_imap4.163.com')
    #设置为显示更详细的调试信息
    s.set_debuglevel(True)
    s.login(username, pwd)
    s.sendmail(fr, to, msg.as_string())
    s.quit()


if __name__ == '__main__':
    mail = adjunctemail()
    mail['From'] = 'frommailaddr'
    mail['To'] = ('tomailaddr')
    mail['Subject'] = 'test subject'
    sendAdjunctMail('yourname', 'yourpass', 'frommailaddr', 'tomailaddr', mail)
