# coding=utf-8
__author__ = 'zgd'
import smtplib
import email.MIMEMultipart# import MIMEMultipart
import email.MIMEText# import MIMEText
import email.MIMEBase# import MIMEBase
import os.path
import mimetypes
class SendEmail():

    def sendEmail(self,filepath):
        """定义发送邮箱的类接收创建的"""
        #发件箱
        From = "test_zhai_sp@126.com"
        #收件箱
        To = "2686852189@qq.com"
        file_name =filepath#附件名
        server = smtplib.SMTP("smtp.126.com")
        # 仅smtp服务器需要验证时----授权码 授权码--授权码,并不是密码
        server.login("test_zhai_sp@126.com","2017shixiaoyu")
        # 构造MIMEMultipart对象做为根容器
        main_msg = email.MIMEMultipart.MIMEMultipart()
        # 构造MIMEText对象做为邮件显示内容并附加到根容器
        text_msg = email.MIMEText.MIMEText("37testReport",_charset="utf-8")
        main_msg.attach(text_msg)
        # 构造MIMEBase对象做为文件附件内容并附加到根容器
        ## 读入文件内容并格式化 [方式1]－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－
        data = open(file_name, 'rb')
        ctype,encoding = mimetypes.guess_type(file_name)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'
        maintype,subtype = ctype.split('/',1)
        file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
        file_msg.set_payload(data.read())
        data.close( )
        email.Encoders.encode_base64(file_msg)#把附件编码
         ## 设置附件头
        basename = os.path.basename(file_name)
        file_msg.add_header('Content-Disposition','attachment', filename = basename)#修改邮件头
        main_msg.attach(file_msg)
        # 设置根容器属性
        main_msg['From'] = From
        main_msg['To'] = To
        main_msg['Subject'] = "mail test "
        main_msg['Date'] = email.Utils.formatdate( )
        # 得到格式化后的完整文本
        fullText = main_msg.as_string( )
        # 用smtp发送邮件
        try:
            server.sendmail(From, To, fullText)
        finally:
            server.quit()
