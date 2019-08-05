#coding:utf-8
import smtplib
from email.mime.text import MIMEText
def sendemail():
    try:
        #发送相关参数
        smtpserver="smtp.qq.com"
        port=465
        sender="2972049643@qq.com"
        password="vszgxojfzyktdcje"
        # receiver="wsy20160123@163.com"
        receiver="2972049643@qq.com"
        acc = 'wsy20160123@163.com'
        #编辑邮件内容
        subject="小麦专业版app"
        body='<p>小麦专业版登录异常，请关注！<p>'
        msg=MIMEText(body,"html","utf-8")
        msg['from']=sender
        msg['to']=receiver
        msg['Cc']=acc
        msg['subject']=subject
        #发送邮件
        # smtp=smtplib.SMTP()
        # smtp.connect(smtpserver)
        smtp=smtplib.SMTP_SSL(smtpserver,port)
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
        print "send mail successed!"
    except Exception,e:
        print e

sendemail()