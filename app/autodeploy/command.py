#encoding:utf-8
import paramiko
import sys
HOST = '192.168.1.58'
PORT = 22
USER = 'root'
PASSWD = '123456'
#创建SHHClient示例对象
ssh = paramiko.SSHClient()
#调用方法，表示没有存储远程机器的公钥，允许访问
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接远程服务器 地址，端口，用户名密码
ssh.connect(HOST,PORT,USER,PASSWD)
def remoteRun(cmd, printOutput=True):
    """执行远程操作命令"""
    stdin, stdout, stderr = ssh.exec_command(cmd)
    output = stdout.read().decode()
    errinfo = stderr.read().decode()
    if printOutput:
        print(output + errinfo)
    return output + errinfo
def start_service(cmd1,cmd2,cmd3,cmd4):
    print("检查tomcat是否有运行......")
    output1 = remoteRun("ps ax |grep -v grep |grep 'solarman2_api_18003' |awk '{print   $1}'")
    output11=output1.split()
    print output11
    print type(output11)
    #如果存在，则杀死进程
    if len(output11)!=0:
        print("tomcat服务运行中，停止服务......")
        for i in output11:
            #杀死进程
            print i
            output2 = remoteRun('kill -9 %s' %i)
        #再次检查是否有先前版本运行
        output3 = remoteRun("ps -ef|grep solarman2_api_18003|grep -v grep")
        if ("solarman2_api_18003") in output3:
            print("服务未能停止运行！！！")
            #退出进程
            sys.exit(3)
        else:
            print("服务停止成功")
    else:
        print("没有")
    # printOutput=True 打印输出
    print("启动tomcat")
    remoteRun("cd /data/tomcat_servers/solarman2_api_18003/bin;sh startup.sh;sleep 5",printOutput=True)

    print("检查tomcat是否运行成功")
    output4 = remoteRun('ps -ef|grep solarman2_api_18003|grep -v grep')

    #如果存在，运行成功
    if ("solarman2_api_18003") in output4:
        print("tomcat服务运行成功")
    else:
        print('服务没有运行成功！')
        sys.exit(3)
    # output5 = remoteRun('cd /data/tomcat_servers/solarman2_api_18003/logs;tail -fn 30 catalina_2018-11-16.out;sleep 5')

if __name__ == '__main__':
    cmd1="ps ax |grep -v grep |grep 'solarman2_api_18003' |awk '{print   $1}'"
    cmd2='ps -ef|grep solarman2_api_18003|grep -v grep'
    cmd3='solarman2_api_18003'
    cmd4='cd /data/tomcat_servers/solarman2_api_18003/bin;sh startup.sh;sleep 5'
    start_service(cmd1,cmd2,cmd3,cmd4)

