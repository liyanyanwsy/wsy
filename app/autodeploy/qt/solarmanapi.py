#encoding:utf-8
import os
from git import Repo
import paramiko
import datetime
import zipfile
#更新小麦专业版api的代码，并进行打包操作
def family():
    repoPath=r'D:\\xingit\\solarman-api-business'
    repo=Repo(repoPath) #获取一个库
    # print(repo.branches) #获取所有分支
    print"所在分支为：%s" %repo.active_branch#获取当前活动分支
    #  切换分支
    dev = repo.heads.dev          # 获取dev分支
    curBranch = repo.head.reference     # 当前活动分支
    if curBranch != dev:
        repo.heads.dev.checkout()    # 切换到dev
    #拉取代码
    remote = repo.remote()
    # 从远程版本库拉取分支
    remote.pull()
    # 推送本地分支到远程版本库
    # remote.push()
    # 重命名远程分支
    # remote.rename('new_origin')
    # os.getcwd()
    # os.chdir('D:\\xingit\\solarman-api-business')
    os.chdir(repoPath)
    os.system('mvn clean')
    os.system('mvn package')
#远程删除服务器的tomcat下的旧包和文件夹，需要优化一下，如果存在就覆盖上传
def remove_remote_file():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(serverIp, username=serverUser, password=serverPwd, allow_agent=True)
    ssh.exec_command("rm -rf " + remoteFilePath3)
    ssh.exec_command("rm -rf " + remoteFilePath1)
    print 'ok'
#创建com目录
def mkdir():
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(serverIp,username=serverUser,password=serverPwd)
        sftp = ssh.open_sftp()
        filename=remoteFilePath1
        #需要增加一条判断文件是否存在，如果存在不创建，存在就补创建
        sftp.mkdir(filename)
        print "Create folder %s in remote hosts successfully!\n" %filename
        ssh.close()
    except:
        print "Create folder failure!\n"
#上传文件
def ftp_upload_file():
    t = paramiko.Transport((serverIp, 22))
    t.connect(username=serverUser, password=serverPwd)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(localMkDirPath + targetFileName, remoteFilePath, put_call_back)
    print "上传成功"
    upload_files(localFilePath1, remoteFilePath1, serverIp, serverUser, serverPwd)
    print("上传成功")
#递归上传目录里面的文件或者文件夹
def upload_files(local_dir, remote_dir, hostname, username, password):
    try:
        t = paramiko.Transport((hostname, 22))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)

        print('upload file start %s ' % datetime.datetime.now())
        for root, dirs, files in os.walk(local_dir):
            print('[%s][%s][%s]' % (root, dirs, files))
            for filespath in files:
                local_file = os.path.join(root, filespath)
                print(11, '[%s][%s][%s][%s]' % (root, filespath, local_file, local_dir))
                a = local_file.replace(local_dir, '').replace('\\', '/').lstrip('/')
                print('01', a, '[%s]' % remote_dir)
                remote_file = os.path.join(remote_dir, a).replace('\\', '/')
                print(22, remote_file)
                try:
                    sftp.put(local_file, remote_file)
                except Exception as e:
                    sftp.mkdir(os.path.split(remote_file)[0])
                    sftp.put(local_file, remote_file)
                    print("66 upload %s to remote %s" % (local_file, remote_file))
            for name in dirs:
                local_path = os.path.join(root, name)
                print(0, local_path, local_dir)
                a = local_path.replace(local_dir, '').replace('\\', '/').lstrip('/')
                print(1, a)
                print(1, remote_dir)
                # remote_path = os.path.join(remote_dir, a).replace('\\', '/')
                remote_path = remote_dir + a
                print(33, remote_path)
                try:
                    sftp.mkdir(remote_path)
                    print(44, "mkdir path %s" % remote_path)
                except Exception as e:
                    print(55, e)
        print('77,upload file success %s ' % datetime.datetime.now())
        t.close()
    except Exception as e:
        print(88, e)
#远程执行linux命令
def ssh_clinet(sys_ip,username,password,cmd,path):
    try:
        #创建ssh客户端
        ssh = paramiko.SSHClient()
        #第一次ssh远程时会提示输入yes或者no
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #密码方式远程连接
        ssh.connect(sys_ip, 22, username=username, password=password, timeout=20)
        #执行命令
        stdin, stdout, stderr = ssh.exec_command('cd ' + path + ';' + cmd)
        #获取命令执行结果,返回的数据是一个list
        print stdout.read()
        result = stdout.readlines()
        # for x in result:
        #     print x.strip("\n")
        return result
    except:
        print '＼tError＼n'
# 上传文件进度反馈
def put_call_back(start, end):
    process = (float(start) / end) * 100
    print("当前上传进度为: %.2f %%" % process)
if __name__ == '__main__':
    #小麦专业版测试环境部署
    serverIp = '192.168.1.58'
    serverUser = 'root'
    serverPwd = '123456'
    # 项目名称
    targetFileName = 'solarman-service-2.0.34.22.jar'
    targetFileName1 = 'com/'
    # 本地文件名称
    createFileName = 'solarman-service-2.0.34.36.jar'
    createFileName1 = '\com'
    # 本地项目根目录
    localMkDirPath = r'D:/xingit/solarman-api-business/target/solarman-app-business/WEB-INF/lib/'
    localMkDirPath1=r'D:\xingit\solarman-api-business\target\classes'
    # # 本地项目的target目录(jar 包生成的目录)
    # localMkDirPath = projectPath + r'target/'
    # 远程服务器的tomcat路径  xxx是你war解压的文件夹  一般war上传至tomcat下 会直接解压
    remoteFileMkDir = '/data/tomcat_servers/solarman2_b_api_pro_18015/webapps/ROOT/WEB-INF/lib/'
    remoteFileMkDir1 = '/data/tomcat_servers/solarman2_b_api_pro_18015/webapps/ROOT/WEB-INF/classes/'
    # 远程服务器
    #远程上传jar包路径
    remoteFilePath = remoteFileMkDir + createFileName
    #远程删除路径
    remoteFilePath3=remoteFileMkDir+targetFileName
    #远程上传代码路径
    remoteFilePath1 = remoteFileMkDir1 + targetFileName1
    #本地com路径
    localFilePath1=localMkDirPath1+createFileName1

    family()
    remove_remote_file()
    mkdir()
    ftp_upload_file()
    cmd='./startup.sh'
    path='/data/tomcat_servers/solarman2_b_api_pro_18015/bin'
    ssh_clinet(serverIp,serverUser,serverPwd,cmd,path)
    # cmd1='tail -fn 30 catalina_2018-10-08.out'
    # path1='/data/tomcat_servers/solarman2_api_18003/logs'
    # ssh_clinet(serverIp,serverUser,serverPwd,cmd1,path1)

    # upload_files(localFilePath1, remoteFilePath1, serverIp, serverUser, serverPwd)

    # #小麦专业预发布环境部署
    # serverIp = '47.88.18.157'
    # serverUser = 'root'
    # serverPwd = 'dwm2yJ$84Y6WW%4a'
    # targetFileName = 'solarman-family-service-1.1.32.jar'
    # targetFileName1 = '\com'
    # createFileName = 'solarman-family-service-1.1.32.jar'
    # createFileName1 = 'com/'
    # localMkDirPath = r'D:/xingit/solarman-family-API/target/solarman-family-api/WEB-INF/lib/'
    # localMkDirPath1=r'D:\xingit\solarman-family-API\target\classes'
    # remoteFileMkDir = '/data/tomcat_servers/solarman2_api_test_18011/webapps/ROOT/WEB-INF/lib'
    # remoteFileMkDir1 = '/data/tomcat_servers/solarman2_api_test_18011/webapps/ROOT/WEB-INF/classes/'
    # remoteFilePath = remoteFileMkDir + targetFileName
    # remoteFilePath1 = remoteFileMkDir1 + createFileName1
    # localFilePath1=localMkDirPath1+targetFileName1
    # family()
    # remove_remote_file()
    # mkdir()
    # ftp_upload_file()
    # cmd='./startup.sh'
    # path='/data/tomcat_servers/solarman2_api_test_18011/bin'
    # ssh_clinet(serverIp,serverUser,serverPwd,cmd,path)




