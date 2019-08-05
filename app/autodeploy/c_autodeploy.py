#encoding:utf-8
import ConfigParser
import os,sys,time
import paramiko
from git import Repo
import datetime
def read_config():
    global g_repoPath,g_mvn1,g_mvn2,g_serverIp,g_serverUser,g_serverPwd,g_cmd,g_path,g_cmd1,g_path1,g_cmd2,g_cmd3,g_cmd4,g_targetFileName,g_targetFileName1,g_createFileName,g_createFileName1,g_localMkDirPath,g_localMkDirPath1,g_remoteFileMkDir,g_remoteFileMkDir1,remoteFilePath,remoteFilePath1,localFilePath1,remoteFilePath3
    cf=ConfigParser.ConfigParser()
    cf.read("c_config.ini")
    g_repoPath=cf.get("git","repoPath")
    g_mvn1=cf.get("git","mvn1")
    g_mvn2=cf.get("git","mvn2")
    g_serverIp=cf.get("Ser","serverIp")
    g_serverUser=cf.get("Ser","serverUser")
    g_serverPwd =cf.get("Ser","serverPwd")
    # g_cmd=cf.get("command","cmd")
    # g_path=cf.get("command","path")
    # g_cmd1=cf.get("command","cmd1")
    # g_path1=cf.get("command","path1")
    g_cmd1=cf.get("command","cmd1")
    g_cmd2=cf.get("command","cmd2")
    g_cmd3=cf.get("command","cmd3")
    g_cmd4=cf.get("command","cmd4")
    g_targetFileName=cf.get("baseconf","targetFileName")
    g_targetFileName1=cf.get("baseconf","targetFileName1")
    g_createFileName=cf.get("baseconf","createFileName")
    g_createFileName1=cf.get("baseconf","createFileName1")
    g_localMkDirPath=cf.get("baseconf","localMkDirPath")
    g_localMkDirPath1=cf.get("baseconf","localMkDirPath1")
    g_remoteFileMkDir=cf.get("baseconf","remoteFileMkDir")
    g_remoteFileMkDir1=cf.get("baseconf","remoteFileMkDir1")
    #远程上传jar包路径
    remoteFilePath = g_remoteFileMkDir + g_createFileName
    #远程上传代码com路径
    remoteFilePath1 = g_remoteFileMkDir1 + g_targetFileName1
    #本地com路径
    localFilePath1=g_localMkDirPath1+g_createFileName1
    #远程删除路径
    remoteFilePath3=g_remoteFileMkDir+g_targetFileName
    print g_repoPath
    print g_mvn1
    print g_mvn2
    print g_serverIp
    print g_serverUser
    print g_serverPwd
    # print g_cmd
    # print g_path
    # print g_cmd1
    # print g_path1
    print g_targetFileName
    print g_targetFileName1
    print g_createFileName
    print g_createFileName1
    print g_remoteFileMkDir
    print g_remoteFileMkDir1
    print g_localMkDirPath
    print g_localMkDirPath1
    # print localFilePath1
    # print remoteFilePath
    # print remoteFilePath1
#更新小麦光伏api的代码，并进行打包操作
def family():
    os.chdir(g_repoPath)
    repo=Repo(g_repoPath) #获取一个库
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
    os.chdir(g_repoPath)
    os.system(g_mvn1)
    print 'ok'
    os.system(g_mvn2)
#远程删除服务器的tomcat下的旧包和文件夹，需要优化一下，如果存在就覆盖上传
def remove_remote_file():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(g_serverIp, username=g_serverUser, password=g_serverPwd, allow_agent=True)
    ssh.exec_command("rm -rf " + remoteFilePath3 )
    # ssh.exec_command("rm -rf " + remoteFilePath1)
    print 'ok'
#创建com目录
def mkdir():
    try:
        ssh=paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(g_serverIp,username=g_serverUser,password=g_serverPwd)
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
    t = paramiko.Transport((g_serverIp, 22))
    t.connect(username=g_serverUser, password=g_serverPwd)
    sftp = paramiko.SFTPClient.from_transport(t)
    # sftp.put(g_localMkDirPath + g_createFileName, remoteFilePath, put_call_back)
    sftp.put(g_localMkDirPath + g_createFileName, remoteFilePath)
    print "上传成功"
    upload_files(localFilePath1, remoteFilePath1, g_serverIp, g_serverUser, g_serverPwd)
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
    output1 = remoteRun(cmd1)
    # print output1

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
        output3 = remoteRun(cmd2)
        if (cmd3) in output3:
            print("服务未能停止运行！！！")
            #退出进程
            sys.exit(3)
        else:
            print("服务停止成功")
    else:
        print("没有")
    # printOutput=True 打印输出
    print("启动tomcat")
    remoteRun(cmd4,printOutput=True)

    print("检查tomcat是否运行成功")
    output4 = remoteRun(cmd2)

    #如果存在，运行成功
    if (cmd3) in output4:
        print("tomcat服务运行成功")
    else:
        print('服务没有运行成功！')
        sys.exit(3)

# def ssh_client(sys_ip,username,password,cmd,path):
#     try:
#         #创建ssh客户端
#         ssh = paramiko.SSHClient()
#         #第一次ssh远程时会提示输入yes或者no
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         #密码方式远程连接
#         ssh.connect(sys_ip, 22, username=username, password=password, timeout=20)
#         #执行命令
#         stdin, stdout, stderr = ssh.exec_command('cd ' + path + ';' + cmd)
#         #获取命令执行结果,返回的数据是一个list
#         print stdout.read()
#         result = stdout.readlines()
#         # for x in result:
#         #     print x.strip("\n")
#         return result
#     except:
#         print '＼tError＼n'
# 上传文件进度反馈
def put_call_back(start, end):
    process = (float(start) / end) * 100
    print("当前上传进度为: %.2f %%" % process)
if __name__ == '__main__':
    read_config()
    family()
    remove_remote_file()
    #  mkdir()
    ftp_upload_file()
    time.sleep(15)
    # ssh_client(g_serverIp,g_serverUser,g_serverPwd,g_cmd,g_path)
    # ssh_client(g_serverIp,g_serverUser,g_serverPwd,g_cmd1,g_path1)
    #创建SHHClient示例对象
    ssh = paramiko.SSHClient()
    #调用方法，表示没有存储远程机器的公钥，允许访问
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #连接远程服务器 地址，端口，用户名密码
    ssh.connect(g_serverIp,username=g_serverUser,password=g_serverPwd)
    start_service(g_cmd1,g_cmd2,g_cmd3,g_cmd4)
    print datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")



