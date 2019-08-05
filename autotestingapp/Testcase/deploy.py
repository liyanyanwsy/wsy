# encoding:utf-8  
  
from fabric.api import *  
import time  
  
TOMCAT_HOME = /data/tomcat_servers/solarman2_b_api_pro_18015"  
WAR_DIR = "D:\Program Files\Git\11\solarman-api-business\target"  
  
#要远程部署的几个服务器  
servers = '192.168.1.58'
  
#这几个服务器有统一的用户名访问  
env.user= "root "  
  
#服务器用户密码  
env.password = "123456"  
  
def deploy(projectname):  
    for server in servers:  
        print("正在部署服务器：" +  server + " 项目名：" + projectname)  
        with settings(host_string = server):  
            deploy_one_server(projectname)  
            print("部署服务器 "+ server +" 项目" + projectname + " 完成!")  
            print "休息60秒"  
            time.sleep(60)  
  
#部署一个服务器  
def deploy_one_server(projectname):  
    warfilename = projectname + ".war"  
    #1，上传文件到tomcat根目录  
    print("1，上传文件到tomcat根目录")  
    with lcd(WAR_DIR):  
        with cd(TOMCAT_HOME):  
            put(warfilename,warfilename)  
            run("ls")  
  
    #2，关闭服务器  
    print "2，关闭服务器"  
    close_tomcat()  
  
    #3，删除原有的部署文件  
    print "3，删除原有的部署文件"  
    with cd(TOMCAT_HOME + "/webapps/"):  
        run("rm -rf " + projectname + "/")  
        run("rm -rfv " + warfilename)  
  
    #4，将已上传的文件放到tomcat项目目录  
    print "4，将已上传的文件放到tomcat项目目录"  
    with cd(TOMCAT_HOME):  
        run("mv " + warfilename + " ./webapps/")  
  
    #5，启动服务器  
    print "5，启动服务器"  
    run(TOMCAT_HOME +"/bin/startup.sh",pty=False)  
  
#关闭tomcat服务器  
def close_tomcat():  
    #kill可能会因为没有tomcat线程，导致关闭命令失败，所以需要在产生异常时继续执行  
    with settings(  
        hide('warnings', 'running', 'stdout', 'stderr'),  
        warn_only=True  
    ):  
        run("ps -ef |grep tomcat |grep -v grep   |awk -F \" \" '{print $2}' | xargs kill -9")  
