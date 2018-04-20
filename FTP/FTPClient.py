import ftplib, os, socket, sys, io

'''创建与ftp服务器的连接
   需要先有配置好的ftp服务器
   可以使用一些开放的ftp服务器
   也可以自建服务器
   windows10 下创建ftp服务器可以参见
   《Win10如何搭建FTP服务器.mhtml》
   如果出现连接不上，需要关闭win的防火墙
'''
HOST = '192.168.1.108'


def dir():
    '''
    相当于执行dir命令，查看ftp目录
    :return:
    '''
    try:
        f = ftplib.FTP('192.168.1.108')
        # 采用匿名登陆,如有用户名密码，作为参数转递即可
        f.login()
        # 直接使用dir（）方法时，中文文件名会显示乱码
        # f.dir()
        # ftplib.FTP默认采用latin-1编码，因此总问操作系统需要修改f的编码,否则中文文件名会出现乱码
        f.encoding = 'gbk'
        # print(f.encoding)

        print(f.retrlines('list'))
    except (socket.error, socket.gaierror) as e:
        print(e)
    else:f.quit()


def down():
    try:
        f = ftplib.FTP(HOST)
        f.encoding='gbk'
        f.login()
        #进入ftp上的目录
        f.cwd('准备')
        f.retrbinary('retr %s' % 'IMG_0128.JPG', open('d:/testimg.jpg', 'wb').write)
        #f.quit()
    except (socket.error, socket.gaierror) as e:
        print(e)
    else: f.quit()


# dir()
down()
